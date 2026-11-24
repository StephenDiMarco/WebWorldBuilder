from http import HTTPMethod
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from web_world_builder.models.town import Town
from web_world_builder.sqlite_db_manager import db_session

bp = Blueprint('generator', __name__)

@bp.route('/')
def index():
    towns = Town.query.all()
    return render_template('generator/index.jinja', towns=towns)

@bp.route('/create')
def create():
    print("Generating new town")
    town = Town()
    town.randomize()
    db_session.add(town)
    db_session.commit()
    return redirect(url_for('generator.index'))

@bp.route('/<int:id>/edit', methods=('GET',))
def edit(id):
    print("Town editing to be added")
    return redirect(url_for('generator.index'))

@bp.route('/<int:id>/delete', methods=('GET',))
def delete(id):
    town = Town.query.get(id)
    if town is None:
        flash("Town does not exist.")
    else:
        db_session.delete(town)
        db_session.commit()

    return redirect(url_for('generator.index'))
