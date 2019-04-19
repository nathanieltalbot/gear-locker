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

    # potentially useful for JSON usage
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
    name = db.Column(db.String())
    brand = db.Column(db.String())
    condition = db.Column(db.String())
    best_use = db.Column(db.String())

    def __init__(self, status, name, brand, condition, best_use):
        self.status = status
        self.brand = brand
        self.name = name
        self.condition = condition
        self.best_use = best_use

    # used in subclass inheritance
    __mapper_args__ = {
        'polymorphic_identity': 'gear_item',
        'polymorphic_on': type
    }

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


class sleepingBag(gear_item):
    __tablename__ = 'sleeping_bag'
    id = db.Column(db.Integer(), db.ForeignKey('gear_item.gear_id'), primary_key=True)
    gender = db.Column(db.String())
    size = db.Column(db.String())
    bag_type = db.Column(db.String())
    temp_rating = db.Column(db.Integer())
    insulation = db.Column(db.String())

    __mapper_args__ = {
        'polymorphic_identity': 'sleeping_bag',
    }

# class tent(gear_item):
#     __tablename__ = 'tent'
#     id = db.Column(db.Integer(), db.ForeignKey('gear_item.gear_id'), primary_key=True)
#     capacity = db.Column(db.String())
#     type = db.Column(db.String())
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'tent',
#     }
#
#
# class microspikes(gear_item):
#     __tablename__ = 'tent'
#     id = db.Column(db.Integer(), db.ForeignKey('gear_item.gear_id'), primary_key=True)
#     size = db.Column(db.String())
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'microspikes',
#     }
#
#
# class hikingPoles(gear_item):
#     __tablename__ = 'tent'
#     id = db.Column(db.Integer(), db.ForeignKey('gear_item.gear_id'), primary_key=True)
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'hikingPoles',
#     }
