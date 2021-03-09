from flask import Flask, render_template,jsonify
from mybd_postgres import *


app = Flask(__name__)

cursor = connexion()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/json')
def result():
    cursor.execute("SELECT * FROM users;")
    results=cursor.fetchall()
    resp = jsonify(results)
    return resp

if __name__ == '__main__':
    print('Connexion flask :')
    app.run(host='0.0.0.0', port=3000, debug=True)


