class PlayerSkillsModel:
    def __init__(self, player_id, finishing, short_passing, dribbling, ball_control, acceleration, sprint_speed, jumping, stamina):
        self.player_id = player_id
        self.finishing = finishing
        self.short_passing = short_passing
        self.dribbling = dribbling
        self.ball_control = ball_control
        self.acceleration = acceleration
        self.sprint_speed = sprint_speed
        self.jumping = jumping
        self.stamina = stamina

class PlayerSkillsTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        # self.tablename = "players_skills"

    def add_skills(self, s:PlayerSkillsModel):
        with self.db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO players_skills (id, finishing, short_passing, dribbling, ball_control, acceleration, sprint_speed, jumping, stamina)\
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (s.player_id, s.finishing, s.short_passing, s.dribbling, s.ball_control, s.acceleration, s.sprint_speed, s.jumping, s.stamina))
            self.db_connection.commit()   