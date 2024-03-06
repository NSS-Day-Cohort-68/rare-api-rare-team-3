import sqlite3
import json


# def create_comment(post, user):
#     with sqlite3.connect("./db.sqlite3") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute(
#             """
#                 INSERT INTO Comments
#                     (
#                         post_id,
#                         author_id,
#                         content
#                     )
#                         VALUES
#                     (
#                         ?,
#                         ?,
#                         ?
#                     )
#             """,
#             (
#                 post["id"],
#                 user["id"],
#                 "COMMENT DATA",
#             ),  # HOW DO I GET THIS??
#         )


# post_id
# author_id
# content


def get_comments_by_post_id(post_id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    c.id,
                    c.post_id,
                    p.id
                    u.user_id,
                    u.image_url,
                    c.author_id,
                    c.content
                FROM Comments c
                    JOIN Users u ON u.id = c.author_id
                    JOIN Posts p ON p.id = c.post_id
    """
        )


# id
# post_id
# ---- user_id
# ---- image_url
# author_id
# content
