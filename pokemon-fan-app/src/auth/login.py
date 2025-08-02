class LoginManager:
    def __init__(self):
        self.sessions = {}

    def login(self, username, password):
        # Here you would typically check the username and password against a database
        if username and password:  # Simplified check for demonstration
            self.sessions[username] = True
            return f"{username} logged in successfully."
        return "Invalid username or password."

    def logout(self, username):
        if username in self.sessions:
            del self.sessions[username]
            return f"{username} logged out successfully."
        return "User not logged in."