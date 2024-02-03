class User:
    id = None
    username = ''
    email = ''
    hashed_password = ''

    def __init__(self, username: str, email: str, hashed_password: str, id: int = None):
        self.id = id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
