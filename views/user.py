import sqlite3
import json
from datetime import datetime


def login_user(user):
    """Checks for the user in the database

    Args:
        user (dict): Contains the username and password of the user trying to login

    Returns:
        json string: If the user was found will return valid boolean of True and the user's id as the token
        If the user was not found will return valid boolean False
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            select id, email
            from Users
            where email = ?
        """,
            (user["email"],),
        )

        user_from_db = db_cursor.fetchone()

        if user_from_db is not None:
            response = {"valid": True, "token": user_from_db["id"]}
        else:
            response = {"valid": False}

        return json.dumps(response)


def create_user(user):
    """Adds a user to the database when they register

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
                Insert into Users (first_name, last_name, email, bio, username, password, profile_image_url, created_on, active) values (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user["first_name"],
                user["last_name"],
                user["username"],
                user["email"],
                user.get("password", None),
                user.get("bio", None),
                user("profile_img_url", None),
                datetime.now(),
                user("active", 1),
            ),
        )

        id = db_cursor.lastrowid

        return json.dumps({"token": id, "valid": True})


def get_users():
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT 
                    u.id,
                    u.first_name,
                    u.last_name,
                    u.email,
                    u.bio,
                    u.username,
                    u.password,
                    u.profile_image_url,
                    u.created_on,
                    u.active
                FROM Users u
            """
        )
        query_results = db_cursor.fetchall()

        users = []
        for row in query_results:
            users.append(dict(row))

        return json.dumps(users)


def get_user_by_id(pk):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT 
                    u.id,
                    u.first_name,
                    u.last_name,
                    u.email,
                    u.bio,
                    u.username,
                    u.password,
                    u.profile_image_url,
                    u.created_on,
                    u.active
                FROM Users u
                WHERE u.id = ?
            """,
            (pk,),
        )
        query_results = db_cursor.fetchall()

        users = []
        for row in query_results:
            users.append(dict(row))

        return json.dumps(users)
