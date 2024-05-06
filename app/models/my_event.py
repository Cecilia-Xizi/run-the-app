from pprint import pprint

from app.db import BaseModel

class Event(BaseModel):

    SHEET_NAME = "my_events"

    COLUMNS = ["user_email", "product_id", "product_name", "product_price"]

    SEEDS = []


if __name__ == "__main__":

    my_events = Event.all()
    print("FOUND", len(my_events), "My EVENTS")
    for event in my_events:
        pprint(dict(event))
