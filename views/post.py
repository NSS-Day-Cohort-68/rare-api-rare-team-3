import sqlite3
import json


def create_post(post):
    """Adds a post to the database when user posts

    Args:
        user (dictionary): The dictionary passed to the register post request

    Returns:
        json string: Contains the token of the newly created user
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                Insert into Posts (user_id, category_id, title, publication_date, image_url, content, approved) values (?, ?, ?, ?, ?, ?, 1)
            """,
            (
                post["user_id"],
                post["category_id"],
                post["title"],
                post["publication_date"],
                post["image_url"],
                post["content"],
            ),
        )

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False


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


def get_posts_by_user(pk, url):
    # Open connection with the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Check to see if _expand query parameter exists
        if "_expand" in url.get("query_params"):
            # write SQL to get the posts by user id and join tables of both FKs
            db_cursor.execute(
                """
            SELECT
                p.id AS p_id,
                p.user_id, 
                p.category_id, 
                p.title, 
                p.publication_date, 
                p.image_url, 
                p.content, 
                p.approved,
                u.id AS u_id,
                u.first_name,
                u.last_name,
                u.email,
                u.bio,
                u.username,
                u.password,
                u.profile_image_url,
                u.created_on,
                u.active,
                c.id AS cat_id,
                c.label
            FROM Posts p
            JOIN Users u
                ON u.id = p.user_id
            JOIN Categories c
                ON c.id = p.category_id
            WHERE p.user_id = ?
            """,
                (pk,),
            )
            query_results = db_cursor.fetchall()

            # Initialize an empty list and then add each dictionary to it
            posts = []

            for row in query_results:
                user = {
                    "id": row["u_id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "email": row["email"],
                    "bio": row["bio"],
                    "username": row["username"],
                    "password": row["password"],
                    "profile_image_url": row["profile_image_url"],
                    "created_on": row["created_on"],
                    "active": row["active"],
                }

                category = {
                    "id": row["category_id"],
                    "label": row["label"],
                }

                post = {
                    "id": row["p_id"],
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

            # Serialize Python list to JSON encoded string
            serialized_posts = json.dumps(posts)

            return serialized_posts

        else:
            # Write the SQL query to get posts by user id
            db_cursor.execute(
                """
            SELECT
                p.id,
                p.user_id, 
                p.category_id, 
                p.title, 
                p.publication_date, 
                p.image_url, 
                p.content, 
                p.approved
            FROM Posts p
            WHERE p.user_id = ?
            """,
                (pk,),
            )

            query_results = db_cursor.fetchall()

            # Initialize an empty list and then add each dictionary to it
            posts = []

            for row in query_results:
                posts.append(dict(row))

            # Serialize Python list to JSON encoded string
            serialized_posts = json.dumps(posts)

            return serialized_posts
