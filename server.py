#! /usr/bin/python

from flask import Flask, jsonify
from flask import Response
from flask import request
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient()



@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')

@app.route('/contact-us', methods=["POST"])
def contact_us():
    print(request.values['key'])
    contactinfo = {"hi": request.values['key']}
    client.rainbow.contacts.insert(contactinfo)

    contactinfo.pop('_id')
    print(contactinfo)
    return jsonify(contactinfo)


if __name__ == "__main__":
     app.run()
