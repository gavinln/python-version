from datetime import datetime

import requests


def get_user(version: str = "1.3") -> dict:
    """Get random users"""
    url = f"https://randomuser.me/api/{version}/?results=1"
    response = requests.get(url)
    if response:
        return response.json()["results"][0]
    return {}


def get_age(user: dict) -> int | None:
    """Get the age of a user"""

    match user:
        case {"dob": {"age": int(age)}}:
            return age

        case {"dob": dob}:
            now = datetime.now()
            dob_date = datetime.strptime(dob, "%Y-%m-%d %H:%M:%S")
            return now.year - dob_date.year
    return None
