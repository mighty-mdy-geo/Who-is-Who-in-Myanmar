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

@app.route('/',methods=['POST','GET'])
def home():
	people = News.query.all()
	
	if request.method == 'POST':
		search = request.form['search']
		names = People.query.order_by(People.name).all()
		results = People.query.filter(People.name.like('%' + search + '%')).all()
		return render_template("result.html",results = results)
	return render_template("home.html",people=people)

@app.route('/home.html',methods=['POST','GET'])
def homepg():
    people = News.query.all()
    return render_template("home.html",people=people)

@app.route('/politician.html',methods=['POST','GET'])
def politician():
	politician = Politician.query.all()
	return render_template("politician.html",politician=politician)

@app.route('/businessleader.html',methods=['POST','GET'])
def business():
    business = BusinessLeader.query.all()
    return render_template("businessleader.html",business=business)

@app.route('/celebrity.html',methods=['POST','GET'])
def celebrity():
    cele = Celebrity.query.all()
    return render_template("celebrity.html",cele=cele)


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

class People(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)
	initialname=db.Column(db.String(10),nullable=False)
	birth = db.Column(db.String(30),nullable=False)
	occupation = db.Column(db.String(30),nullable=False)
	photo = db.Column(db.Text,nullable=False)
	facebook = db.Column(db.Text,nullable=False)
	bio = db.Column(db.Text,nullable=True)

	def __init__(self,*args,**kwargs):
		super(People,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<People %r>' % self.name

class News(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	photo = db.Column(db.Text,nullable=False)
	content = db.Column(db.Text,nullable=True)
	link = db.Column(db.Text,nullable=True)


	def __init__(self,*args,**kwargs):
		super(News,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<News %r>' % self.id

if __name__ == '__main__':
    app.run(debug=True)
