# Customer Management System Project 
  ```
   Team
   Kutay Orallı - 220911791
   Berk Günberk - 220911759
   Eyüpcan Işıkgör - 210911023
   Beril Çitil - 210911031
  ```
## Oversight
A simple web application for managing customer information, built with Python, Flask, and MySQL.

## Features

- RESTful API for customer data management
- Web interface for easy interaction
- CRUD operations (Create, Read, Update, Delete)
- Integration with MySQL (with SQLite fallback option)

## Requirements

- Python 3.8+
- MySQL (or SQLite for development)
- PyMySQL

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Kutay32/customer-management-system.git
   cd customer-management-system
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure the database:
   - For MySQL: Create a database named `CustomerDB` in MySQL
   - Update the `.env` file with your database connection details:
     ```
     # For MySQL
     DATABASE_URL=mysql+pymysql://username:password@localhost/CustomerDB

     # Or for SQLite (default for development)
     DATABASE_URL=sqlite:///customer.db
     ```

## Running the Application

1. Activate the virtual environment (if not already activated):
   ```
   venv\Scripts\activate
   ```

2. Run the Flask application:
   ```
   # For local development
   flask run

   # For public access
   python app.py
   ```

3. Access the application:
   - Local development:
     - Web interface: http://localhost:5000
     - API endpoints: http://localhost:5000/api/customers

   - Public access:
     - Web interface: http://your-ip-address:5000
     - API endpoints: http://your-ip-address:5000/api/customers

   Note: Replace `your-ip-address` with your actual IP address or domain name.

4. Configuration (via .env file):
   - `HOST`: Set to `0.0.0.0` for public access or `127.0.0.1` for local-only access
   - `PORT`: Default is `5000`, change as needed
   - `DEBUG`: Set to `True` for development or `False` for production

## Production Deployment(For Public Website)

For deploying this application in a production environment, consider the following recommendations:

1. Use a WSGI server:
   ```
   # Install Gunicorn
   pip install gunicorn

   # Run with Gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

   Or with uWSGI:
   ```
   # Install uWSGI
   pip install uwsgi

   # Run with uWSGI
   uwsgi --http 0.0.0.0:5000 --module app:app --processes 4
   ```

2. Security considerations:
   - Set `DEBUG=False` in your .env file
   - Consider implementing API authentication for public deployments
   - Use HTTPS for secure communication
   - Consider using a reverse proxy like Nginx or Apache

3. Database considerations:
   - For production, consider using a more robust database like MySQL or PostgreSQL
   - Update the DATABASE_URL in your .env file accordingly

## API Endpoints

- `GET /api/customers` - Get all customers
- `GET /api/customers/<id>` - Get a specific customer
- `POST /api/customers` - Create a new customer
- `PUT /api/customers/<id>` - Update a customer
- `DELETE /api/customers/<id>` - Delete a customer

## Testing with Postman

1. Download and install [Postman](https://www.postman.com/downloads/)
2. Import the provided Postman collection and environment:
   - Click on "Import" in Postman
   - Select the files `Customer_Management_API.postman_collection.json` and `Customer_Management_API.postman_environment.json`
   - Click "Import" to add them to your workspace

3. Set up the environment:
   - In the top-right corner of Postman, select the "Customer Management API - Local" environment
   - This will automatically use the correct base URL for all requests

4. Use the collection efficiently:
   - **Get all customers**: Retrieves all customer records
   - **Get Customer by ID**: Retrieves a specific customer (uses the `customer_id` environment variable)
   - **Create Customer**: Creates a new customer with randomly generated data using Postman's dynamic variables
   - **Update Customer**: Updates an existing customer (uses the `customer_id` from the previous create operation)
   - **Delete Customer**: Removes a customer (uses the `customer_id` environment variable)
   - **Bulk Create Customers**: Use this with the Collection Runner to create multiple customers quickly

5. Advanced features:
   - **Automatic testing**: Each request includes tests that validate the response
   - **Environment variables**: The collection automatically stores the ID of newly created customers
   - **Dynamic data generation**: Uses Postman's built-in variables like `{{$randomFullName}}` and `{{$randomEmail}}` to generate test data
   - **Collection Runner**: Run multiple requests in sequence for efficient testing

   For detailed instructions and advanced usage tips, see the [Advanced Postman Guide](docs/postman_guide.md)

6. Example request (Create Customer):
   ```json
   {
     "name": "{{$randomFullName}}",
     "email": "{{$randomEmail}}",
     "phone": "{{$randomPhoneNumber}}",
     "address": "{{$randomStreetAddress}}, {{$randomCity}}, {{$randomCountry}}"
   }
   ```

## Project Structure

```
customer-management-system/
├── app.py                                      # Main application file
├── requirements.txt                            # Python dependencies
├── .env                                        # Environment variables
├── Customer_Management_API.postman_collection.json  # Postman collection for API testing
├── Customer_Management_API.postman_environment.json # Postman environment variables
├── templates/                                  # HTML templates
│   └── index.html                              # Main UI template
├── static/                                     # Static assets
│   └── css/                                    # CSS stylesheets
│       └── styles.css                          # Main stylesheet
└── docs/                                       # Documentation
    ├── architecture.md                         # Architectural documentation
    └── postman_guide.md                        # Advanced Postman usage guide
```

## Architecture

This project follows the 4+1 architectural model as requested. For detailed architectural documentation, see [docs/architecture.md](docs/architecture.md).

## License

MIT
