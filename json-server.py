import json
from http.server import HTTPServer
from handler import HandleRequests, status

from views import login_user, create_user


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


def main():
    host = ""
    port = 9999
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
