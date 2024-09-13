from .. import db


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)

    def __init__(self, username):
        self.username = username

class Patient(db.Model):
    __tablename__ = 'patient_id'
    id = db.Column(db.BigInteger, primary_key=True)
    patientname = db.Column(db.String(80),nullable=False)
    patientid =db.Column(db.BigInteger,nullable=False,unique=True)
    #angle_degrees = db.relationship('AngleDegree', backref='patient', lazy=True)

    def __init__(self, patientname,patientid):
        self.patientname = patientname
        self.patientid = patientid

class AngleDegree(db.Model):
    __tablename__ = 'patient_degree'
    id = db.Column(db.BigInteger,primary_key=True)
    left_angle_degree = db.Column(db.Float,nullable=False)
    right_angle_degree =db.Column(db.Float,nullable=False)
    patient_id = db.Column(db.BigInteger, db.ForeignKey('patient_id.patientid'), nullable=False)
    #GIF=db.Column(db.LargeBinary,nullable=False)

    def __init__(self,left_angle_degree, right_angle_degree, patient_id):
        self.left_angle_degree = left_angle_degree
        self.right_angle_degree = right_angle_degree
        self.patient_id = patient_id
        #self.gif = gif
    