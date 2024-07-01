from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.model.models import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/pet_feeder_db'   #aici partea de baza de date postgres
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from application.model import models

    db.init_app(app)
    with app.app_context():
        db.create_all()


    #urmeaza partea de controler aici si partea de CORS
    CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

    from .controller.FoodScheduleController import foodScheduleController
    app.register_blueprint(foodScheduleController)
    from .controller.WeightStatisticsController import weightStatisticsController
    app.register_blueprint(weightStatisticsController)
    # with app.test_request_context():
    #     print(app.url_map)

    return app



