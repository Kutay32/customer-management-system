# Customer Management System - Architectural Documentation

This document outlines the architectural design of the Customer Management System based on the 4+1 architectural model.

## 1. Use Case View

### Primary Actors
- **Administrator**: Manages the customer database
- **API Consumer**: External systems that interact with the API

### Use Cases

#### UC1: Manage Customers
- **Actor**: Administrator
- **Description**: The administrator can view, add, edit, and delete customer records.
- **Flow**:
  1. Administrator accesses the customer management interface
  2. System displays a list of existing customers
  3. Administrator can:
     - View customer details
     - Add a new customer
     - Edit an existing customer
     - Delete a customer

#### UC2: API Integration
- **Actor**: API Consumer
- **Description**: External systems can interact with the customer database through the RESTful API.
- **Flow**:
  1. API Consumer sends a request to one of the API endpoints
  2. System processes the request and performs the requested operation
  3. System returns the appropriate response

### Use Case Diagram
```
    +----------------------+                               +----------------------+
    |       Actor:         |                               |       Actor:         |
    |   Administrator       |                               |    API Consumer      |
    +----------------------+                               +----------------------+
               |                                                   |
               v                                                   v
     +--------------------+                               +-----------------------+
     | Use Case:          |                               | Use Case:             |
     | Manage Customers   |                               | External Integration  |
     +--------------------+                               +-----------------------+
               |                                                   |
               +---------------------------------------------------+
                            Interacts with Customer Management System
```

## 2. Logical View

### Components
- **Web Interface**: Provides a user-friendly interface for administrators
- **RESTful API**: Provides programmatic access to the customer data
- **Database Layer**: Manages data persistence

### Class Diagram
```
+-------------------------+
|       Flask App         |
+-------------------------+
| +handle_request(): void |
+-------------------------+
           |
           v
+-------------------------+                 +--------------------------+
| Customer Resource       |<>------------->|       Customer Model     |
+-------------------------+ composition     +--------------------------+
| +add_customer(): void   |                | - id: int               |
| +edit_customer(): void  |                | - name: string          |
| +delete_customer(): void|                | - email: string         |
| +get_customer(): object |                | - phone: string         |
| +validate_input(): bool |                | +save(): void           |
+-------------------------+                +--------------------------+

               |                                    ^
               |                                    |
               v                                    |
+--------------------------+                       |
|         Database         |-----------------------+ SQL-Based Integration
+--------------------------+
| +perform_query(): result |
+--------------------------+
```

### Component Description
- **Flask App**: The main application that handles HTTP requests and responses
- **Customer Resource**: RESTful resource that implements CRUD operations for customers
- **Customer Model**: Data model representing a customer entity
- **Web Interface**: HTML/CSS/JavaScript frontend for user interaction
- **Database**: SQL Server database for data persistence

## 3. Development View

### Project Structure
```
customer-management-system/
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── instances/              # Database Instances
│   └── customer.db         # Customer Database 
├── templates/              # HTML templates
│   └── index.html          # Main UI template
└── docs/                   # Documentation
    └── architecture.md     # This document
```

### Technology Stack
- **Backend**: Python, Flask, Flask-RESTful, SQLAlchemy
- **Database**: Mysql
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **API**: RESTful architecture

### Development Process
1. Set up the development environment
2. Implement the database models
3. Create the RESTful API endpoints
4. Develop the web interface
5. Test the application
6. Deploy to production

## 4. Process View

### Main Processes
- **HTTP Request Processing**: How the application handles incoming HTTP requests
- **Database Operations**: How the application interacts with the database
- **API Authentication**: How the API validates requests (future enhancement)

### Sequence Diagram for Customer Creation
```
Client                          Flask App                Customer Model      Database
   |                                |                         |                 |
   | POST /customers                |                         |                 |
   |------------------------------->|                         |                 |
   |                                | validate input          |                 |
   |                                |------------------------>|                 |
   |                                |                         | save to DB      |
   |                                |                         |---------------->|
   |                                |                         |   success       |
   |                                |                         |<----------------|
   |  Return HTTP 201               |                         |                 |
   |<-------------------------------|                         |                 |
```

## 5. Physical View

### Deployment Diagram
                +----------------------+        +-------------------------+
                |    Web Browser       |        | SQL Server Database     |
                | (Frontend Interface) |        | (Backend Storage)       |
                +----------------------+        +-------------------------+
                           |                                   |
                           v                                   v
                +---------------------------------------------+
                |               Flask Web Server              |
                | (Handles App Requests + RESTful API Routes) |
                +---------------------------------------------+

### Deployment Considerations
- The application can be deployed on any server that supports Python
- The database can be hosted on a separate server for better performance
- For production, consider using a WSGI server like Gunicorn or uWSGI
- Consider implementing a caching layer for improved performance

## Conclusion

This architecture provides a solid foundation for the Customer Management System, allowing for easy maintenance and future enhancements. The RESTful API design enables integration with other systems, while the web interface provides a user-friendly way to manage customer data.
```
+-------------------------+
|         app.py          |
|  Main Flask Application |
+-------------------------+
         |
         |
+-------------------------+         +--------------------------+
| Customer Resource       |         | API Documentation       |
+-------------------------+         +--------------------------+
| Handles all requests    |         | Includes OpenAPI specs  |
| (CRUD logic)            |         | for integration         |
+-------------------------+         +--------------------------+
         |
+-------------------------+         +--------------------------+
|     Templates           |         |      Static Assets      |
| (HTML Frontend)         |         | (CSS/JavaScript)        |
+-------------------------+         +--------------------------+