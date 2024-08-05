# backend/mock_data.py

from datetime import datetime

from .models import People


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PEOPLE = {
    "Fairy": People(
        fname="Tooth",
        lname="Fairy",
        timestamp=get_timestamp()
    ),
    "Ruprecht": People(
        fname="Knecht",
        lname="Ruprecht",
        timestamp=get_timestamp()
    ),
    "Bunny": People(
        fname="Easter",
        lname="Bunny",
        timestamp=get_timestamp()
    ),
}
