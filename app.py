from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import hashlib
from bson import ObjectId

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY5NjYxNDU0NCwiaWF0IjoxNjk2NjE0NTQ0fQ.kE4E0y3KIFAW2_0oZ5aqHC1DMbaYL_Qg2cX0JtqdnIU'
conn = MongoClient( 'mongodb+srv://mrprashantkrprasad:prashant007@learningmongodb.6tm3xbu.mongodb.net/sloovi')

db = conn['registration_db']
users_collection = db['users']
jwt = JWTManager(app)

@app.route('/register', methods=['POST', 'GET'])
def register():
        if request.method=='POST':
            try:
                data = request.get_json()
                first_name = data.get('first_name')
                last_name = data.get('last_name')
                email = data.get('email')
                password = data.get('password')

                if not (first_name and last_name and email and password):
                    return jsonify({"error": "All fields are required"}), 400

                # Checking existing user
                if users_collection.find_one({"email": email}):
                    return jsonify({"error": "Email already registered"}), 400

                hashed_password = generate_password_hash(data['password'], method='sha256')

                # Insert user data into the MongoDB collection
                user_data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "password": hashed_password,  # In a production environment, hash the password before storing.
                }
                users_collection.insert_one(user_data)

                return jsonify({'message': 'User registered and logged in successfully'}), 201

            except Exception as e:
                print(f"Error: {e}")
                return jsonify({"error": str(e)}), 500
        
        elif request.method == 'GET':
            return render_template('register.html')



@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'GET':
        # Render the login form
        return render_template('login.html')
    
    elif request.method == 'POST':
        data = request.form  # Use request.form to access form data

        user = conn.db.users.find_one({'email': data['email']})

        
        if user and check_password_hash(user['password'], data['password']):
            access_token = create_access_token(identity=data['email'])
            return jsonify({'message': 'Logged in successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    

@app.route('/template', methods=['POST', 'GET'])
@jwt_required()
def create_template():
    current_user = get_jwt_identity()

    data = request.get_json()
    template_name = data.get('template_name')
    subject = data.get('subject')
    body = data.get('body')

    # Creating a new template document in the database
    template_id = conn.db.templates.insert_one({
        'template_name': template_name,
        'subject': subject,
        'body': body
    }).inserted_id

    return jsonify({'message': 'Template created successfully', 'template_id': str(template_id)}), 201


@app.route('/template', methods=['GET'])
@jwt_required()
def get_all_templates():
    current_user = get_jwt_identity()

    templates = list(conn.db.templates.find({}, {'_id': False}))

    return jsonify({'templates': templates}), 200


@app.route('/template/<template_id>', methods=['GET'])
@jwt_required()
def get_single_template(template_id):
    current_user = get_jwt_identity()

    template = conn.db.templates.find_one({'_id': ObjectId(template_id)}, {'_id': False})
    if template:
        return jsonify({'template': template}), 200
    else:
        return jsonify({'message': 'Template not found'}), 404


@app.route('/template/<template_id>', methods=['PUT'])
@jwt_required()
def update_template(template_id):
    current_user = get_jwt_identity()

    data = request.get_json()
    template_name = data.get('template_name')
    subject = data.get('subject')
    body = data.get('body')

    # Update the template document in the database
    result = conn.db.templates.update_one({'_id': ObjectId(template_id)}, {
        '$set': {
            'template_name': template_name,
            'subject': subject,
            'body': body
        }
    })

    if result.modified_count > 0:
        return jsonify({'message': 'Template updated successfully'}), 200
    else:
        return jsonify({'message': 'Template not found'}), 404


@app.route('/template/<template_id>', methods=['DELETE'])
@jwt_required()
def delete_template(template_id):
    current_user = get_jwt_identity()

    # Delete the template document from the database
    result = conn.db.templates.delete_one({'_id': ObjectId(template_id)})

    if result.deleted_count > 0:
        return jsonify({'message': 'Template deleted successfully'}), 200
    else:
        return jsonify({'message': 'Template not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)