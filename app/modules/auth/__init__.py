from flask import Blueprint

auth = Blueprint('signup', __name__, url_prefix="/auth", template_folder="templates")

from . import routes