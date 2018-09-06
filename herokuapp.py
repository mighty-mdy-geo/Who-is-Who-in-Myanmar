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




if __name__ == '__main__':
    app.run(debug=True)
