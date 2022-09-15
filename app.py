from flask import Flask, render_template

from flask import jsonify, request

app = Flask(__name__)

@app.route('/index1.html')
@app.route('/')
def hello():
    return render_template("index1.html")

@app.route('/fleece.html')
def fleece():
    return render_template("fleece.html")

@app.route('/shoes.html')
def shoes():
    return render_template("shoes.html")

@app.route('/jackets.html')
def jackets():
    return render_template("jackets.html")

@app.route('/power/<int:nmb>'
def power(nmb):
    val= nmb **2
    return jsonify({'data':val})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555)
