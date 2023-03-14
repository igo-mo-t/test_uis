

class Accrual:
    id = db.Column(db.Integer(), primary_key = True)
    date = db.Column(db.DateTime())
    month = db.Column(db.Integer())

class Payment:
    id = db.Column(db.Integer(), primary_key = True)
    date = db.Column(db.DateTime())
    month = db.Column(db.Integer())    