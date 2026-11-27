
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from http.cookies import SimpleCookie
import secrets
import re
import html

# ==========================================
# LOCAL CYBERSECURITY TRAINING APPLICATION
# ==========================================

HOST = "127.0.0.1"
PORT = 8000

# Fictional training accounts only.
# Passwords are plaintext for this simple lab.
USERS = {
    "admin": {
        "password": "Admin123!",
        "role": "admin"
    },
    "employee": {
        "password": "User123!",
        "role": "employee"
    }
}

# Temporary in-memory session storage.
SESSIONS = {}


class TrainingApp(BaseHTTPRequestHandler):

    def send_html(self, content, status=200, extra_headers=None):
        body = content.encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))

        if extra_headers:
            for name, value in extra_headers:
                self.send_header(name, value)

        self.end_headers()
        self.wfile.write(body)

    def get_current_user(self):
        cookie_header = self.headers.get("Cookie", "")

        cookie = SimpleCookie()
        cookie.load(cookie_header)

        if "session_id" not in cookie:
            return None

        session_id = cookie["session_id"].value
        return SESSIONS.get(session_id)

    def page(self, title, content):
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{html.escape(title)}</title>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f1f5f9;
                    margin: 50px;
                }}
                .container {{
                    background: white;
                    max-width: 500px;
                    margin: auto;
                    padding: 30px;
                    border-radius: 10px;
                }}
                input, button {{
                    width: 100%;
                    padding: 12px;
                    margin: 8px 0;
                    box-sizing: border-box;
                }}
                button {{
                    background: #2563eb;
                    color: white;
                    border: none;
                    cursor: pointer;
                }}
                a {{
                    color: #2563eb;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                {content}
            </div>
        </body>
        </html>
        """

    def do_GET(self):

        # Home / Login page
        if self.path == "/":

            content = """
                <h2>Mediroza Training Lab</h2>
                <p>Local cybersecurity practice application.</p>

                <form method="POST" action="/login">
                    <label>Username</label>
                    <input type="text" name="username"
                           maxlength="30" required>

                    <label>Password</label>
                    <input type="password" name="password"
                           maxlength="128" required>

                    <button type="submit">Login</button>
                </form>

                <hr>

                <p><b>Training accounts:</b></p>
                <p>Admin: admin / Admin123!</p>
                <p>Employee: employee / User123!</p>
            """

            self.send_html(self.page("Login", content))
            return

        # Dashboard
        if self.path == "/dashboard":

            user = self.get_current_user()

            if not user:
                self.send_html(
                    self.page("Unauthorized", "<h2>Please log in first.</h2>"),
                    401
                )
                return

            content = f"""
                <h2>Welcome to Dashboard</h2>
                <p>Role: {html.escape(user["role"])}</p>
                <p>You are successfully logged in.</p>

                <a href="/admin">Admin Area</a>
                <br><br>
                <a href="/logout">Logout</a>
            """

            self.send_html(self.page("Dashboard", content))
            return

        # Admin-only area
        if self.path == "/admin":

            user = self.get_current_user()

            if not user:
                self.send_html(
                    self.page("Unauthorized", "<h2>Please log in first.</h2>"),
                    401
                )
                return

            if user["role"] != "admin":
                self.send_html(
                    self.page(
                        "Forbidden",
                        "<h2>403 Forbidden</h2>"
                        "<p>You do not have administrator permission.</p>"
                    ),
                    403
                )
                return

            content = """
                <h2>Admin Training Area</h2>
                <p>Access granted to administrator.</p>
                <p>This is fictional training data.</p>
                <a href="/dashboard">Dashboard</a>
                <br><br>
                <a href="/logout">Logout</a>
            """

            self.send_html(self.page("Admin Area", content))
            return

        # Logout
        if self.path == "/logout":

            user = self.get_current_user()
            cookie_header = self.headers.get("Cookie", "")
            cookie = SimpleCookie()
            cookie.load(cookie_header)

            if "session_id" in cookie:
                session_id = cookie["session_id"].value
                SESSIONS.pop(session_id, None)

            headers = [
                (
                    "Set-Cookie",
                    "session_id=; Path=/; HttpOnly; SameSite=Strict; Max-Age=0"
                )
            ]

            self.send_html(
                self.page("Logged Out", "<h2>You have logged out.</h2><a href='/'>Login again</a>"),
                extra_headers=headers
            )
            return

        self.send_error(404, "Page not found")

    def do_POST(self):

        if self.path != "/login":
            self.send_error(404, "Page not found")
            return

        # Limit incoming request size.
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_error(400, "Invalid Content-Length")
            return

        if content_length <= 0 or content_length > 4096:
            self.send_error(400, "Invalid request size")
            return

        # Read submitted form data.
        raw_data = self.rfile.read(content_length)

        try:
            data = parse_qs(
                raw_data.decode("utf-8"),
                keep_blank_values=True
            )
        except UnicodeDecodeError:
            self.send_error(400, "Invalid request encoding")
            return

        username = data.get("username", [""])[0]
        password = data.get("password", [""])[0]

        # ==========================================
        # SERVER-SIDE INPUT VALIDATION
        # ==========================================

        if not username or not password:
            self.send_error(400, "Username and password are required")
            return

        if len(username) > 30:
            self.send_error(400, "Username is too long")
            return

        if not re.fullmatch(r"[A-Za-z0-9_-]+", username):
            self.send_error(400, "Invalid username format")
            return

        if len(password) > 128:
            self.send_error(400, "Password is too long")
            return

        # ==========================================
        # AUTHENTICATION
        # ==========================================

        if username not in USERS:
            self.send_error(401, "Invalid username or password")
            return

        if password != USERS[username]["password"]:
            self.send_error(401, "Invalid username or password")
            return

        # ==========================================
        # SESSION CREATION
        # ==========================================

        session_id = secrets.token_urlsafe(32)

        SESSIONS[session_id] = {
            "username": username,
            "role": USERS[username]["role"]
        }

        cookie_value = (
            f"session_id={session_id}; "
            "Path=/; HttpOnly; SameSite=Strict"
        )

        headers = [
            ("Set-Cookie", cookie_value)
        ]

        self.send_html(
            self.page(
                "Login Successful",
                """
                <h2>Login Successful!</h2>
                <p>Your session has been created.</p>
                <a href="/dashboard">Open Dashboard</a>
                """
            ),
            extra_headers=headers
        )


if __name__ == "__main__":

    server = HTTPServer((HOST, PORT), TrainingApp)

    print("=" * 45)
    print("Mediroza Local Training Application")
    print(f"Running at http://{HOST}:{PORT}")
    print("Press CTRL+C to stop the server.")
    print("=" * 45)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
