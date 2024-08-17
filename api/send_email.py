import requests

from environs import Env
env = Env()
env.read_env()
def send_simple_message(to_email, subject, text):
    try:
        response = requests.post(
            "https://api.mailgun.net/v3/sandboxa9db5656948c4eb0b278f08db69ebe61.mailgun.org/messages",
            auth=("api","efa7666b7af23a1fb654bbadd576f165-911539ec-9eb5faaf" ),
            data={"from": "Excited User <mailgun@sandboxa9db5656948c4eb0b278f08db69ebe61.mailgun.org>",
                  "to": [to_email, "YOU@sandboxa9db5656948c4eb0b278f08db69ebe61.mailgun.org"],
                  "subject": subject,
                  "text": text}
        )
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response
    except requests.RequestException as e:
        # Log the exception if needed
        print(f"An error occurred: {e}")
        return None