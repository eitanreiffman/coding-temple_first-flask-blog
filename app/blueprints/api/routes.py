from flask import request
from . import api
from .auth import basic_auth, token_auth
from app.models import Post, User

@api.route('/token')
@basic_auth.login_required
def index():
    user = basic_auth.current_user()
    token = user.get_token()
    return {'token': token, 'token_expiration': user.token_expiration}

@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return [p.to_dict() for p in posts]

@api.route('/posts/<int:post_id>')
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return post.to_dict()

@api.route('/posts', methods=['POST'])
@token_auth.login_required
def create_post():
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    data = request.json
    for field in ['title', 'body']:
        if field not in data:
            return {'error': f'{field} must be in request body'}, 400
        
    title = data.get('title')
    body = data.get('body')

    user = token_auth.current_user()

    new_post = Post(title=title, body=body, user_id=user.id)
    return new_post.to_dict(), 201

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return [u.to_dict() for u in users]

@api.route('/users/<int:user_id>')
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user.to_dict()

@api.route('/users', methods=['POST'])
def create_user():
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    data = request.json
    for field in ['email', 'username', 'password']:
        if field not in data:
            return {'error': f'{field} must be in request body'}, 400
        
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    new_user = User(email=email, username=username, password=password)
    return new_user.to_dict(), 201

