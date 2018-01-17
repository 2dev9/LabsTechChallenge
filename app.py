from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/dah2184', methods=['GET'])
def main():
    return render_template('devon.html')

if __name__ == '__main__':
    app.run()
