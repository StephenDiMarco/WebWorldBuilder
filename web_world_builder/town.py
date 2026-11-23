from http import HTTPMethod
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from web_world_builder.utilities import capitalize_sentences
from web_world_builder.randomizers.town_randomizer import TownRandomizer

bp = Blueprint('town', __name__)

class Town:

    def __init__(self, name):
        self.town_constructor = TownRandomizer.get_instance()
        if not name:
            self.name = self.town_constructor.randomize()
        else:
            self.name = name

    def __str__(self):
        description = f"{self.name}"
        return capitalize_sentences(description)

@bp.route('/')
def index():
    return render_template('town/index.jinja', towns=[Town(None), Town(None)])
