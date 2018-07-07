from app import db


class appointment(db.Model):
    __table__ = db.Model.metadata.tables['appointment']

    def __repr__(self):
        return self.aid

class specialist(db.Model):
    __table__ = db.Model.metadata.tables['specialist']
    def __repr__(self):
        return self.sname

class unavailibility(db.Model):
    __table__ = db.Model.metadata.tables['unavailibility']
    def __repr__(self):
        return self.sid


