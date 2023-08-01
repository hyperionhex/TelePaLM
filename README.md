# TelePaLM - Telegram Bot with Google's Palm 2 API

TelePaLM is a Telegram bot that uses Google's Palm 2 API to generate text completions for user messages. The bot maintains a context for each user and responds to their queries with relevant text generated using the Palm 2 model. The bot is designed to be friendly and helpful in providing text completions for various types of questions.

## How to Use

1. Get the API Keys:
   - Obtain the Palm API key from Google's Palm API service.
   - Create a Telegram bot and get the Telegram Bot API key.
   
2. Set Up the Database:
   - TelePaLM uses an SQLite database to store user contexts. Run the `initialize_database` function from `database.py` to create the necessary table.
   
3. Configuration:
   - Replace `PALM_API_KEY` in `TelePaLM.py` with your actual Palm API key.
   - Replace `TELEGRAM_BOT_KEY` in `TelePaLM.py` with your actual Telegram Bot API key.
   
4. Start the Bot:
   - Run `TelePaLM.py` to start the Telegram bot.

## How it Works

- Upon receiving a message, the bot checks if it is a command (e.g., `/start`) and responds accordingly.

- For user messages, the bot retrieves the user's previous context from the database.

- It combines the new user question with the previous context and generates a prompt for the Palm 2 model.

- The bot then uses the Palm 2 model to generate text completions for the prompt.

- The generated completion is saved as the user's new context in the database. 

- The bot sends the generated completion as a reply to the user's message.

## Note

- Make sure you have installed the required Python packages, including `telebot`, `google.generativeai`, and `google.api_core`.

- Ensure that the `user_history.db` file is present in the working directory for the SQLite database to work correctly.

Feel free to explore and modify the code to customize the behavior of the bot and the Palm 2 model.

Enjoy using TelePaLM! 🤖🌴
