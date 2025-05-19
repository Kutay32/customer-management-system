from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///customer.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-RESTful API
api = Api(app)

# Define database models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))

    def __repr__(self):
        return f'<Customer {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }

# Create database tables
with app.app_context():
    db.create_all()

# Define API Resources
class CustomerResource(Resource):
    def get(self, customer_id=None):
        if customer_id:
            customer = Customer.query.get_or_404(customer_id)
            return jsonify(customer.to_dict())
        else:
            customers = Customer.query.all()
            return jsonify([customer.to_dict() for customer in customers])

    def post(self):
        data = request.get_json()
        new_customer = Customer(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone', ''),
            address=data.get('address', '')
        )
        db.session.add(new_customer)
        db.session.commit()
        return jsonify(new_customer.to_dict()), 201

    def put(self, customer_id):
        customer = Customer.query.get_or_404(customer_id)
        data = request.get_json()

        customer.name = data.get('name', customer.name)
        customer.email = data.get('email', customer.email)
        customer.phone = data.get('phone', customer.phone)
        customer.address = data.get('address', customer.address)

        db.session.commit()
        return jsonify(customer.to_dict())

    def delete(self, customer_id):
        customer = Customer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return '', 204

# Register API routes
api.add_resource(CustomerResource, '/api/customers', '/api/customers/<int:customer_id>')

# Web routes
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
