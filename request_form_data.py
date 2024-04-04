import requests
from decouple import config


form_id = config("KWESFORMS_ID", cast=str, default='5762')
api_key = config("KWESFORMS_API_KEY", cast=str, default=None)


def get_submissions():
    endpoint = f"https://kwes.io/api/v1/forms/{form_id}/submissions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    r = requests.get(endpoint, headers=headers)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    print("Getting data")
    data = get_submissions()
    print(data)