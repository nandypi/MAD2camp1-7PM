from json import dumps
from httplib2 import Http
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Copy the webhook URL from the Chat space where the webhook is registered.
# The values for SPACE_ID, KEY, and TOKEN are set by Chat, and are included
# when you copy the webhook URL.
url = os.getenv("GSPACE_WEBHOOK_URL")

def main(msg="Hello bootcamp students! Greetings from the Python script!"):
    """Google Chat incoming webhook quickstart."""
    if not url:
        raise ValueError("GSPACE_WEBHOOK_URL environment variable is not set.")
    
    app_message = {
        "text": msg
    }
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )
    print(response)


if __name__ == "__main__":
    main(msg="Thanks for joining the bootcamp! Looking forward to seeing you completing the project and submitting it on time. All the best!")