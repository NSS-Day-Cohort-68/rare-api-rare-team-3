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


def add_tags_to_post(post_tags):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        for tag in post_tags:
            db_cursor.execute(
                """
                INSERT INTO PostTags (post_id, tag_id)
                VALUES  (?, ?)
                """,
                (tag["post_id"], tag["tag_id"]),
            )

        # Get the count of inserted rows
        new_tag_count = db_cursor.rowcount

    return True if new_tag_count > 0 else False


def get_tags():
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT 
                    t.id,
                    t.label
                FROM Tags t
            """
        )
        query_results = db_cursor.fetchall()

        tags = []
        for row in query_results:
            tags.append(dict(row))

        return json.dumps(tags)
