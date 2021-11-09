class PlayerImageModel:
    def __init__(self, player_id, image):
        self.player_id = player_id
        self.image = image

class PlayerImageTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        # self.tablename = "players_image"

    def add_image(self, i:PlayerImageModel):
        with self.db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO players_image (id, image)\
                            VALUES (%s, %s)",
                            (i.player_id, i.image))