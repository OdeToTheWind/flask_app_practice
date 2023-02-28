from flask import Flask, render_template, request

app = Flask(__name__)

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
    colours = ['Red', 'Blue', 'Black', 'Orange']
    cars = ['car1', 'car2', 'car3', 'car4', 'car5', 'car6', 'car7']
#    return render_template('example.html' )    # This is also working, without passing LINKS to that HTML file.
    return render_template('example.html', links=links, colours=colours, cars=cars)

@app.route("/process", methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

#    return 'Name is: ' + name + ' and the comment is: ' + comment     # This line is also working, but def feunction can return only one task.
    return render_template('index.html', name=name, comment=comment)

@app.route("/dropdwn", methods=['POST'])
def dropdown():
    colour = request.form.get('colour')
    car = request.form.get('car')
    
    return render_template('dropdown.html', colour=colour, car=car)

if __name__ == '__main__':
    app.run(debug=True)
