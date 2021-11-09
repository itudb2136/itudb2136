from datetime import datetime

class TransferModel:
    def __init__(self, player_id, from_team, to_team, transfer_fee, offered_wage, is_loan=False, offer_date=datetime.now(), positive_reviews=0, negative_reviews=0, is_accepted=False, transfer_id=None):
        self.transfer_id = transfer_id
        self.player_id = player_id
        self.from_team = from_team
        self.to_team = to_team
        self.transfer_fee = transfer_fee
        self.offered_wage = offered_wage
        self.is_loan = is_loan
        self.offer_date = offer_date
        self.positive_reviews = positive_reviews
        self.negative_reviews = negative_reviews
        self.is_accepted = is_accepted

def create_transfer_models_from_tuple(transfers):
    res_models = []
    for t in transfers:
        model = TransferModel(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10])
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

        return create_transfer_models_from_tuple(transfers) 

    def get_transfer_by_id(self, transfer_id):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM transfers WHERE transfer_id = %s", (transfer_id,))
            transfer = cursor.fetchone()
        
        return create_transfer_models_from_tuple(transfer)
        
    def add_transfer(self, new_transfer:TransferModel):
        with self.db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO transfers (player_id, from_team, to_team, transfer_fee, is_loan, offer_date, offered_wage)\
                            VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (new_transfer.player_id, new_transfer.from_team, new_transfer.to_team,
                            new_transfer.transfer_fee, new_transfer.is_loan, new_transfer.offer_date,
                            new_transfer.offered_wage,)
                        )
            self.db_connection.commit()

    def delete_transfer(self, transfer_id):
        with self.db_connection.cursor() as cursor:
            cursor.execute("DELETE FROM transfers WHERE transfer_id = %s", (transfer_id,))
            self.db_connection.commit()

    def update_transfer(self, transfer_id, updated_transfer:TransferModel):
        player_id = updated_transfer.transfer_id
        to_team = updated_transfer.to_team
        transfer_fee = updated_transfer.transfer_fee
        is_loan = updated_transfer.is_loan
        offer_date = updated_transfer.offer_date
        is_accepted = updated_transfer.is_accepted
        offered_wage = updated_transfer.offered_wage

        with self.db_connection.cursor() as cursor:
            cursor.execute("UPDATE transfers\
                            SET player_id = %s,\
                                to_team = %s,\
                                transfer_fee = %s,\
                                is_loan = %s,\
                                offer_date = %s,\
                                is_accepted = %s,\
                                offered_wage = %s\
                            WHERE transfer_id = %s",
                            (player_id, to_team, transfer_fee, is_loan, offer_date, is_accepted, offered_wage, transfer_id,))
            self.db_connection.commit()
