from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ibm-index.html')

@app.route('/login/', methods=['POST','GET'])
def form_post():
    if request.method == 'GET':
        return f"The URL /login is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('ibm-image.html',form_data = form_data)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)