# backend/mock_data.py

from .models import Person


DEFAULT_PERSON = {
    "fname": "Tooth",
    "lname": "Fairy",
    "timestamp": "2022-10-08 09:15:10"
}

PEOPLE = {
    "Fairy": Person(
        fname="Tooth",
        lname="Fairy",
        timestamp="2022-10-08 10:15:10"
    ),
    "Ruprecht": Person(
        fname="Knecht",
        lname="Ruprecht",
        timestamp="2022-10-08 11:15:10"
    ),
    "Bunny": Person(
        fname="Easter",
        lname="Bunny",
        timestamp="2022-10-08 12:15:10"
    ),
}
