from flask import Flask, request,jsonify,make_response
from flask_cors import CORS
import models
from os import environ
from db import db

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI']=environ.get("DATABASE_URL")
    db.init_app(app)
    db.create_all()
    return app

app = create_app()

@app.route('/test',methods=['GET'])
def test():
    return jsonify({'message':'The server is running'})