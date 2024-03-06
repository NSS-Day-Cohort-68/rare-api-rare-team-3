import sqlite3
import json


def create_tag(tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO Tags (label)
            VALUES  (?)
            """,
            (tag["label"],),
        )

        new_tag_id = db_cursor.rowcount

    return True if new_tag_id > 0 else False
