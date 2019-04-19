import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

# from flask_table import Table, Col

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import club_member, gear_item

#For page for adding members.
@app.route("/add_member", methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        status = request.form.get('status')
        if (status == "True"):
            status = True
        else:
            status = False
        name = request.form.get('name')
        email = request.form.get('email')
        try:
            member = club_member(status=status, name=name, email=email)
            db.session.add(member)
            db.session.commit()
            return "Member added. member id={}".format(member.id)
        except Exception as e:
            return(str(e))
    return render_template("add_member.html")

#page for adding gear
@app.route("/add_gear", methods=['GET', 'POST'])
def add_gear():
    if request.method == 'POST':
        status = request.form.get('status')
        if (status == "True"):
            status = True
        else:
            status = False
        name = request.form.get("name")
        brand = request.form.get("brand")
        condition = request.form.get("condition")
        best_use = request.form.get("best_use")
        try:
            item = gear_item(status=status, brand=brand, name=name, condition=condition, best_use=best_use)
            db.session.add(item)
            db.session.commit()
            return "Gear added. gear id={}".format(item.gear_id)
        except Exception as e:
            return(str(e))
    return render_template("add_gear.html")

#home page
@app.route("/")
def home():
    return render_template("home.html")

#deleting members/items
@app.route("/delete", methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        member_id = request.form.get("g_id")
        try:
            g_item = db.session.query(gear_item).get(member_id)
            db.session.delete(g_item)
            db.session.commit()
            return "Gear item deleted with id={}".format(member_id)
        except Exception as e:
            return(str(e))
    return render_template("delete.html")


# deleting members/items
@app.route("/view", methods=['GET'])
def view(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db.session.query(gear_item)
        results = qry.all()

    if not results:
        return 'No results found!'
    else:
        # display results
        table = gear_item(results)
        table.border = True
        return render_template('results.html', table=table)



if __name__ == '__main__':
    app.run()
