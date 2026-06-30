"""Simple rule-based chat in Python.

A rule-based chatbot is a chatbot that works using predefined rules created by developers.
 It does not understand language like AI chatbots.
   Instead, it follows specific instructions:
   IF user says "Hello" → THEN reply "Hi! How can I help you?"
"""

from datetime import datetime
import random

def get_reply(message: str, name: str | None):
    """Return the bot reply, the updated name, and whether to exit."""

    text = message.strip()
    lowered = text.lower()

    if not text:
        return "Please type something.", name, False
    if lowered in ("what is chatbot","chatbot"):
        return " A chatbot is a software program that interacts with users through text or voice. It is designed to answer questions, provide information, perform tasks, or assist users automatically.\nTypes of Chatbots\n1.Rule-based chatbots:These chatbots operate based on predefined rules and patterns.\n2.AI chatbots:These use Artificial Intelligence, Natural Language Processing (NLP), and Machine Learning to understand user input.\n3.Hybrid chatbots:A combination of rule-based and AI-based approaches.these provide the more flexible and accurate responses.",name,False
    

    if lowered in ("hi", "hello", "hey"):
        if name:
            return f"Hello, {name}. How can I help you?", name, False
        return "Hello. How can I help you?", name, False

    if lowered.startswith("my name is "):
        new_name = text[11:].strip().strip(".,!?")
        if new_name:
            name = new_name.title()
            return f"Nice to meet you, {name}.", name, False
        return "Please tell me your name after 'my name is'.", name, False

    if lowered in ("what is my name", "who am i"):
        if name:
            return f"Your name is {name}.", name, False
        return "I do not know your name yet. Say 'my name is ...'.", name, False

    if lowered in ("how are you"):
        return "I am fine. How are you?", name, False

    if lowered in ("help"):
        return  "Hello, my name is Alex,what do you want to know? ",  name, False
    if lowered in ("what can you do", "what is your name"):
        return "I am a chatbot. I can answer questions upto my knowledge, tell jokes, and perform calculations.", name, False

    if lowered in ("month"):
        month_name = datetime.now().strftime("%B")
        return f"The current month is {month_name}.", name, False
    #day
    if lowered in ("what day is today"):
        day_name = datetime.now().strftime("%A")
        return f"Today is {day_name}.", name, False
    #time
    if lowered in ("time"):
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The time is {current_time}.", name, False
    #date
    if lowered in ("date"):
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}.", name, False

    if lowered in ("thanks", "thank you", "thx"):
        return "You're welcome.", name, False

    if lowered in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye.", name, True
    # Weather
    if "weather" in lowered:
        return (
        "I cannot check live weather. Please open a weather website or app.",
        name,
        False,
        )

    # Calculator
    if lowered.startswith("calculate "):
        try:
           expression = text[10:].strip()
           result = eval(expression)
           return f"The answer is {result}.", name, False
        except:
           return "Invalid calculation.", name, False
    
    # Jokes
    if "joke" in lowered:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer get cold? It left its Windows open.",
            "Why do Python programmers wear glasses? Because they can't C."
        ]
    
        return random.choice(jokes), name, False

    # Age
    if "your age" in lowered or "how old are you" in lowered:
         return "I am a chatbot, so I do not have an age.", name, False

    # Favorite Color
    if "favorite color" in lowered:
        return "My favorite color is blue.", name, False

    # Current Year
    if "current year" in lowered or "what year is it" in lowered:
         year = datetime.now().year
         return f"The current year is {year}.", name, False
    try:
        allowed = "0123456789+-*/(). "

        if text and all(char in allowed for char in text):
           result = eval(text)
        return f"The answer is {result}.", name, False

    except:
     pass

    return "I do not understand yet. Type help for examples.", name, False


def chat() -> None:
    """Run the chat in the terminal."""

    name = None
    print("Simple rule-based chat")
    print("Type help for examples. Type bye to exit.\n")

    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye.")
            break

        reply, name, should_exit = get_reply(message, name)
        print(f"Bot: {reply}")

        if should_exit:
            break


if __name__ == "__main__":
    chat()
