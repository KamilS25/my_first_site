from http.server import BaseHTTPRequestHandler, HTTPServer


NAME = ""
GROUP = ""

PAGE = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>my_first_site</title>
</head>
<body>
    <h1>my_first_site</h1>
    <p>Репозиторий для выполнения второй практики по предмету
    "Методы и средства сборки и развертывания цифрового продукта"</p>
    <p>{NAME} {GROUP}</p>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return

        content = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    print("Сайт запущен: http://localhost:8000")
    try:
        HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
