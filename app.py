import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import ClubMember, GearItem, Reservation


# For page for adding members.
@app.route("/add_member", methods=['GET', 'POST'])
def add_member():
    """Loads content for the add_member page when called by Flask."""
    if request.method == 'POST':
        status = request.form.get('status')
        if status == "True":
            status = True
        else:
            status = False
        name = request.form.get('name')
        email = request.form.get('email')
        try:
            member = ClubMember(status=status, name=name, email=email)
            # Checks if email is of a valid format
            if ("@" in email) and ("." in email):
                db.session.add(member)
                db.session.commit()
                return "Member added. member id={}".format(member.id)
            else:
                return "Please enter a valid email address."
        except Exception as e:
            return str(e)
    return render_template("add_member.html")


# page for adding gear
@app.route("/add_gear", methods=['GET', 'POST'])
def add_gear():
    """Loads content for the add_gear page when called by Flask."""
    if request.method == 'POST':
        status = request.form.get('status')
        if status == "True":
            status = True
        else:
            status = False
        name = request.form.get("name")
        brand = request.form.get("brand")
        condition = request.form.get("condition")
        best_use = request.form.get("best_use")
        try:
            item = GearItem(status=status, brand=brand, name=name, condition=condition, best_use=best_use)
            db.session.add(item)
            db.session.commit()
            return "Gear added. gear id={}".format(item.gear_id)
        except Exception as e:
            return str(e)
    return render_template("add_gear.html")


# home page
@app.route("/")
def home():
    """Loads content for the home page when called by Flask."""
    return render_template("home.html")


# deleting members/items
@app.route("/delete", methods=['GET','POST'])
def delete():
    """Loads content for the delete page when called by Flask."""
    if request.method == 'POST':
        gear_id = request.form.get("g_id")
        try:
            g_item = db.session.query(GearItem).get(gear_id)
            # Checks if a gear item exists with the given ID number
            if g_item is not None:
                db.session.delete(g_item)
                db.session.commit()
                return "Gear item deleted with id={}".format(gear_id)
            else:
                return "Please enter a valid Gear ID."
        except Exception as e:
            return str(e)
    return render_template("delete.html")


# finding info on members/items
@app.route("/view", methods=['GET', 'POST'])
def view():
    """Loads content for the view page when called by Flask."""
    if request.method == 'POST':
        member_id = request.form.get("member_id")
        try:
            member = db.session.query(ClubMember).get(member_id)
        except Exception as e:
            return str(e)

        # display results if member exists with valid ID number
        if member is not None:
            return render_template('results.html', member_obj=member)
        else:
            return "Please enter a valid Member ID."
    return render_template('search.html')


# For a member to reserve a gear item
@app.route("/reserve", methods=['GET', 'POST'])
def reserve():
    """Loads content for the reserve page when called by Flask."""
    if request.method == 'POST':
        member_id = request.form.get("mem_id")
        gear_id = request.form.get("g_id")
        member = db.session.query(ClubMember).get(member_id)
        item = db.session.query(GearItem).get(gear_id)

        # testing to see if member and gear are defined
        try: member
        except Exception: member = None
        
        try: item
        except Exception: item = None

        # Different checks to ensure both the gear ID and member ID are valid
        if member == None:
            return "Must be a valid member ID!"
        elif item == None:
            return "Must be a valid gear ID!"
        elif not member.status:
            return "Member must be an active member!"
        elif not gear_item.status:
            return "Gear item must be available!"
        else:
            try:
                reserved = Reservation(member_id=member_id, gear_id=gear_id)
                db.session.add(reserved)
                item.status = False
                db.session.commit()
                return "Member with ID {} has reserved gear with ID {}".format(member_id, gear_id)
            except Exception as e:
                return str(e)
    return render_template("reservations.html")


# changing the status of a member
@app.route("/change_status", methods=['GET', 'POST'])
def status():
    """Loads content for the change_status page when called by Flask."""
    if request.method == 'POST':
        member_id = request.form.get("mem_id")
        status = request.form.get('status')
        if status == "True":
            status = True
        else:
            status = False
        
        member = db.session.query(ClubMember).get(member_id)
        
        try: member
        except Exception: member = None

        if member == None:
            return "Must be a valid member!"
      
        else:
            member.status = status
            db.session.commit()
            return "Member of ID {} updated to {}".format(member_id, status)
    return render_template("status.html")


if __name__ == '__main__':
    app.run()
