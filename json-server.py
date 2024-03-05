import json
from http.server import HTTPServer
from handler import HandleRequests, status

from views import login_user, create_user
from views import get_single_post


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
                return self.response("", status.HTTP_500_SERVER_ERROR.value)

    def do_GET(self):
        """Handle GET requests from a client"""

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "posts":
            if url["pk"] != 0:
                response_body = get_single_post(url["pk"], url)
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

        else:
            return self.response(
                "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )


def main():
    host = ""
    port = 9999
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
