# Advanced Postman Guide for Customer Management API

This guide provides detailed instructions and tips for efficiently using Postman with the Customer Management API.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Environment Setup](#environment-setup)
3. [Using Dynamic Variables](#using-dynamic-variables)
4. [Automated Testing](#automated-testing)
5. [Collection Runner](#collection-runner)
6. [Workflow Automation](#workflow-automation)
7. [Troubleshooting](#troubleshooting)

## Getting Started

### Importing the Collection and Environment
1. Open Postman
2. Click on "Import" in the top-left corner
3. Select the files:
   - `Customer_Management_API.postman_collection.json`
   - `Customer_Management_API.postman_environment.json`
4. Click "Import" to add them to your workspace

### Initial Setup
1. In the top-right corner, select the "Customer Management API - Local" environment
2. Verify the environment is active (the environment name should be visible)

## Environment Setup

### Understanding Environment Variables
The collection uses two main environment variables:
- `base_url`: The base URL for all API requests (default: http://localhost:5000)
- `customer_id`: Stores the ID of the most recently created customer

### Creating Additional Environments
You can create additional environments for different deployment scenarios:

1. Duplicate the existing environment
2. Rename it (e.g., "Customer Management API - Production")
3. Update the `base_url` value to point to your production server
4. Save the environment

## Using Dynamic Variables

### Built-in Dynamic Variables
The collection uses Postman's dynamic variables to generate random test data:

- `{{$randomFullName}}`: Generates a random person's name
- `{{$randomEmail}}`: Generates a random email address
- `{{$randomPhoneNumber}}`: Generates a random phone number
- `{{$randomStreetAddress}}`, `{{$randomCity}}`, `{{$randomCountry}}`: Generate random address components

### Custom Dynamic Variables
You can create your own dynamic variables in the Pre-request Script tab:

```javascript
// Generate a random customer ID between 1000 and 9999
pm.environment.set("random_id", Math.floor(Math.random() * 9000) + 1000);

// Generate a timestamp-based identifier
pm.environment.set("timestamp_id", Date.now());
```

## Automated Testing

### Understanding the Test Scripts
Each request in the collection includes test scripts that:
1. Verify the HTTP status code is correct
2. Validate the response structure
3. Store relevant data for subsequent requests

### Example: Create Customer Test
```javascript
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Customer created successfully", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('id');
    pm.expect(jsonData).to.have.property('name');
    pm.expect(jsonData).to.have.property('email');
    
    // Store the new customer ID for later use
    if (jsonData.id) {
        pm.environment.set("customer_id", jsonData.id);
    }
});
```

### Adding Custom Tests
You can add your own tests to verify specific business logic:

```javascript
pm.test("Email format is valid", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.email).to.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/);
});
```

## Collection Runner

### Running Multiple Requests in Sequence
1. Click the "Runner" button in Postman
2. Select the "Customer Management API" collection
3. Choose which requests to run (e.g., select "Create Customer" to create multiple customers)
4. Set the number of iterations (how many times to run each request)
5. Click "Run" to execute the requests in sequence

### Data-Driven Testing
You can use a CSV or JSON file to drive your tests with different data:

1. Create a CSV file with test data (e.g., `customers.csv`)
2. In the Collection Runner, click "Select File" and choose your data file
3. Use the data variables in your requests: `{{name}}`, `{{email}}`, etc.

## Workflow Automation

### Creating a Complete Workflow
You can create a workflow that simulates a complete user journey:

1. Get all customers (to see initial state)
2. Create a new customer
3. Get the specific customer by ID
4. Update the customer
5. Delete the customer
6. Verify the customer was deleted

### Running the Workflow
1. In the Collection Runner, select all the requests in the correct order
2. Set iterations to 1
3. Click "Run" to execute the entire workflow

## Troubleshooting

### Common Issues and Solutions

#### 404 Not Found
- Verify the server is running
- Check that the `base_url` environment variable is correct
- Ensure you're using the correct customer ID in the URL

#### 400 Bad Request
- Check the request body format (must be valid JSON)
- Verify all required fields are included
- Check for typos in field names

#### 500 Server Error
- Check the server logs for details
- Verify the database connection is working
- Ensure the server has sufficient resources

### Getting Help
If you encounter issues not covered in this guide:
1. Check the API documentation
2. Look at the server logs for error messages
3. Contact the development team with specific details about the issue