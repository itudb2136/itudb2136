from .player_main_characteristics_model import PlayerCharacteristicsModel, PlayerCharacteristicsTable
from .player_skills_model import PlayerSkillsModel, PlayerSkillsTable
from .player_image_model import PlayerImageModel, PlayerImageTable
from .player_contract_model import PlayerContractModel, PlayerContractTable

class PlayerModel:
    def __init__(self, player_id, name, age, nationality, int_reputation, position, height, weight, characteristics:PlayerCharacteristicsModel, skills:PlayerSkillsModel, image:PlayerImageModel, contract:PlayerContractModel):
        self.player_id = player_id
        self.name = name
        self.age = age
        self.nationality = nationality
        self.int_reputation = int_reputation
        self.position = position
        self.height = height
        self.weight = weight
        self.characteristics = characteristics
        self.skills = skills
        self.image = image
        self.contract = contract

def create_player_models_from_tuple(players):
    res_models = []
    for p in players:
        characteristics = PlayerCharacteristicsModel(p[0], p[8], p[9], p[10], p[11], p[12], p[13], p[14])
        skills = PlayerSkillsModel(p[0], p[15], p[16], p[17], p[18], p[19], p[20], p[21], p[22])
        image = PlayerImageModel(p[0], p[23])
        contract = PlayerContractModel(p[0], p[24], p[25], p[26], p[27], p[28], p[29], p[30], p[31])
        
        model = PlayerModel(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], characteristics, skills, image, contract)
        res_models.append(model)

    if len(res_models) == 1:
        return res_models[0]
    return res_models

class PlayerTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        # self.tablename = "players"

    def get_player_by_id(self, player_id):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * \
                            FROM players \
                            INNER JOIN players_characteristics\
                                USING (id)\
                            INNER JOIN players_skills\
                                USING (id)\
                            INNER JOIN players_photo\
                                USING (id)\
                            INNER JOIN contract\
                                USING (id)\
                            WHERE id = %s",
                            (player_id,))
           
            player = cursor.fetchall()

        return create_player_models_from_tuple(player)

    def get_all_players(self, limit=None):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * \
                            FROM players \
                            INNER JOIN players_characteristics\
                                USING (id)\
                            INNER JOIN players_skills\
                                USING (id)\
                            INNER JOIN players_photo\
                                USING (id)\
                            INNER JOIN contract\
                                USING (id)\
                            LIMIT %s",
                            (limit,))
           
            player = cursor.fetchall()

        return create_player_models_from_tuple(player)

    def add_player(self, player:PlayerModel):
        with self.db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO players (id, name, age, nationality, international_reputation, position, height, weight)\
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (player.player_id, player.name, player.age, player.nationality, player.int_reputation, player.position, player.height, player.weight))

            pst = PlayerSkillsTable(self.db_connection)
            pst.add_skills(player.skills)

            pct = PlayerContractTable(self.db_connection)
            pct.add_contract(player.contract)

            pcharaceristict = PlayerCharacteristicsTable(self.db_connection)
            pcharaceristict.add_characteristics(player.characteristics)

            pit = PlayerImageTable(self.db_connection)
            pit.add_image(player.image)

            self.db_connection.commit()

    # while adding a new player, this function return all available player
    # ids and make enable to check whether the given id is already
    # in or not.
    def get_maximum_player_id(self):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT id FROM players ORDER BY id DESC")
            maximum_id = cursor.fetchone()

        return maximum_id[0]
