# Eventee EventBuddy Bot 🤖  

Eventee EventBuddy is a **Telegram bot** designed to provide event updates in group chats.  
It automatically starts when deployed and responds to user commands.  

## Features 🚀  
✅ **/start** - Introduces the bot  
✅ **/help** - Displays available commands  
✅ **/link unique_code** - Links a group to EventBuddy for event updates  

## Installation & Setup 🛠️  

## 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/eventee_eventBuddy_bot.git
cd eventee_eventBuddy_bot
```

## 2️⃣ Create & Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

## 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

## 4️⃣ Set Up Environment Variables
Create a .env file in the root directory and add:

```
BOT_ACCESS_TOKEN=your_telegram_bot_token
BOT_USERNAME=your_bot_username
```

## 5️⃣ Run the Bot
```
python bot.py
```

## Running with Streamlit 🖥️

To test and visualize bot functionality, create an app.py file:
import streamlit as st
```
st.title("Eventee EventBuddy Bot")
st.write("✅ The bot is running successfully!")
```

Then, run:
```
streamlit run app.py
Dependencies 📦
```

## Pre Requesties  
```
✅ **anyio==4.8.0** 
✅ **certifi==2025.1.31** 
✅ **h11==0.14.0** 
✅ **httpcore==1.0.7** 
✅ **httpx==0.28.1** 
✅ **idna==3.10** 
✅ **python-dotenv==1.0.1** 
✅ **python-telegram-bot==21.10**  
✅ **sniffio==1.3.1** 
✅ **typing_extensions==4.12.2** 
✅ **nest-asyncio** 
```
### You can deploy this bot on:
Heroku
Railway.app
Render

Contributing 🤝


### License 📝
This project is licensed under the MIT License.
