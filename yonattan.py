#! /usr/bin/python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index0.html')

if __name__ == "__main__":
    app.run()
else:
    print('nothings')