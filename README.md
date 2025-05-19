# Customer Management System

A simple web application for managing customer information, built with Python, Flask, and Microsoft SQL Server.

## Features

- RESTful API for customer data management
- Web interface for easy interaction
- CRUD operations (Create, Read, Update, Delete)
- Integration with Microsoft SQL Server

## Requirements

- Python 3.8+
- Microsoft SQL Server
- ODBC Driver 17 for SQL Server

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
   - Create a database named `CustomerDB` in Microsoft SQL Server
   - Update the `.env` file with your database connection details if needed

## Running the Application

1. Activate the virtual environment (if not already activated):
   ```
   venv\Scripts\activate
   ```

2. Run the Flask application:
   ```
   flask run
   ```

3. Access the application:
   - Web interface: http://localhost:5000
   - API endpoints: http://localhost:5000/api/customers

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

This project follows the 4+1 architectural model. For detailed architectural documentation, see [docs/architecture.md](docs/architecture.md).

## License

MIT
