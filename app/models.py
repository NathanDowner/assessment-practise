from . import db

links = db.Table('links',
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.staff_id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.project_id'))
)

class Staff(db.Model):
    # __tablename__ = 'staff_members'
    staff_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    position = db.Column(db.String(20))
    projects = db.relationship('Project', secondary=links,
        backref = db.backref('team_members', lazy='dynamic'))
    
    def __init__(self, fname, lname, pos):
        self.fname = fname
        self.lname = lname
        self.position = pos
        
    def __repr__(self):
        return '<Staff {}>'.format(self.fname)
        
class Project(db.Model):
    # __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(20), nullable=False)
    
    
    def __init__(self, name):
        self.project_name = name
        
    def __repr__(self):
        return '<Project {}>'.format(self.project_name)