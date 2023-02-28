from flask import Flask, render_template, request
#    from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#       app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12601613:Zse?$789Qsc@sql12.freemysqlhosting.net/sql12601613'
#       app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#       
#       db = SQLAlchemy(app)
#       
#       class Comments(db.Model):
#           id = db.Column(db.Integer, primary_key=True)
#           name = db.Column(db.String(20))
#           comment = db.Column(db.String(1000))
    
@app.route("/")
def index():
#     return '<h1>Hello There!</h1>'
    return render_template('index.html')

@app.route("/sign")
def sign():
    return render_template('sign.html')

#  @app.route("/home", methods=['GET', 'POST'])
#  def home():
#      return '<h1> You are on the home page ! </h1>'

@app.route("/home", methods=['GET', 'POST'])
def home():
    links = ['https://www.youtube.com/', 'https://www.bing.com/', 'https://www.python.org/', 'https://www.english.com/']
#    return render_template('example.html' )    # This is also working, without passing LINKS to that HTML file.
    return render_template('example.html', links=links)

@app.route("/process", methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

#    return 'Name is: ' + name + ' and the comment is: ' + comment     # This line is also working, but def feunction can return only one task.
    return render_template('index.html', name=name, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)
