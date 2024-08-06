# backend/mock_data.py

from datetime import datetime

from .models import Person


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


DEFAULT_PERSON = {
    "fname": "Tooth",
    "lname": "Fairy",
    "timestamp": "2022-10-08 09:15:10"
}

PEOPLE = {
    "Fairy": Person(
        fname="Tooth",
        lname="Fairy",
        timestamp=get_timestamp()
    ),
    "Ruprecht": Person(
        fname="Knecht",
        lname="Ruprecht",
        timestamp=get_timestamp()
    ),
    "Bunny": Person(
        fname="Easter",
        lname="Bunny",
        timestamp=get_timestamp()
    ),
}
