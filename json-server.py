import json
from http.server import HTTPServer
from handler import HandleRequests, status

from views import login_user, create_user, get_users
from views import get_categories, create_category
from views import (
    get_posts,
    get_posts_by_user,
    retrieve_post,
    delete_post,
    create_post,
    edit_post,
)
from views import get_comments_by_post_id, create_comment
from views import create_tag


class JSONServer(HandleRequests):

    def do_POST(self):
        """Handle POST requests from a client"""
        url = self.parse_url(self.path)
        pk = url["pk"]

        content_length = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_length)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "users":
            if pk == 0:
                successfully_posted = create_user(request_body)
                if successfully_posted:
                    return self.response("", status.HTTP_201_SUCCESS_CREATED.value)

                else:
                    return self.response(
                        "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
                    )

        elif url["requested_resource"] == "categories":
            if pk == 0:
                successfully_posted = create_category(request_body)
                if successfully_posted:
                    return self.response("", status.HTTP_201_SUCCESS_CREATED.value)

                else:
                    return self.response(
                        "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
                    )

        elif url["requested_resource"] == "tags":
            if pk == 0:
                try:
                    successfully_posted = create_tag(request_body)
                    if successfully_posted:
                        return self.response("", status.HTTP_201_SUCCESS_CREATED.value)

                except KeyError:
                    return self.response(
                        "Error creating tag: Invalid data format. Need a label",
                        status.HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA.value,
                    )
        elif url["requested_resource"] == "posts":
            if pk == 0:
                successfully_posted = create_post(request_body)
                if successfully_posted:
                    return self.response("", status.HTTP_201_SUCCESS_CREATED.value)

                else:
                    return self.response(
                        "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
                    )

        elif url["requested_resource"] == "comments":
            if pk == 0:
                try:
                    successfully_posted = create_comment(request_body)
                    if successfully_posted:
                        return self.response("", status.HTTP_201_SUCCESS_CREATED.value)

                except KeyError:
                    return self.response(
                        "Error creating comment: Need comment content",
                        status.HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA.value,
                    )

        else:
            return self.response(
                "Requested resource not found",
                status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
            )

    def do_GET(self):
        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "posts":
            if "user_id" in url.get("query_params"):
                user_id = int(url["query_params"]["user_id"][0])
                posts_by_user = get_posts_by_user(user_id, url)
                return self.response(posts_by_user, status.HTTP_200_SUCCESS.value)

            elif url["pk"] != 0:
                response_body = retrieve_post(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            response_body = get_posts()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "categories":
            response_body = get_categories()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "comments":
            response_body = get_comments_by_post_id(url)
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "users":
            response_body = get_users()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        else:
            return self.response(
                "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )

    def do_DELETE(self):
        """Handle DELETE requests from a client"""

        url = self.parse_url(self.path)
        pk = url["pk"]

        if url["requested_resource"] == "posts":
            if pk != 0:
                successfully_deleted = delete_post(pk)
                if successfully_deleted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

                return self.response(
                    "Requested resource not found",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )

    def do_PUT(self):
        """Handle PUT requests from a client"""

        # Parse the URL and get the primary key
        url = self.parse_url(self.path)
        pk = url["pk"]

        # Get the request body JSON for the new data
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "posts":
            if pk != 0:
                successfully_updated = edit_post(pk, request_body)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
        return self.response(
            "Requested resource not found",
            status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
        )


def main():
    host = ""
    port = 9999
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
