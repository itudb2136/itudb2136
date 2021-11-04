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