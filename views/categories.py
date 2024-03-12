import sqlite3
import json


def get_categories():

    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            c.id,
            c.label
        FROM Categories c
        """
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        categories = []
        for row in query_results:
            categories.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_categories = json.dumps(categories)

    return serialized_categories


def create_category(category_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO Categories (label)
            VALUES  (?)
            """,
            (category_data["label"],),
        )

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False


def delete_category(pk):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                DELETE FROM Categories WHERE id = ?
            """,
            (pk,),
        )
        return True if db_cursor.rowcount > 0 else False
