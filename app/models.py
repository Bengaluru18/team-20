from app import db


class appointment(db.Model):
    __table__ = db.Model.metadata.tables['appointment']

    def __repr__(self):
        return self.aid

class specialist(db.Model):
    __table__ = db.Model.metadata.tables['specialist']
    def __repr__(self):
        return self.sname

class unavailability(db.Model):
    __table__ = db.Model.metadata.tables['unavailability']
    def __repr__(self):
        return self.sid

class unavailability(db.Model):
    __table__ = db.Model.metadata.tables['patient']
    def __repr__(self):
        return self.pid

