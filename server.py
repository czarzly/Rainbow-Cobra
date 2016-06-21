#! /usr/bin/python

from flask import Flask
from flask import Response
from flask import request

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/contact-us', methods=["POST"])
def contact_us():
    print(request.values["key"])
    return Response("ok")


if __name__ == "__main__":
     app.run()
