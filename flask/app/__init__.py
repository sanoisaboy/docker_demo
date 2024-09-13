from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

from .config.config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    # 設定config
    app.config.from_object(config['development'])

    db.init_app(app)

    from .models.users import Person,Patient,AngleDegree

    @app.route('/')
    def index():
        return 'hello world'

    @app.route('/create')
    def create_db():
        db.create_all()
        return 'ok'

    @app.route('/max',methods=['POST'])
    def insert_max():
        #u = Person('Max')
        #db.session.add(u)
        #data = request.get_json()
        
        id = request.args.get('id')
        patient_id = request.args.get('patient_id')
        name = request.args.get('name')

        degree_id = request.args.get('patient_degree_id')
        left_angle_degree = request.args.get('left_angle_degree')
        right_angle_degree = request.args.get('right_angle_degree')
        #GIF = request.args.get('GIF')
        
        if not patient_id or not name or not id:
            return jsonify({'error': '缺少必要的資料'}), 400
        
        existing_patient = Patient.query.filter_by(patientid=patient_id).first()
    
        if existing_patient:
            angle_degree = AngleDegree(left_angle_degree,right_angle_degree,patient_id)
            db.session.add(angle_degree)
            db.session.commit()
            return jsonify({'error': f'Patient ID {patient_id} 已存在'}), 200
        
        patient = Patient(name,patient_id)
        db.session.add(patient)
        angle_degree = AngleDegree(left_angle_degree,right_angle_degree,patient_id)
        db.session.add(angle_degree)
        db.session.commit()
        return 'ok'
    
    @app.route('/get')
    def get_data():
         
        patient_id = request.args.get('patient_id')

        if not patient_id :
            return jsonify({'error': '缺少必要的資料'}), 400
        
        existing_patient = Patient.query.filter_by(patientid=patient_id).first()
        existing_angle_degree = AngleDegree.query.filter_by(patientid=patient_id).first()

        return jsonify({'error': f'Patient ID {existing_patient} 已存在'}), 200
    
       

    return app
