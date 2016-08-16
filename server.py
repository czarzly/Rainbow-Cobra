#! /usr/bin/python

from flask import Flask, jsonify
from flask import Response
from flask import request
from pymongo import MongoClient


app = Flask(__name__)

mongo_client = MongoClient()



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
    mongo_client.rainbow.contacts.insert(contactinfo)

    return jsonify({"status": "success"})

@app.route('/contacts-details')
def contacts_info():
    def map_contacts(contact):
        contact.pop("_id")
        return contact
    contacts = mongo_client.rainbow.contacts.find()
    contacts = map(map_contacts, contacts)

    return jsonify({"contacts": contacts})

if __name__ == "__main__":
     app.run(debug=True)
