import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/test')
def test():
    return "Test"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
