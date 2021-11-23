from flask import g, request, Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from controllers.forms.LoginForm import LoginForm
from models.club_model import ClubTable
from database import get_db
from models.user_model import User, UserTable
from app import login_manager

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    ct = ClubTable(get_db())
    teams = ct.get_all_clubs()

    form = LoginForm()
    if form.validate_on_submit():
        # validate user, if not flash and redirect there
        ut = UserTable(get_db())
        if ut.get_id_by_username(form.username.data) is None:
            user = User(form.username.data, form.password.data, form.fullname.data, form.role.data)
            ut.add_user(user)
            login_user(user)
            return redirect('/players')
        else:
            flash("The username is in use.", category="error")
            render_template('signup.html', form=form, teams=teams)

    return render_template('signup.html', form=form, teams=teams)

@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    pass


@auth_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('home_bp.home'))

@login_manager.user_loader
def load_user(username):
    """Check if user is logged-in on every page load."""
    if username is not None:
        ut = UserTable(get_db())
        return ut.get_user_by_username(username)
    return None

