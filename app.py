from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Data v JSON formátu
data = {
    "name": "Péťa",
    "age": 45,
    "city": "Vanďák",
    "job": "Učitel v institutu pro duševně choré",
    "description": "Jsem učitel s kryzí strědního věku a závislostí na kafíčkách",
    "signature": "KOZY"
    
}

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/api/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
