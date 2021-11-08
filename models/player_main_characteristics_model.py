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
    pass