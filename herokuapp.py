from flask import Flask , render_template, request
import os 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "whoiswho.db"))


app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "Who is Who in Myanmar"
db = SQLAlchemy(app)

search_name = ""

class Politician(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)
	initialname=db.Column(db.String(10),nullable=False)
	birth = db.Column(db.String(30),nullable=False)
	occupation = db.Column(db.String(30),nullable=False)
	photo = db.Column(db.Text,nullable=False)
	facebook = db.Column(db.Text,nullable=False)
	bio = db.Column(db.Text,nullable=True)

	def __init__(self,*args,**kwargs):
		super(Politician,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<Politician %r>' % self.name

class BusinessLeader(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)
	initialname=db.Column(db.String(10),nullable=False)
	birth = db.Column(db.String(30),nullable=False)
	occupation = db.Column(db.String(30),nullable=False)
	photo = db.Column(db.Text,nullable=False)
	facebook = db.Column(db.Text,nullable=False)
	bio = db.Column(db.Text,nullable=True)

	def __init__(self,*args,**kwargs):
		super(BusinessLeader,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<BusinessLeader %r>' % self.name

class Celebrity(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)
	initialname=db.Column(db.String(10),nullable=False)
	birth = db.Column(db.String(30),nullable=False)
	occupation = db.Column(db.String(30),nullable=False)
	photo = db.Column(db.Text,nullable=False)
	facebook = db.Column(db.Text,nullable=False)
	bio = db.Column(db.Text,nullable=True)

	def __init__(self,*args,**kwargs):
		super(Celebrity,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<Celebrity %r>' % self.name



if __name__ == '__main__':
    app.run(debug=True)
