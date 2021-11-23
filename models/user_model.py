from flask_login import UserMixin
from datetime import date, datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, username, password, full_name, role, relevant_team_id=None, last_update=None, created_date=datetime.today(), profile_photo=None, user_id=None):
        self.username = username
        self.password = generate_password_hash(password, method="sha256")
        self.full_name = full_name
        self.role = role
        self.relevant_team_id = relevant_team_id
        self.last_update = last_update
        self.created_date = created_date
        self.profile_photo = profile_photo
        self.user_id = user_id

    def get_id(self):
        return self.username

def create_user_from_tuple(user_tuple):
    if user_tuple is not None:
        return User(user_tuple[1], user_tuple[2], user_tuple[3], user_tuple[4], user_tuple[5], user_tuple[6], user_tuple[7], user_tuple[8], user_tuple[0])
    return None
    
class UserTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_user(self, user:User):
        with self.db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (username, password, full_name, role, relevant_team_id, last_update, created_date, profile_photo)\
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (user.username, user.password, user.full_name, user.role, user.relevant_team_id, user.last_update, user.created_date, user.profile_photo))

            self.db_connection.commit()

    def get_user_by_username(self, username):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
        
        return create_user_from_tuple(user)

    def get_user_by_id(self, id):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
            user = cursor.fetchone()
        
        return create_user_from_tuple(user)

    def get_id_by_username(self, username):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
            user_id = cursor.fetchone()
        
        return None if user_id is None else user_id[0]