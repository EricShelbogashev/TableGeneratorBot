import datetime
import os
import random

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackContext

# List of members
members_file = "members.txt"  # Replace with the actual file path

# Read the list from the file
with open(members_file, "r", encoding="utf-8") as file:
    members = [line.strip() for line in file]

# Print the list

# Initialize the current time
current_time = datetime.datetime(2023, 8, 25, 16, 5)


def get_time_with_offset(offset_minutes):
    """Generate a time with a specified minutes offset."""
    global current_time
    current_time += datetime.timedelta(minutes=offset_minutes)
    time = current_time.time()
    return f"{time.hour}:{time.minute:02}"


async def generate_table(update: Update, context: CallbackContext):
    """Generate a table of subjects with a specified time offset."""
    global members

    # Get the offset from the message
    message_text = update.message.text.replace("/generate", "").strip()
    offset_minutes = int(message_text) if message_text.isdigit() else 0

    # Filter subjects based on the message
    message_parts = message_text.split()
    filtered_subjects = [
        subject for subject in members if not any(name in subject for name in message_parts)
    ]

    # Shuffle the filtered subjects
    random.shuffle(filtered_subjects)

    # Generate the table
    table = "\n".join(
        f"{i + 1}. {subject}  {get_time_with_offset(i * offset_minutes)}" for i, subject in
        enumerate(filtered_subjects)
    )

    # Send the table to the user
    await update.message.reply_text(f"Список сдачи:\n{table}")


async def generate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /generate command."""
    global current_time
    current_time = datetime.datetime(2023, 8, 25, 16, 5)
    await generate_table(update, context)


def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(os.environ['BOT_TOKEN']).build()

    application.add_handler(CommandHandler("generate", generate_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
