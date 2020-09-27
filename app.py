# import flask dependency 
from flask import Flask 

# create a new Flask instance 
app = Flask(__name__)

# create Flask routes 
@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == "__main__":
    app.run(debug=True)
