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
                        c.author_id,
                        u.id AS user_id,
                        u.first_name,
                        u.last_name,
                        u.username,
                        c.content,
                        c.creation_datetime
                    FROM Comments c
                        JOIN Users u ON user_id = c.author_id
                    WHERE c.post_id = ?
                """,
                (url["query_params"]["_post_id"][0],),
            )
            query_results = db_cursor.fetchall()

            comments = []
            for row in query_results:
                author = {
                    "user_id": row["user_id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "username": row["username"],
                }
                comment = {
                    "id": row["id"],
                    "post_id": row["post_id"],
                    "author_id": row["author_id"],
                    "author": author,
                    "content": row["content"],
                    "creation_datetime": row["creation_datetime"]
                }
                comments.append(comment)

            return json.dumps(comments)


def create_comment(comment_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                INSERT INTO Comments
                    (
                        post_id,
                        author_id,
                        content
                    )
                        VALUES
                    (
                        ?,
                        ?,
                        ?
                    )
            """,
            (
                comment_data["post_id"],
                comment_data["author_id"],
                comment_data["content"],
            ),
        )

        return True if db_cursor.rowcount > 0 else False
