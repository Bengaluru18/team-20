from app import db


class appointment(db.Model):
    __table__ = db.Model.metadata.tables['appointment']

    def __repr__(self):
        return self.aid

class specialist(db.Model):
    __table__ = db.Model.metadata.tables['specialist']
    def __repr__(self):
        return self.sname

class unavail(db.Model):
    __table__ = db.Model.metadata.tables['unavail']
    def __repr__(self):
        return self.sid

class patient(db.Model):
    __table__ = db.Model.metadata.tables['patient']
    
    def __json__(self):
        return ['pid', 'pname', 'dob', 'parent_name', 'phno', 'address', 'comment' ]

