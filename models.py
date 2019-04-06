from app import db

'''
Explanation:
This is a 'pythonic' way of representing database objects in postgres
in lieu of using raw SQL statements in python code
This allows for extensibility as well as for generally cleaner-looking
code. 
Documentation can be found here: https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
'''
class club_member(db.Model):
    __tablename__ = 'club_member'

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    status = db.Column(db.Boolean())
    name = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, status, name, email):
        self.status = status
        self.name = name
        self.email = email

    # overriding default __repr__ method 
    def __repr__(self):
        return 'id:{}'.format(self.id)
    
    # overriding default __str__ method for object which allows printing
    def __str__(self):
        return 'id: {}\nstatus: {}\nname: {}\nemail: {}'.format(self.id, self.status, self.name, self.email)

    #potentially useful for JSON usage
    def serialize(self):
        return {
            'id': self.id,
            'status': self.status,
            'name': self.name,
            'email': self.email
        }
'''
class Reservations(db.Model):
    member = db.Column(Integer
'''
