import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from billing.db import get_db

from .service import AuthService
from .utils import validate_body
from .models.user.dto.user_create_dto import UserCreateDto


# create a Blueprint named 'auth'
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# create a route for the register view
auth_bp.route('/register', methods=['POST'])
def register():
    
    validate_body(request.json(), UserCreateDto())

    AuthService.register(request.json)

    return "OK"