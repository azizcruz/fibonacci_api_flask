from db import db

# Database Table.
class FibData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_idx = db.Column(db.Integer, nullable=False)
    end_idx = db.Column(db.Integer, nullable=False)

    def __init__(self, start, end):
        self.start_idx = start
        self.end_idx = end

    def __repr__(self):
        return '<data>'
