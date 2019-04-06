import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import club_member

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

    

if __name__ == '__main__':
    app.run()
