class PlayerCharacteristicsModel:
    def __init__(self, player_id, overall, potential, preferred_foot, weak_foot_skill, skill_moves, attack_work_rate, defence_work_rate):
        self.player_id = player_id
        self.overall = overall
        self.potential = potential
        self.preferred_foot = preferred_foot
        self.weak_foot_skill = weak_foot_skill
        self.skill_moves = skill_moves
        self.attack_work_rate = attack_work_rate
        self.defence_work_rate = defence_work_rate

class PlayerCharacteristicsTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        # self.tablename = "players_characteristics"

    def add_characteristics(self, c:PlayerCharacteristicsModel):
        with self.db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO players_characteristics (id, overall, potential, preferred_foot, weak_foot_skill, skill_moves, attack_work_rate, defence_work_rate)\
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (c.player_id, c.overall, c.potential, c.preferred_foot, c.weak_foot_skill, c.skill_moves, c.attack_work_rate, c.defence_work_rate))
            self.db_connection.commit()