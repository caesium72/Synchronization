import re
import os
import time
import datetime
import emoji
import gspread
from dotenv import load_dotenv
from openai import OpenAI
from telethon import TelegramClient, events

# Load environment variables
load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
channel_id = int(os.getenv("CHANNEL_ID"))
sheet_id = os.getenv("GOOGLE_SHEET_ID")

# Telegram client setup
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# OpenAI client setup
client_ai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Google Sheets client setup
gc = gspread.service_account(filename='credentials.json')
sheet = gc.open_by_key(sheet_id).sheet1

# Regular expression to extract links
link_pattern = re.compile(r'(https?://\S+|www\.\S+)')

def extract_links(message):
    raw_links = re.findall(link_pattern, message)
    cleaned_links = []

    for link in raw_links:
        link = emoji.replace_emoji(link, replace='')
        if not link.startswith('http'):
            link = 'https://' + link
        cleaned_links.append(link.strip())

    return cleaned_links

def get_titles_from_links(links):
    try:
        prompt = f"Generate a short and descriptive title for each of the following links. Format: Title | Link\n\n{chr(10).join(links)}"
        response = client_ai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip().split("\n")
    except Exception as e:
        print("OpenAI Error:", e)
        return [f"Untitled | {link}" for link in links]

@client.on(events.NewMessage(chats=channel_id))
async def handler(event):
    message = event.message.message
    links = extract_links(message)

    if links:
        titled_links = get_titles_from_links(links)
        for entry in titled_links:
            try:
                title, link = entry.split(" | ", 1)
            except:
                title, link = "Untitled", entry
            sheet.append_row([
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                title.strip(),
                link.strip()
            ])
            print("✅ Logged:", title.strip(), "|", link.strip())
            time.sleep(1.2)

print("🤖 Bot is running...")
client.run_until_disconnected()
