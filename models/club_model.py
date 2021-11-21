class ClubModel:
    def __init__(self, id, club_name, is_taken):
        self.id = id
        self.club_name = club_name
        self.is_taken = is_taken

def create_clubs_models_from_tuple(players):
    res_models = []
    for p in players:
        model = ClubModel(p[1], p[0], p[2])
        res_models.append(model)

    if len(res_models) == 1:
        return res_models[0]
    return res_models

class ClubTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        # self.tablename = "clubs"
    
    def get_club_by_id(self, id):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM clubs WHERE id = %s", (id,))
            club = cursor.fetchall()

        return create_clubs_models_from_tuple(club) 

    def get_all_clubs(self, limit=None):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM clubs LIMIT %s", (limit, ))
            clubs = cursor.fetchall()

        return create_clubs_models_from_tuple(clubs) 