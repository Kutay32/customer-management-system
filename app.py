from flask import Flask, request, render_template
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import os
import re
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

# Validation helpers
EMAIL_REGEX = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

def validate_customer_payload(data, existing_customer=None):
    errors = {}
    name = (data.get('name') or '').strip()
    email = (data.get('email') or '').strip()

    if not name:
        errors['name'] = 'Name is required.'
    if not email:
        errors['email'] = 'Email is required.'
    elif not EMAIL_REGEX.match(email):
        errors['email'] = 'Email must be a valid address.'

    if email:
        existing = Customer.query.filter_by(email=email)
        if existing_customer:
            existing = existing.filter(Customer.id != existing_customer.id)
        if existing.first():
            errors['email'] = 'Email already exists.'

    return errors, name, email

# Create database tables
with app.app_context():
    db.create_all()

# Define API Resources
class CustomerResource(Resource):
    def get(self, customer_id=None):
        if customer_id:
            customer = Customer.query.get_or_404(customer_id)
            return customer.to_dict()
        else:
            search = request.args.get('search', '').strip()
            sort_by = request.args.get('sort_by', 'name')
            sort_dir = request.args.get('sort_dir', 'asc')
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            per_page = max(1, min(per_page, 100))

            query = Customer.query
            if search:
                like = f"%{search}%"
                query = query.filter(
                    or_(
                        Customer.name.ilike(like),
                        Customer.email.ilike(like),
                        Customer.phone.ilike(like),
                        Customer.address.ilike(like)
                    )
                )

            sort_options = {
                'id': Customer.id,
                'name': Customer.name,
                'email': Customer.email,
                'phone': Customer.phone,
                'address': Customer.address
            }
            sort_column = sort_options.get(sort_by, Customer.name)
            if sort_dir == 'desc':
                query = query.order_by(sort_column.desc())
            else:
                query = query.order_by(sort_column.asc())

            pagination = query.paginate(page=page, per_page=per_page, error_out=False)

            return {
                'items': [customer.to_dict() for customer in pagination.items],
                'page': page,
                'per_page': per_page,
                'total': pagination.total,
                'pages': pagination.pages
            }

    def post(self):
        data = request.get_json(silent=True) or {}
        errors, name, email = validate_customer_payload(data)

        if errors:
            return {'errors': errors}, 400

        new_customer = Customer(
            name=name,
            email=email,
            phone=(data.get('phone') or '').strip(),
            address=(data.get('address') or '').strip()
        )
        db.session.add(new_customer)
        db.session.commit()
        return new_customer.to_dict(), 201

    def put(self, customer_id):
        customer = Customer.query.get_or_404(customer_id)
        data = request.get_json(silent=True) or {}
        if not data:
            return {'message': 'No update data provided.'}, 400

        name = (data.get('name', customer.name) or '').strip()
        email = (data.get('email', customer.email) or '').strip()
        errors = {}

        if not name:
            errors['name'] = 'Name is required.'
        if not email:
            errors['email'] = 'Email is required.'
        elif not EMAIL_REGEX.match(email):
            errors['email'] = 'Email must be a valid address.'
        elif email != customer.email:
            if Customer.query.filter_by(email=email).first():
                errors['email'] = 'Email already exists.'

        if errors:
            return {'errors': errors}, 400

        customer.name = name
        customer.email = email
        customer.phone = (data.get('phone', customer.phone) or '').strip()
        customer.address = (data.get('address', customer.address) or '').strip()

        db.session.commit()
        return customer.to_dict()

    def delete(self, customer_id):
        customer = Customer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return '', 204

class CustomerStatsResource(Resource):
    def get(self):
        total = Customer.query.count()
        with_phone = Customer.query.filter(Customer.phone.isnot(None), Customer.phone != '').count()
        with_address = Customer.query.filter(Customer.address.isnot(None), Customer.address != '').count()

        return {
            'total': total,
            'with_phone': with_phone,
            'with_address': with_address
        }

# Register API routes
api.add_resource(CustomerResource, '/api/customers', '/api/customers/<int:customer_id>')
api.add_resource(CustomerStatsResource, '/api/customers/stats')

# Web routes
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Get host and port from environment variables with defaults
    # 0.0.0.0 makes the app publicly accessible
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'True').lower() == 'true'

    app.run(host=host, port=port, debug=debug)
