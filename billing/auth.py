import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from .service import AuthService
from .utils import validate_body
from .models.user.dto.user_create_dto import UserCreateDto


authService = AuthService()


# create a Blueprint named 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')

# create a route for the register view
@bp.route('/register', methods=['POST'])
def register():
    
    validate_body(request.json, UserCreateDto(name="", password="", email=""))
    
    created_user = authService.register(request.json)

    return jsonify(created_user.__dict__()), 201