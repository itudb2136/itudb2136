from flask import g, request, Blueprint, render_template
from database import get_db
from models.transfer_model import TransferModel, TransferTable

transfer_bp = Blueprint('transfer_bp', __name__, url_prefix="/transfers")

@transfer_bp.route('/all_transfers', methods=['GET'])
def show_all_transfers():
    tt = TransferTable(get_db())
    transfers = tt.get_all_transfers()
    return render_template("test.html", transfers=transfers)
