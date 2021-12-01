from datetime import datetime
from flask import g, request, Blueprint, render_template, redirect, url_for
from database import get_db
from models.player_image_model import PlayerImageModel
from models.transfer_model import TransferModel, TransferTable
from models.player_model import PlayerModel, PlayerTable
from models.player_main_characteristics_model import PlayerCharacteristicsModel
from models.player_skills_model import PlayerSkillsModel
from models.player_contract_model import PlayerContractModel
from models.club_model import ClubTable

player_bp = Blueprint('player_bp', __name__, url_prefix='/players')

@player_bp.route('/', methods=['GET'])
def show_all_players():
    pt = PlayerTable(get_db())
    ct = ClubTable(get_db())
    players = pt.get_all_players(limit=100)
    statistics = {"Average age": "",
                  "Max age": "",
                  "Min age": ""}
    return render_template("all_players.html", players=players, ct=ct, statistics=statistics)

@player_bp.route('/<player_id>', methods=['GET', 'POST'])
def show_player_by_id(player_id):
    pt = PlayerTable(get_db())
    player = pt.get_player_by_id(player_id)

    if request.method == 'GET':
        return render_template("player_by_id.html", player=player)
    else:
        # change player informations
        to_team = request.form['ToTeam']
        tt = TransferTable(get_db())
        transfer = TransferModel(player_id, player.contract.club, to_team, 1, 1, True)
        tt.add_transfer(transfer)
        return redirect(url_for("player_bp.show_all_players"))

@player_bp.route('/add_player', methods=['GET', 'POST'])
def add_new_player():
    pt = PlayerTable(get_db())
    if request.method == 'GET':
        max_id = pt.get_maximum_player_id()
        return render_template("add_player.html", max_id=max_id)
    else:
        player_id = request.form['playerId']
        name = request.form['name']
        age = request.form['age']
        nationality = request.form['nationality']
        int_reputation = request.form['int_reputation']
        position = request.form['position']
        height = request.form['height']
        weight = request.form['weight']
        overall = request.form['overall']
        potential = request.form['potential']

        characteristic = PlayerCharacteristicsModel(player_id, overall, potential, "Left", 1, 2, "High", "Medium")
        skills = PlayerSkillsModel(player_id, 0, 1, 2, 3, 4, 5, 6, 7)
        contract = PlayerContractModel(player_id, 1, 9, 9, None, '2025-09-20', '2025-09-20', 212, 8)
        image = PlayerImageModel(player_id, None)
        player = PlayerModel(player_id, name, age, nationality, int_reputation, position, height, weight, characteristic, skills, image, contract)

        pt.add_player(player)

        return "<p>Success</p>"