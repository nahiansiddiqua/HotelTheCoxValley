import json

from flask import Flask, render_template ,request

app = Flask(__name__)


@app.route('/')
def home():

    with open('rooms.json', 'r') as file:
        rooms = json.load(file)

    return render_template('index.html', rooms=rooms)




@app.errorhandler(404)  
def not_found(e): 
  return render_template("404.html") 

# if __name__ == '__main__':
#     app.run(debug=True)