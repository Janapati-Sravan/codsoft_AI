import cv2
import os
import sys
import numpy as np
import pickle
from insightface.app import FaceAnalysis

DATASET_PATH  = "dataset"
MODEL_PATH    = "face_model.pkl"
PHOTOS_NEEDED = 50

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def capture_photos():
    print("\n=== CAPTURE MODE ===")
    print("Enter person names one by one.")
    print("Type 'done' when finished all people.\n")

    while True:
        person_name = input("Enter person name (or 'done' to finish): ").strip()
        if person_name.lower() == "done":
            break
        if not person_name:
            continue

        save_folder = os.path.join(DATASET_PATH, person_name)
        os.makedirs(save_folder, exist_ok=True)
        existing = len([f for f in os.listdir(save_folder)
                        if f.lower().endswith((".jpg", ".jpeg", ".png"))])
        print(f"\nCapturing for '{person_name}' (existing: {existing})")
        print("SPACE = capture | Q = next person | Move head slightly each shot!\n")

        camera = cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        count = 0

        while True:
            ret, frame = camera.read()
            if not ret:
                break

            gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.1, 5, minSize=(80, 80))
            face_found = len(faces) > 0

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            status = f"{count}/{PHOTOS_NEEDED} | {'FACE OK - Press SPACE' if face_found else 'No face'}"
            cv2.putText(frame, status, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                        (0, 255, 0) if face_found else (0, 0, 255), 2)
            cv2.putText(frame, f"Person: {person_name}", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 220, 0), 2)

            bar_w = int((count / PHOTOS_NEEDED) * frame.shape[1])
            cv2.rectangle(frame, (0, frame.shape[0]-10),
                          (bar_w, frame.shape[0]), (0, 200, 0), -1)

            cv2.imshow(f"Capturing: {person_name}", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord(" ") and face_found:
                x, y, w, h = max(faces, key=lambda f: f[2]*f[3])
                pad = int(w * 0.2)
                x1, y1 = max(0, x-pad), max(0, y-pad)
                x2, y2 = min(frame.shape[1], x+w+pad), min(frame.shape[0], y+h+pad)
                face_crop = frame[y1:y2, x1:x2]
                filename = os.path.join(save_folder,
                                        f"{person_name}_{existing+count+1}.jpg")
                cv2.imwrite(filename, face_crop)
                count += 1
                print(f"  Saved {count}/{PHOTOS_NEEDED}")
                if count >= PHOTOS_NEEDED:
                    print(f"Done! {PHOTOS_NEEDED} photos for '{person_name}'")
                    break
            elif key == ord("q"):
                print(f"Stopped. {count} photos saved for '{person_name}'")
                break

        camera.release()
        cv2.destroyAllWindows()

    print("\nCapture finished. Starting training...\n")


def train():
    print("=" * 45)
    print("  TRAINING")
    print("=" * 45)

    app = FaceAnalysis(name="buffalo_sc", providers=["CPUExecutionProvider"])
    app.prepare(ctx_id=0, det_size=(320, 320))

    all_embeddings = []
    all_names      = []

    if not os.path.exists(DATASET_PATH):
        print(f"ERROR: '{DATASET_PATH}' folder not found!")
        print("Run:  python train.py --capture  first")
        exit()

    for person_name in sorted(os.listdir(DATASET_PATH)):
        person_folder = os.path.join(DATASET_PATH, person_name)
        if not os.path.isdir(person_folder):
            continue

        print(f"\nPerson: {person_name}")
        count = 0

        for img_file in os.listdir(person_folder):
            img_path = os.path.join(person_folder, img_file)
            img = cv2.imread(img_path)
            if img is None:
                continue
            faces = app.get(img)
            if len(faces) == 0:
                print(f"  NO FACE: {img_file}")
                continue
            face = max(faces, key=lambda f: (f.bbox[2]-f.bbox[0])*(f.bbox[3]-f.bbox[1]))
            all_embeddings.append(face.normed_embedding)
            all_names.append(person_name)
            count += 1

        print(f"  --> {count} faces encoded")

    print(f"\nTotal: {len(all_embeddings)} encodings")
    if len(all_embeddings) == 0:
        print("ERROR: No faces found. Add images to dataset/ first.")
        exit()

    with open(MODEL_PATH, "wb") as f:
        pickle.dump({
            "embeddings": np.array(all_embeddings),
            "names":      all_names
        }, f)

    print(f"Model saved -> {MODEL_PATH}")
    print("Done! Run:  python main.py")


# ── Entry point ──────────────────────────
if "--capture" in sys.argv:
    capture_photos()

train()