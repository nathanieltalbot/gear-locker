"""Module containing data definitions for tables in the gear database"""
from app import db


'''
Explanation:
This is a 'pythonic' way of representing database objects in postgres
in lieu of using raw SQL statements in python code
This allows for extensibility as well as for generally cleaner-looking
code. 
Documentation can be found here: https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
'''

# Representing a member of the club
class ClubMember(db.Model):
    """Representing a member of the club with identifying attributes."""

    __tablename__ = 'club_member'

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    status = db.Column(db.Boolean())
    name = db.Column(db.String())
    email = db.Column(db.String())

    # initiate the variables
    def __init__(self, status, name, email):
        """Creates a club_member object with given status, name, and email."""
        self.status = status
        self.name = name
        self.email = email

    # overriding default __repr__ method 
    def __repr__(self):
        """Overriding default __repr__ method to return the ID of the club member."""
        return 'id:{}'.format(self.id)
    
    # overriding default __str__ method for object which allows printing
    def __str__(self):
        """Overriding default __str__ method to return all fields of the club member."""
        return 'id: {}\nstatus: {}\nname: {}\nemail: {}'.format(self.id, self.status, self.name, self.email)

class GearItem(db.Model):
    """Representing an item of gear available to rent from the gear locker."""

    _tablename_ = 'gear_item'

    gear_id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    status = db.Column(db.Boolean())
    name = db.Column(db.String())
    brand = db.Column(db.String())
    condition = db.Column(db.String())
    best_use = db.Column(db.String())

    def __init__(self, status, name, brand, condition, best_use):
        """Creates a gear object with given status, name, brand, condition, and best use."""
        self.status = status
        self.name = name
        self.brand = brand
        self.condition = condition
        self.best_use = best_use

    # used in subclass inheritance
    __mapper_args__ = {
        'polymorphic_identity': 'gear_item',
        'polymorphic_on': name
    }

    def __repr__(self):
        """Overriding default __repr__ method to return the ID of the gear item."""
        return 'id:{}'.format(self.id)

    def __str__(self):
        """Overriding default __str__ method to return all fields of the gear item."""
        return 'id: {}\nstatus: {}\nname: {}\nbrand: {}\ncondition: {}\nbest_use:{}'.format(
            self.id, self.status, self.name, self.brand, self.condition, self.best_use)

'''
Notes, for reference:
The classes below are subclasses of gear_item
and inherit using the joined table inheritance pattern,
one of several ways to set up table inheritance in the SQLALchemy ORM

For more information on these patterns, see: 
https://docs.sqlalchemy.org/en/13/orm/inheritance.html#joined-table-inheritance
'''

class SleepingBag(GearItem):
    """Subclass of GearItem, contains specific information on a sleeping bag."""

    __tablename__ = 'sleeping_bag'

    id = db.Column(db.Integer(), db.ForeignKey('gear_item.gear_id'), primary_key=True)
    gender = db.Column(db.String())
    size = db.Column(db.String())
    bag_type = db.Column(db.String())
    temp_rating = db.Column(db.Integer())
    insulation = db.Column(db.String())

    #TODO -- this can and probably should be refactored using the Builder pattern
    #this will reduce the number of parameters
    def __init__(self, status, name, brand, condition, best_use, gender, size, temp_rating, insulation):
        """Creates a sleeping bag object with the given attributes."""
        gear_item.__init__(self, status, name, brand, condition, best_use)
        self.gender = gender
        self.size = size
        self.bag_type = bag_type
        self.temp_rating = rating
        self.insulation = insulation
        
   #Used by SQLAlchemy for class polymorphism
    __mapper_args__ = {
        'polymorphic_identity': 'sleeping_bag',
    }

# Representing a tent with specific tent-related attributes
class Tent(GearItem):
    """Representing a tent with specific attributes of capacity and type."""
    __tablename__ = 'tent'
    id = db.Column(db.Integer(), db.ForeignKey('gear_item.gear_id'), primary_key=True)
    capacity = db.Column(db.String())
    tent_type = db.Column(db.String())
    
    def __init__(self, status, name, brand, condition, best_use, capacity, tent_type):
        """Creates a tent object with the given attributes."""
        gear_item.__init__(self, status, name, brand, condition, best_use)
        self.capacity = capacity
        self.tent_type = tent_type
    
    __mapper_args__ = {
        'polymorphic_identity': 'tent',
    }

class Reservation(db.Model):
    """Representing a gear item reserved by a given member."""
    
    __tablename__ = 'reservation'
    
    # The IDs of the member and the gear jointly make up the primary key of the reservation
    member_id = db.Column(db.Integer(), db.ForeignKey('club_member.id'), primary_key=True)
    gear_id = db.Column(db.Integer(), db.ForeignKey('gear_item.gear_id'), primary_key=True)

    def __init__(self, member_id, gear_id):
        """Constructs a Reservation object with a given member ID and gear ID."""
        self.member_id = member_id
        self.gear_id = gear_id
