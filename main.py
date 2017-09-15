from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name"/>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/") #this function will receive requests at the / path
def index():
    return form

@app.route("/hello", methods=['POST']) #get the name out of the request and greet user by their name
def hello():
    #first_name = request.args.get('first_name') #this is method"GET"
    first_name = request.form['first_name']  #this is method"POST"
    return '<h1>Hello, ' + first_name + '</h1>'

app.run()