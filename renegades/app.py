from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///User.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


class User(db.Model):
    sno= db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(25), nullable= False)
    email = db.Column(db.String(25), nullable=False)
    message = db.Column(db.String(500), nullable= False)

    def __repr__(self) -> str:
        return f"{self.name} - {self.email}"

@app.route("/", methods=["GET", "POST"])
def details():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        user = User(name= name, email= email, message=message)
        db.session.add(user)
        db.session.commit()
    return render_template("index.html")



if __name__ =="__main__":
    app.run(debug=True)