from datetime import datetime
from flask import g, request, Blueprint, render_template, redirect, url_for
from database import get_db
from models.club_model import ClubTable
from models.player_image_model import PlayerImageModel
from models.transfer_model import TransferModel, TransferTable
from models.player_model import PlayerModel, PlayerTable
from models.player_main_characteristics_model import PlayerCharacteristicsModel
from models.player_skills_model import PlayerSkillsModel
from models.player_contract_model import PlayerContractModel

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    pt = PlayerTable(get_db())
    tt = TransferTable(get_db())
    ct = ClubTable(get_db())

    players = pt.get_all_players(limit=100)
    clubs = ct.get_all_clubs(limit=100)
    transfers = tt.get_all_transfers(limit=100)

    return render_template("home.html", players=players, clubs=clubs, transfers=transfers, ct=ct, pt=pt, tt=tt)