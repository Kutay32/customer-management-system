from app import app, db, Customer
import os

# Check if the SQLite database file exists
db_path = 'customer.db'
if os.path.exists(db_path):
    print(f"SQLite database file found at {db_path}")
else:
    print(f"SQLite database file will be created at {db_path}")

# Add sample data to the database
with app.app_context():
    # Clear existing data
    db.session.query(Customer).delete()
    db.session.commit()

    # Add sample customers
    sample_customers = [
        Customer(name="John Doe", email="john@example.com", phone="555-1234", address="123 Main St, New York, NY 10001"),
        Customer(name="Jane Smith", email="jane@example.com", phone="555-5678", address="456 Oak Ave, Los Angeles, CA 90001"),
        Customer(name="Bob Johnson", email="bob@example.com", phone="555-9012", address="789 Pine Rd, Chicago, IL 60601"),
        Customer(name="Alice Brown", email="alice@example.com", phone="555-3456", address="321 Elm Blvd, Houston, TX 77001"),
        Customer(name="Charlie Wilson", email="charlie@example.com", phone="555-7890", address="654 Maple Dr, Phoenix, AZ 85001"),
        Customer(name="Emma Davis", email="emma@example.com", phone="555-2468", address="987 Cedar Ln, Philadelphia, PA 19019"),
        Customer(name="Michael Garcia", email="michael@example.com", phone="555-1357", address="753 Birch St, San Antonio, TX 78201"),
        Customer(name="Sophia Martinez", email="sophia@example.com", phone="555-8642", address="159 Walnut Ave, San Diego, CA 92101"),
        Customer(name="William Rodriguez", email="william@example.com", phone="555-9753", address="357 Cherry Blvd, Dallas, TX 75201"),
        Customer(name="Olivia Lopez", email="olivia@example.com", phone="555-8024", address="246 Spruce Dr, San Jose, CA 95101"),
        Customer(name="James Lee", email="james@example.com", phone="555-6913", address="864 Ash St, Austin, TX 78701"),
        Customer(name="Ava Gonzalez", email="ava@example.com", phone="555-7531", address="975 Fir Ln, Jacksonville, FL 32099"),
        Customer(name="Alexander Perez", email="alex@example.com", phone="555-1593", address="258 Redwood Rd, San Francisco, CA 94101"),
        Customer(name="Mia Sanchez", email="mia@example.com", phone="555-4680", address="369 Sequoia Blvd, Columbus, OH 43085"),
        Customer(name="Benjamin Torres", email="ben@example.com", phone="555-8024", address="147 Sycamore Ave, Indianapolis, IN 46201")
    ]

    for customer in sample_customers:
        db.session.add(customer)

    db.session.commit()
    print(f"Added {len(sample_customers)} sample customers to the database")

    # Verify data was added
    customers = Customer.query.all()
    print("\nCustomers in database:")
    for customer in customers:
        print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")
