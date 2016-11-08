#! /usr/bin/python
from datetime import datetime
now = datetime.now

from flask import Flask, jsonify
from flask import Response
from flask import request
from pymongo import MongoClient


app = Flask(__name__)

mongo_client = MongoClient()


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/about-us')
def about_us():
    return app.send_static_file('about.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')

@app.route('/contact-us', methods=["POST"])
def contact_us():
    try:
        
        contactinfo = {
            "message": request.values['message'],
            "sent_time": now()
        }

        mongo_client.rainbow.contacts.insert(contactinfo)

        return jsonify({"status": "success"})
    except Exception as ex:
        print ex
        return jsonify({"status": "disaster"})

@app.route('/contacts-details')
def contacts_info():
    def map_contacts(contact):
        contact.pop("_id")
        return contact
    contacts = mongo_client.rainbow.contacts.find()
    contacts = map(map_contacts, contacts)

    return jsonify({"contacts": contacts})

@app.route('/admin')
def admin():
    return app.send_static_file('admin.html')



if __name__ == "__main__":
     app.run(debug=True)
