from datetime import datetime

class TransferModel:
    def __init__(self, transfer_id, player_id, from_team, to_team, transfer_fee, is_loan=False, offer_date=datetime.now(), positive_reviews=0, negative_reviews=0, is_accepted=False):
        self.transfer_id = transfer_id
        self.player_id = player_id
        self.from_team = from_team
        self.to_team = to_team
        self.transfer_fee = transfer_fee
        self.is_loan = is_loan
        self.offer_date = offer_date
        self.positive_reviews = positive_reviews
        self.negative_reviews = negative_reviews
        self.is_accepted = is_accepted

def create_models_from_tuple(transfers):
    res_models = []
    for t in transfers:
        model = TransferModel(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9])
        res_models.append(model)
    return res_models

class TransferTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        # self.tablename = "transfers"

    def get_all_transfers(self, limit=None):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM transfers ORDER BY offer_date DESC LIMIT %s", (limit,))
            transfers = cursor.fetchall()

        return create_models_from_tuple(transfers) 

    def get_transfer_by_id(self, transfer_id):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM transfers WHERE transfer_id = %s", (transfer_id,))
            transfer = cursor.fetchone()
        
        return create_models_from_tuple(transfer)
        
    def add_transfer(self, new_transfer:TransferModel):
        with self.db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO transfers (player_id, from_team, to_team, transfer_fee, is_loan, offer_date)\
                            VALUES(?, ?, ?, ?, ?, ?)",
                            new_transfer.player_id, new_transfer.from_team, new_transfer.to_team,
                            new_transfer.transfer_fee, new_transfer.is_loan, new_transfer.offer_date)

    def delete_transfer(self, transfer_id):
        pass

    def update_transfer(self, transfer_id):
        pass