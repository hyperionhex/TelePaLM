import telebot
import google.generativeai as palm
from google.api_core import retry
from database import initialize_database, save_user_context, get_user_context

# Configure Palm API
palm.configure(api_key='PALM_API_KEY')

# Retry decorator for generating text
@retry.Retry()
def generate_text(*args, **kwargs):
    return palm.generate_text(*args, **kwargs)

# Initialize Telegram Bot
bot = telebot.TeleBot("TELE_BOT_KEY")

# Initialize the database
initialize_database()

# Handler for /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm a bot made using Google's Palm 2 API by Master @hemantelle. What can I do for you today?")

# ... (rest of the command handlers)

# Handler for user messages
@bot.message_handler(func=lambda message: True)
def solve_word_problem(message):
    # Extract the user's question
    question = message.text.strip()

    # Get the user's ID
    user_id = str(message.from_user.id)

    # Retrieve the user's context from the database
    context = get_user_context(user_id)

    # Combine the new question with the previous context (if any)
    prompt = """
    friendly conversation and helpful in everything Here's one:

    {}

    Your solution:
    """.format(context + " " + question)

    # Replace 'YOUR_MODEL_NAME' with your desired model name
    model_name = 'models/text-bison-001'

    # Generate completion
    completion = generate_text(
        model=model_name,
        prompt=prompt,
        candidate_count=8,
        temperature=0.0,
        max_output_tokens=800
    )

    # Save the user's context (including the previous response) to the database
    context = context + " " + question + " " + completion.result
    save_user_context(user_id, context)

    # Send the completion as a reply (exclude the context from the response)
    bot.reply_to(message, completion.result)

# ... (other code)

# Start the bot
bot.polling()
