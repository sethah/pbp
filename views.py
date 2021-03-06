from flask import render_template, flash, redirect, session, url_for, request, Blueprint
from mysite import models
import data_functions as df
import team_info_functions as tf
from sqlalchemy import and_, or_
from datetime import datetime

current_year = df.get_year()

mod = Blueprint('main', __name__)

@mod.route('/')
@mod.route('/index')
def index():
    return redirect(url_for('teams.teams'))

@mod.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@mod.app_errorhandler(500)
def internal_error(error):
    #db.session.rollback()
    return render_template('500.html'), 500