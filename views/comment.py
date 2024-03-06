import sqlite3
import json


def get_comments_by_post_id(url):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        if "_post_id" in url["query_params"]:
            db_cursor.execute(
                """
                    SELECT
                        c.id,
                        c.post_id,
                        p.id,
                        u.id AS user_id,
                        u.profile_image_url,
                        c.author_id,
                        c.content
                    FROM Comments c
                        JOIN Users u ON u.id = c.author_id
                        JOIN Posts p ON p.id = c.post_id
                    WHERE c.post_id = ?
        """,
                (url["query_params"]["_post_id"][0],),
            )
            query_results = db_cursor.fetchall()

            comments = []
            for row in query_results:
                post = {
                    "user_id": row["user_id"],
                    "profile_image_url": row["profile_image_url"],
                }
                comment = {
                    "id": row["id"],
                    "post": post,
                    "author_id": row["author_id"],
                    "content": row["content"],
                }
                comments.append(comment)

            return json.dumps(comments)


# id
# post_id
# ---- POST:
# ---- user_id
# ---- image_url
# author_id
# content
