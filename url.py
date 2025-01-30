import socket
import ssl


class URL:
    __scheme: str
    __host: str
    __path: str
    __port: int

    def __init__(self, url: str):
        self.__scheme, url = url.split("://", 1)
        assert self.__scheme in ["http", "https"]

        if self.__scheme == "https":
            self.__port = 443
        elif self.__scheme == "http":
            self.__port = 80

        if "/" not in url:
            url = url + "/"

        self.__host, url = url.split("/", 1)
        self.__path = "/" + url

        if ":" in self.__host:
            self.__host, port = self.__host.split(":", 1)
            self.__port = int(port)

    def request(self) -> str:
        s = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP
        )

        s.connect((self.__host, self.__port))

        if self.__scheme == "https":
            context = ssl.create_default_context()
            s = context.wrap_socket(s, server_hostname=self.__host)

        request = "GET {} HTTP/1.0\r\n".format(self.__path)
        request += "Host: {}\r\n".format(self.__host)
        request += "\r\n"
        s.send(request.encode("utf8"))

        response = s.makefile("r", encoding="utf8", newline="\r\n")
        statusline = response.readline()
        version, status, explanation = statusline.split(" ", 2)
        response_headers = {}

        if version == "HTTP/1.1":
            response_headers["connection"] = "close"
            response_headers["user-agent"] = "vini-serafini browser"

        while True:
            line = response.readline()
            if line == "\r\n":
                break

            header, value = line.split(":", 1)
            response_headers[header.casefold()] = value.strip()

        assert "transfer-encoding" not in response_headers
        assert "content-encoding" not in response_headers

        content = response.read()
        s.close()

        return content


def lex(body: str) -> None:
    text = ""
    in_tag = False
    for c in body:
        if c == "<":
            in_tag = True
        elif c == ">":
            in_tag = False
        elif not in_tag:
            text += c
    return text
