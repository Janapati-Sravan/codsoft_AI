import cv2
import numpy as np
import pickle
from collections import deque, Counter
from insightface.app import FaceAnalysis

# ─────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────
SIMILARITY_THRESH = 0.35
MIN_MARGIN        = 0.04
SMOOTH_FRAMES     = 6
PROCESS_EVERY     = 3
FRAME_WIDTH       = 480
MODEL_PATH        = "face_model.pkl"
# ─────────────────────────────────────────

if not __import__("os").path.exists(MODEL_PATH):
    print("ERROR: face_model.pkl not found!")
    print("Run:  python train.py  first")
    exit()

with open(MODEL_PATH, "rb") as f:
    data = pickle.load(f)

known_embeddings = np.array(data["embeddings"])
known_names      = data["names"]
print("People loaded:", list(set(known_names)))

app = FaceAnalysis(name="buffalo_sc", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0, det_size=(320, 320))

name_buffer = deque(maxlen=SMOOTH_FRAMES)


def identify(embedding):
    sims     = known_embeddings @ embedding
    best_idx = int(np.argmax(sims))
    best_sim = float(sims[best_idx])

    if best_sim < SIMILARITY_THRESH:
        return "Unknown", best_sim

    if len(sims) > 1:
        sorted_sims = np.sort(sims)[::-1]
        if (best_sim - sorted_sims[1]) < MIN_MARGIN:
            return "Unknown", best_sim

    return known_names[best_idx], best_sim


def smooth(name):
    name_buffer.append(name)
    top, count = Counter(name_buffer).most_common(1)[0]
    return top if count >= max(2, SMOOTH_FRAMES // 2) else "..."


camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
camera.set(cv2.CAP_PROP_FPS, 30)

if not camera.isOpened():
    print("ERROR: Camera not found!")
    exit()

print(f"Running | Q=quit | +/- = tune threshold (current: {SIMILARITY_THRESH})")

results     = []
frame_count = 0

while True:
    ret, frame = camera.read()
    if not ret:
        break

    frame_count += 1

    if frame_count % PROCESS_EVERY == 0:
        h, w  = frame.shape[:2]
        scale = FRAME_WIDTH / w
        small = cv2.resize(frame, (FRAME_WIDTH, int(h * scale)))
        faces = app.get(small)

        if len(faces) == 0:
            name_buffer.clear()
            results = []
        else:
            results = []
            for face in faces:
                raw_name, sim = identify(face.normed_embedding)
                stable_name   = smooth(raw_name)
                bbox = (face.bbox / scale).astype(int)
                results.append((bbox, stable_name, sim))

    for bbox, name, sim in results:
        x1, y1, x2, y2 = bbox
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(frame.shape[1], x2), min(frame.shape[0], y2)
        color = (0, 210, 0) if name not in ("Unknown", "...") else (0, 0, 220)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.rectangle(frame, (x1, y2-32), (x2, y2), color, cv2.FILLED)
        cv2.putText(frame, f"{name}  {sim:.2f}",
                    (x1+5, y2-8), cv2.FONT_HERSHEY_DUPLEX, 0.65, (255,255,255), 1)

    cv2.putText(frame, f"Thresh:{SIMILARITY_THRESH:.2f}  +/- to tune",
                (10, 26), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255,220,0), 2)
    cv2.imshow("Face Recognition", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key in (ord("+"), ord("=")):
        SIMILARITY_THRESH = min(0.9, round(SIMILARITY_THRESH + 0.02, 2))
        name_buffer.clear()
        print(f"Threshold -> {SIMILARITY_THRESH}")
    elif key == ord("-"):
        SIMILARITY_THRESH = max(0.1, round(SIMILARITY_THRESH - 0.02, 2))
        name_buffer.clear()
        print(f"Threshold -> {SIMILARITY_THRESH}")

camera.release()
cv2.destroyAllWindows()