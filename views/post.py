import sqlite3
import json


def retrieve_post(pk):
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content
        FROM Posts p
        WHERE p.id = ?
        """,
            (pk,),
        )
        query_results = db_cursor.fetchone()

        # Serialize Python list to JSON encoded string
        serialized_post = json.dumps(dict(query_results))

    return serialized_post


def get_posts():

    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
                SELECT
                    p.id,
                    p.user_id,
                    u.first_name,
                    u.last_name,
                    u.username,
                    u.profile_image_url,
                    p.category_id,
                    c.label,
                    p.title,
                    p.publication_date,
                    p.image_url,
                    p.content,
                    p.approved
                FROM Posts p
                    JOIN Users u ON u.id = p.user_id
                    JOIN Categories c ON c.id = p.category_id
            """
        )
        query_results = db_cursor.fetchall()

        posts = []
        for row in query_results:
            user = {
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "username": row["username"],
                "profile_image_url": row["profile_image_url"],
            }
            category = {"label": row["label"]}
            post = {
                "id": row["id"],
                "user_id": row["user_id"],
                "user": user,
                "category_id": row["category_id"],
                "category": category,
                "title": row["title"],
                "publication_date": row["publication_date"],
                "image_url": row["image_url"],
                "content": row["content"],
                "approved": row["approved"],
            }
            posts.append(post)

        serialized_posts = json.dumps(posts)

        return serialized_posts
