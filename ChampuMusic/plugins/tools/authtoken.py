import asyncio
import os
import time
import glob
import random
import browser_cookie3
from pyrogram import filters
from yt_dlp import YoutubeDL
from ChampuMusic import app
from ChampuMusic.misc import SUDOERS

def extract_cookies():
    try:
        cj = browser_cookie3.chrome(domain_name="youtube.com")
        cookie_file = "cookies/cookies.txt"
        with open(cookie_file, "w") as f:
            for cookie in cj:
                f.write(f"{cookie.name}\t{cookie.value}\n")
        return True
    except Exception as e:
        return str(e)

def play_video():
    video_url = "https://www.youtube.com/watch?v=LLF3GMfNEYU"
    os.system(f"start {video_url}")
    time.sleep(random.randint(10, 15))

@app.on_message(filters.command("cookies") & SUDOERS)
async def generate_cookies(client, message):
    status_msg = await message.reply_text("🔄 Generating cookies, please wait...")
    
    try:
        play_video()
        extract_status = extract_cookies()
        
        if extract_status is True:
            await status_msg.edit_text("✅ Successfully extracted and saved cookies.")
            await client.send_message("log_group", "✅ Successfully generated new cookies!")
        else:
            await status_msg.edit_text(f"❌ Failed to extract cookies: {extract_status}")
    except Exception as e:
        await status_msg.edit_text(f"❌ Error: {str(e)}")
