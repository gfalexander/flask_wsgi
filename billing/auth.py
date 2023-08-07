import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
    jsonify,
    current_app,
)
from werkzeug.security import check_password_hash, generate_password_hash

from .service import AuthService
from .utils import validate_body
from .models.user.dto.user_create_dto import UserCreateDto


authService = AuthService()


# create a Blueprint named 'auth'
bp = Blueprint("auth", __name__, url_prefix="/auth")

# create a route for the register view
@bp.route("/register", methods=["POST"])
def register():

    validate_body(request.json, UserCreateDto(name="", password="", email=""))

    created_user = authService.register(request.json)

    current_app.logger.debug("this is a DEBUG message")
    current_app.logger.info("this is an INFO message")
    current_app.logger.warning("this is a WARNING message")
    current_app.logger.error("this is an ERROR message")
    current_app.logger.critical("this is a CRITICAL message")

    return jsonify(created_user.__dict__()), 201
