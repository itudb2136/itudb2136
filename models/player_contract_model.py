class PlayerContractModel:
    def __init__(self, player_id, club, value, wage, loaned_from, contract_valid_until, joined, release_clause, jersey_number):
        self.player_id = player_id
        self.club = club
        self.value = value
        self.wage = wage
        self.loaned_from = loaned_from
        self.contract_valid_until = contract_valid_until
        self.joined = joined
        self.release_clause = release_clause
        self.jersey_number = jersey_number

def create_contract_models_from_tuple(contracts):
    res_models = []
    for c in contracts:
        model = PlayerContractModel(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8])
        res_models.append(model)
    
    if len(res_models) == 1:
        return res_models[0];
    return res_models

class PlayerContractTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        # self.tablename = "contract"

    def get_contract_by_player_id(self, player_id):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM contract WHERE id = %s", (player_id,))
            contract = cursor.fetchall()

        return create_contract_models_from_tuple(contract)

    def get_all_contract(self, limit=None):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM contract WHERE")
            contract = cursor.fetchall()

        return create_contract_models_from_tuple(contract)

    def add_contract(self, c:PlayerContractModel):
        with self.db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO contract (id, club, value, wage, loaned_from, contract_valid_until, joined, release_clause, jersey_number)\
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (c.player_id, c.club, c.value, c.wage, c.loaned_from, c.contract_valid_until, c.joined, c.release_clause, c.jersey_number))
            self.db_connection.commit()