from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teste')
def teste():
    return render_template('teste.html')

if __name__ == '__main__':
    app.run(debug=True)
