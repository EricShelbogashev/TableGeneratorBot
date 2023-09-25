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

# Initialize the current time
current_time = datetime.datetime.now()


def get_time_with_offset(offset_minutes):
    """Generate a time with a specified minutes offset."""
    time = current_time
    time += datetime.timedelta(minutes=offset_minutes)
    return f"{time.hour}:{time.minute:02}"


async def generate_table(update: Update):
    """Generate a table of subjects with a specified time offset."""
    global members

    # Get the offset from the message
    message_text = update.message.text.replace("/generate", "").strip()

    # Filter subjects based on the message
    message_parts = message_text.split()

    offset_minutes = [
        offset for offset in message_parts if "offset=" in offset
    ]

    if not offset_minutes:
        offset_minutes = 15
    else:
        offset_minutes = int(offset_minutes[-1].replace("offset=", ""))

    filtered_subjects = [
        member for member in members if not any(name in member for name in message_parts)
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


async def generate_command(update: Update, context: CallbackContext):
    """Handle the /generate command."""
    global current_time
    await generate_table(update)


def init_current_time():
    global current_time
    current_time = datetime.datetime(
        year=current_time.year,
        month=current_time.month,
        day=current_time.day,
        hour=int(os.environ['INIT_HOURS']),
        minute=int(os.environ['INIT_MINUTES'])
    )


def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    init_current_time()
    application = Application.builder().token(os.environ['BOT_TOKEN']).build()

    application.add_handler(CommandHandler("generate", generate_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
