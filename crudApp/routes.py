from crudApp.models import User
import json
from crudApp import app, db
from flask import request


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello, Welcome to Flask Crud app, direct to localhost/users</h1>"


@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    if not users:
        return "<h1>No users found</h1>"
    ans = []
    for user in users:
        ans.append(user.__str__())
    return json.dumps(ans)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.form

    find_user = User.query.filter_by(name=data['name']).first()
    if find_user:
        return "User already exists"

    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return json.dumps(f"{user.name.capitalize()}'s account created.")


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    # user = User.query.get_or_404(user_id)
    if not user:
        return f"User with id {user_id} does not exist."
    return json.dumps(user.__str__())


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.form
    # user = User.query.get_or_404(user_id)
    user = User.query.get(user_id)
    if not user:
        return f"User with id {user_id} does not exist."
    if data.get('name'):
        user.name = data.get('name')
    if data.get('email'):
        user.email = data.get('email')
    db.session.commit()
    return json.dumps(user.__str__())


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204
