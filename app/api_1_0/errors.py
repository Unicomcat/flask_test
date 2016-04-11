from flask import jsonify

def forbidden(message):
    respose= jsonify({'error':'forbidden','message':message})