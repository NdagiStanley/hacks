from flask import Flask, Response
from tasks import add


app = Flask(__name__)

@app.route("/")
def index():
    return "Celery hack!"

@app.route("/celery_hack/<int:i>")
def task(i):
    list = []
    for f in range(i):
        list.append(add.delay(i^2, i))
    return Response(list[0])

if __name__ == "__main__":
    app.run(debug=True)
