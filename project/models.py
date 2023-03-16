from project import db

class Accrual(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    date = db.Column(db.Date())
    month = db.Column(db.Integer())

class Payment(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    date = db.Column(db.Date())
    month = db.Column(db.Integer())    