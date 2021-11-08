class PlayerImage:
    def __init__(self, player_id, image):
        self.player_id = player_id
        self.image = image

class PlayerImageTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        # self.tablename = "players_image"