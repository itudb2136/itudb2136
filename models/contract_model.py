class ContractModel:
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

class ContractTable:
    pass