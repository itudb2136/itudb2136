
class User:
    def __init__(self, user_id, username, password, full_name, role, relevant_team_id, last_update, created_date, profile_photo):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.role = role
        self.relevant_team_id = relevant_team_id
        self.last_update = last_update
        self.created_date = created_date
        self.profile_photo = profile_photo