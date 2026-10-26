import os
import requests
import random
import time

TOKEN = os.environ.get("8736595098:AAG9jyDUGGy3ZIqEDlvi0XZW83gnZtxe-L0")

MORNING_WISHES = [
    "☀️ Chào buổi sáng cả nhà! Chúc mọi người một ngày mới ngập tràn năng lượng và may mắn! 💪",
    "🌻 Một ngày mới bắt đầu rồi! Chúc bạn làm việc hiệu quả, tâm trạng vui vẻ!",
    "☕ Sáng rồi, uống ly nước/cà phê rồi bắt đầu ngày mới thôi! Chúc mọi người một ngày tuyệt vời!",
    "🚀 Chào buổi sáng! Hôm nay là một cơ hội mới để làm những điều tuyệt vời. Cố lên nhé!",
    "🌞 Nắng đã lên rồi, chúc bạn một buổi sáng tốt lành, một ngày làm việc suôn sẻ!"
]

def get_all_users():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    try:
        response = requests.get(url).json()
        user_ids = set()
        if response.get("ok"):
            for result in response["result"]:
                if "message" in result:
                    user_ids.add(result["message"]["chat"]["id"])
                elif "my_chat_member" in result:
                    user_ids.add(result["my_chat_member"]["chat"]["id"])
        return list(user_ids)
    except:
        return []

def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        requests.post(url, json=payload, timeout=10)
    except:
        pass

if __name__ == "__main__":
    if TOKEN:
        all_users = get_all_users()
        for uid in all_users:
            message = random.choice(MORNING_WISHES)
            send_telegram_message(uid, message)
            time.sleep(0.5)
