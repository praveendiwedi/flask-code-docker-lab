from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()

    return f"""
    <h1>Hello, my name is Your Name</h1>
    <p>Current Date: {now.strftime('%d-%m-%Y')}</p>
    <p>Current Time: {now.strftime('%H:%M:%S')}</p>
    """

if __name__ == "__main__":
    app.run()
