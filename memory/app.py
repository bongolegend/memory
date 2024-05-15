from flask import Flask, request, jsonify
from google.cloud.firestore import SERVER_TIMESTAMP
import hashlib
import time

from memory.config import config
from memory.firestore import db


app = Flask(__name__)


def generate_hash_id(prefix):
    return f"{prefix}-{hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]}"


@app.route('/health', methods=['GET'])
@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "UP"}), 200

# CRUD for Users
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = generate_hash_id('user')
    user_data = {
        'id': user_id,
        'name': data['name'],
        'created_at': SERVER_TIMESTAMP
    }
    db.collection('users').document(user_id).set(user_data)
    return jsonify(user_data), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_ref = db.collection('users').document(user_id)
    user = user_ref.get()
    if user.exists:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user_ref = db.collection('users').document(user_id)
    user_ref.update(data)
    return jsonify({'success': True}), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_ref = db.collection('users').document(user_id)
    user_ref.delete()
    return jsonify({'success': True}), 200

# CRUD for Journals
@app.route('/users/<user_id>/journals', methods=['POST'])
def create_journal(user_id):
    data = request.json
    journal_id = generate_hash_id('jour')
    journal_data = {
        'id': journal_id,
        'name': data['name'],
        'created_at': SERVER_TIMESTAMP
    }
    db.collection('users').document(user_id).collection('journals').document(journal_id).set(journal_data)
    return jsonify(journal_data), 201

@app.route('/users/<user_id>/journals/<journal_id>', methods=['GET'])
def get_journal(user_id, journal_id):
    journal_ref = db.collection('users').document(user_id).collection('journals').document(journal_id)
    journal = journal_ref.get()
    if journal.exists:
        return jsonify(journal.to_dict()), 200
    else:
        return jsonify({'error': 'Journal not found'}), 404

@app.route('/users/<user_id>/journals/<journal_id>', methods=['PUT'])
def update_journal(user_id, journal_id):
    data = request.json
    journal_ref = db.collection('users').document(user_id).collection('journals').document(journal_id)
    journal_ref.update(data)
    return jsonify({'success': True}), 200

@app.route('/users/<user_id>/journals/<journal_id>', methods=['DELETE'])
def delete_journal(user_id, journal_id):
    journal_ref = db.collection('users').document(user_id).collection('journals').document(journal_id)
    journal_ref.delete()
    return jsonify({'success': True}), 200

# CRUD for Entries
@app.route('/users/<user_id>/journals/<journal_id>/entries', methods=['POST'])
def create_entry(user_id, journal_id):
    data = request.json
    entry_id = generate_hash_id('entr')
    entry_data = {
        'id': entry_id,
        'name': data['name'],
        'content': data['content'],
        'created_at': SERVER_TIMESTAMP
    }
    db.collection('users').document(user_id).collection('journals').document(journal_id).collection('entries').document(entry_id).set(entry_data)
    return jsonify(entry_data), 201

@app.route('/users/<user_id>/journals/<journal_id>/entries/<entry_id>', methods=['GET'])
def get_entry(user_id, journal_id, entry_id):
    entry_ref = db.collection('users').document(user_id).collection('journals').document(journal_id).collection('entries').document(entry_id)
    entry = entry_ref.get()
    if entry.exists:
        return jsonify(entry.to_dict()), 200
    else:
        return jsonify({'error': 'Entry not found'}), 404

@app.route('/users/<user_id>/journals/<journal_id>/entries/<entry_id>', methods=['PUT'])
def update_entry(user_id, journal_id, entry_id):
    data = request.json
    entry_ref = db.collection('users').document(user_id).collection('journals').document(journal_id).collection('entries').document(entry_id)
    entry_ref.update(data)
    return jsonify({'success': True}), 200

@app.route('/users/<user_id>/journals/<journal_id>/entries/<entry_id>', methods=['DELETE'])
def delete_entry(user_id, journal_id, entry_id):
    entry_ref = db.collection('users').document(user_id).collection('journals').document(journal_id).collection('entries').document(entry_id)
    entry_ref.delete()
    return jsonify({'success': True}), 200

if __name__ == '__main__':
    app.run(debug=config["FLASK_DEBUG"], port=config['FLASK_PORT'])
