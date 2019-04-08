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

class gear_item(db.Model):
    _tablename_ = 'gear_item'

    gear_id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    status = db.Column(db.Boolean())
    brand = db.Column(db.String())
    name = db.Column(db.String())
    condition = db.Column(db.String())
    best_use = db.Column(db.String())

    def __init__(self, status, brand, name, condition, best_use):
        self.status = status
        self.brand = brand
        self.name = name
        self.condition = condition
        self.best_use = best_use

    # overriding default _repr_ method
    def __repr__(self):
        return 'id:{}'.format(self.id)

    # overriding default _str_ method for object which allows printing
    def __str__(self):
        return 'id: {}\nstatus: {}\nbrand: {}\nname: {}\ncondition: {}\nbest_use:{}'.format(
            self.id, self.status, self.brand, self.name, self.condition, self.best_use)

    # potentially useful for JSON usage
    def serialize(self):
        return {
            'gear_id': self.id,
            'status': self.status,
            'brand': self.brand,
            'name': self.name,
            'condition': self.condition,
            'best_use':self.best_use
        }
'''
class Reservations(db.Model):
    member = db.Column(Integer
'''