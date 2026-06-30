Rule-Based Chatbot

A simple Python-based Rule-Based Chatbot that responds to user input using predefined keyword/pattern matching and responses. This chatbot can handle greetings, name recognition, jokes, time/date queries, basic calculations, and more.

📌 Features


Greeting & Farewell Responses
User Name Recognition (remembers and recalls your name)
Current Time, Date, Month, Day & Year
Basic Math Calculations

Addition
Subtraction
Multiplication
Division



Jokes & Humor
Weather-related Replies
Small Talk (how are you, thanks, favorite color, age)
Help Menu with Example Commands
Interactive Command Line Interface


🛠️ Technologies Used


Python 3
Datetime Module
Random Module


📂 Project Structure

rule_based_chatbot/
│
├── Rule_based_chatbot.py   # Main chatbot source code
├── README.md               # Project documentation

▶️ How to Run


Make sure Python 3.10+ is installed.
Clone or download this repository.
Open a terminal in the project folder and run:


bashpython Rule_based_chatbot.py


Start chatting! Type help for example commands, or bye to exit.


💬 Example Conversation

Simple rule-based chat
Type help for examples. Type bye to exit.

You: hello
Bot: Hello. How can I help you?
You: my name is Alex
Bot: Nice to meet you, Alex.
You: what is my name
Bot: Your name is Alex.
You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!
You: calculate 12 * 7
Bot: The answer is 84.
You: bye
Bot: Goodbye.

📋 Example Commands

CommandDescriptionhi / hello / heyGreets the usermy name is <name>Sets your namewhat is my name / who am iRecalls your nametimeShows the current timedateShows the current datemonthShows the current monthwhat day is todayShows the current daycurrent yearShows the current yearcalculate <expression>Evaluates a math expression2 + 2Plain math expressions also worktell me a jokeReturns a random jokeweatherWeather-related replyhow are youSmall talkthanks / thank youAcknowledgementhelpShows example commandsbye / goodbye / exit / quitEnds the chat

⚙️ How It Works

The core logic lives in the get_reply(message, name) function, which:


Cleans and lowercases the incoming message.
Checks the message against a series of if conditions (rules) for known commands and keywords.
Returns a tuple of (reply, updated_name, should_exit).


The chat() function runs a loop that reads user input from the terminal, calls get_reply, prints the bot's response, and exits when should_exit is True.