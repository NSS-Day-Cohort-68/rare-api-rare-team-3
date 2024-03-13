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


def delete_tag(pk):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                DELETE FROM Tags WHERE id = ?
            """,
            (pk,),
        )
        return True if db_cursor.rowcount > 0 else False


def edit_tag(pk, tag_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                UPDATE Tags
                    SET
                        label = ?
                WHERE id = ?
            """,
            (
                tag_data["label"],
                pk,
            ),
        )

        return True if db_cursor.rowcount > 0 else False


def get_tags_by_post(postId):
    # Open connection with the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get postTags by post id
        db_cursor.execute(
            """
            SELECT
                pt.id,
                pt.post_id,
                pt.tag_id,
                t.label
            FROM PostTags pt
            JOIN Tags t ON pt.tag_id = t.id
            WHERE pt.post_id = ?
            """,
            (postId,),
        )

        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        postTags = []

        for row in query_results:

            tag = {"label": row["label"]}

            post_tag = {
                "id": row["id"],
                "post_id": row["post_id"],
                "tag_id": row["tag_id"],
                "tag": tag,
            }

            postTags.append(post_tag)

        # Serialize Python list to JSON encoded string
        serialized_posts = json.dumps(postTags)

        return serialized_posts
