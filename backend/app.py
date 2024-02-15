from flask import Flask, request,jsonify,make_response
from flask_cors import CORS
from models.user import User
from db import db
from os import environ

app = Flask(__name__)
CORS(app)
with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI']=environ.get("DATABASE_URL")
    db.init_app(app)
    db.create_all()

@app.route('/test',methods=['GET'])
def test():
    return jsonify({'message':'The server is running'})

@app.route('/api/flask/users',methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(name=data['name'],email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            'id':new_user.id,
            'name':new_user.name,
            'email':new_user.email
        }),201
    except Exception as e:
        return make_response(jsonify({
            'message':'Error has occured during user creation',
            'error': str(e)
            }))

@app.route('/api/flask/users',methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        users_data = [{'id':user.id,'name':user.name,'email':user.email} for user in users]
        return jsonify(users_data),200
    except Exception as e:
        return make_response(jsonify({
            'message':'Error while getting user',
            'error': str(e)
            }))
    
@app.route('/api/flask/users/<int:id>',methods=['GET'])
def get_user_by_id(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'user':user.json()}),200)
        return make_response(jsonify({'message':'user not found'}),404)
    except Exception as e:
        return make_response(jsonify({
            'message':'Error has occured during getting user',
            'error': str(e)
            }),500)
    
@app.route('/api/flask/users/<int:id>',methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.name = data['name']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({
            'message':'User updated'
            }),200)
        return make_response(jsonify({
            'message':'User not found'
            }),404)
    except Exception as e:
        return make_response(jsonify({
            'message':'Error has occured during updating user',
            'error': str(e)
            }),500)

@app.route('/api/flask/users/<int:id>',methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({
            'message':'User deleted'
            }),200)
        return make_response(jsonify({
            'message':'User not found'
            }),404)
    except Exception as e:
        return make_response(jsonify({
            'message':'Error has occured during delete operation',
            'error': str(e)
            }),500)