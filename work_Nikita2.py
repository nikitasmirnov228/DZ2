from flask import Flask, request, current_app

app = Flask(__name__)

@app.route('/')
def index():
    with app.test_request_context('/'):
        p = request.path
        m = request.method
        n = current_app.name
    print(p + " "+m+" " +n)
    return 'Home Page'

@app.route('/career/')
def career():
    with app.test_request_context('/career/'):
        p = request.path
        m = request.method
        n = current_app.name
    print(p + " "+m+" " +n)
    return 'Career Page'

@app.route('/feedback/')
def feedback():
    with app.test_request_context('/feedback/'):
        p = request.path
        m = request.method
        n = current_app.name
    print(p + " "+m+" " +n)
    return 'Feedback Page'

@app.route('/user/<id>/')
def User_Profile(id):
    with app.test_request_context('/user/<is>/'):
        p = request.path
        m = request.method
        n = current_app.name
    print(p + " "+m+" " +n)
    return "Profile page of user #{}".format(id)
    
if __name__ == "__main__":
    app.run(debug=True)