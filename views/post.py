import sqlite3
import json


def get_single_post(pk, url):
    # Open connection with the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Check to see if _expand query parameter exists
        if "_expand" in url.get("query_params"):
            # write SQL to get the post by id and join tables of both FKs
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
            WHERE p.id = ?
            """,
                (pk,),
            )
            query_results = db_cursor.fetchone()

            # Make nested object
            user = {
                "id": query_results["u_id"],
                "first_name": query_results["first_name"],
                "last_name": query_results["last_name"],
                "email": query_results["email"],
                "bio": query_results["bio"],
                "username": query_results["username"],
                "password": query_results["password"],
                "profile_image_url": query_results["profile_image_url"],
                "created_on": query_results["created_on"],
                "active": query_results["active"],
            }

            category = {
                "id": query_results["category_id"],
                "label": query_results["label"],
            }

            post = {
                "id": query_results["p_id"],
                "user_id": query_results["user_id"],
                "user": user,
                "category_id": query_results["category_id"],
                "category": category,
                "title": query_results["title"],
                "publication_date": query_results["publication_date"],
                "image_url": query_results["image_url"],
                "content": query_results["content"],
                "approved": query_results["approved"],
            }

            # Serialize Python list to JSON encoded string
            serialized_post = json.dumps(dict(post))

            return serialized_post

        else:
            # Write the SQL query to get single post by id
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
            WHERE p.id = ?
            """,
                (pk,),
            )

            query_results = db_cursor.fetchone()

            # Serialize Python list to JSON encoded string
            serialized_post = json.dumps(dict(query_results))

            return serialized_post
