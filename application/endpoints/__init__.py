# -*- coding: utf-8 -*-
"""
    This module contain a Blueprint for the API Endpoints
"""
from flask import Blueprint


api = Blueprint('api', __name__)


@api.before_request
def before_request():
    pass


@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

