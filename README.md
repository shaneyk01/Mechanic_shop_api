# Mechanic Shop API

A RESTful API for managing a mechanic shop's operations, including customers, mechanics, and service tickets. Built with Flask, SQLAlchemy, and MySQL.

## Features

- **Customer Management**: Create, read, update, and delete customer records
- **Mechanic Management**: Manage mechanic information and assignments
- **Service Ticket Management**: Track service requests and assign mechanics to tickets
- **Many-to-Many Relationships**: Assign multiple mechanics to service tickets
- **Data Validation**: Input validation using Marshmallow schemas
- **RESTful Design**: Clean, intuitive API endpoints following REST principles

## Technology Stack

- **Framework**: Flask (Python web framework)
- **ORM**: SQLAlchemy with Flask-SQLAlchemy
- **Database**: MySQL
- **Serialization**: Flask-Marshmallow
- **Validation**: Marshmallow schemas
- **Database Connector**: mysql-connector-python

## Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shaneyk01/Mechanic_shop_api.git
   cd Mechanic_shop_api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy mysql-connector-python
   ```

## Database Setup

1. **Create MySQL database**
   ```sql
   CREATE DATABASE mechanic_shop_api;
   ```

2. **Update configuration**
   Edit `config.py` and update the database connection string:
   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/mechanic_shop_api'
   ```

3. **Initialize the database**
   The application will automatically create tables when you run it for the first time.

## Running the Application

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5001`

## API Documentation

### Base URL
```
http://127.0.0.1:5001
```

### Customers Endpoints

#### Create a Customer
- **URL**: `/customers/`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "123-456-7890",
    "password": "securepassword"
  }
  ```
- **Success Response**: `201 Created`

#### Get All Customers
- **URL**: `/customers/`
- **Method**: `GET`
- **Success Response**: `200 OK`

#### Get Customer by ID
- **URL**: `/customers/<customer_id>`
- **Method**: `GET`
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`

#### Update Customer
- **URL**: `/customers/<customer_id>`
- **Method**: `PUT`
- **Body**: Same as Create Customer
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`

#### Delete Customer
- **URL**: `/customers/<customer_id>`
- **Method**: `DELETE`
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`

### Mechanics Endpoints

#### Create a Mechanic
- **URL**: `/mechanics/`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "name": "Jane Smith",
    "email": "jane@example.com",
    "phone": "098-765-4321",
    "salary": "50000"
  }
  ```
- **Success Response**: `201 Created`

#### Get All Mechanics
- **URL**: `/mechanics/`
- **Method**: `GET`
- **Success Response**: `200 OK`

#### Update Mechanic
- **URL**: `/mechanics/<mechanic_id>`
- **Method**: `PUT`
- **Body**: Same as Create Mechanic
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`

#### Delete Mechanic
- **URL**: `/mechanics/<mechanic_id>`
- **Method**: `DELETE`
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`

### Service Tickets Endpoints

#### Create a Service Ticket
- **URL**: `/tickets/`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "ticket_date": "2024-01-15",
    "service_desc": "Oil change and tire rotation",
    "customer_id": 1
  }
  ```
- **Success Response**: `201 Created`

#### Get All Tickets
- **URL**: `/tickets/`
- **Method**: `GET`
- **Success Response**: `200 OK`

#### Get Ticket by ID
- **URL**: `/tickets/<ticket_id>`
- **Method**: `GET`
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`

#### Add Mechanic to Ticket
- **URL**: `/tickets/<ticket_id>/add-mechanic/<mechanic_id>`
- **Method**: `PUT`
- **Success Response**: `200 OK`

#### Remove Mechanic from Ticket
- **URL**: `/tickets/<ticket_id>/remove-mechanic/<mechanic_id>`
- **Method**: `PUT`
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`

## Project Structure

```
Mechanic_shop_api/
├── app/
│   ├── __init__.py              # Application factory
│   ├── extensions.py            # SQLAlchemy and Marshmallow instances
│   ├── models.py                # Database models (Customer, Mechanic, Service_tickets)
│   └── blueprints/
│       ├── customer/
│       │   ├── __init__.py
│       │   ├── routes.py        # Customer endpoints
│       │   └── schemas.py       # Customer serialization
│       ├── mechanics/
│       │   ├── __init__.py
│       │   ├── routes.py        # Mechanic endpoints
│       │   └── schemas.py       # Mechanic serialization
│       └── service_tickets/
│           ├── __init__.py
│           ├── routes.py        # Service ticket endpoints
│           └── schemas.py       # Service ticket serialization
├── app.py                       # Application entry point
├── config.py                    # Configuration settings
└── MNECHANIC SHOP.postman_collection.json  # Postman collection for testing
```

## Database Schema

### Tables

1. **customers**
   - `customer_id` (Primary Key)
   - `name`
   - `email`
   - `phone`
   - `password`

2. **mechanics**
   - `mechanic_id` (Primary Key)
   - `name`
   - `email`
   - `phone`
   - `salary`

3. **tickets**
   - `ticket_id` (Primary Key)
   - `ticket_date`
   - `service_desc`
   - `customer_id` (Foreign Key → customers)

4. **ticket_mechanics** (Junction Table)
   - `ticket_id` (Foreign Key → tickets)
   - `mechanic_id` (Foreign Key → mechanics)

### Relationships

- A **Customer** can have multiple **Service Tickets** (One-to-Many)
- A **Service Ticket** belongs to one **Customer** (Many-to-One)
- **Mechanics** and **Service Tickets** have a Many-to-Many relationship

## Configuration

The application uses different configurations for different environments:

- **DevelopmentConfig**: For local development with debug mode enabled
- **TestingConfig**: For running tests (to be implemented)
- **ProductionConfig**: For production deployment (to be implemented)

To change the configuration, modify the argument in `app.py`:
```python
app = create_app("DevelopmentConfig")  # or "TestingConfig" or "ProductionConfig"
```

## Testing

A Postman collection is included (`MNECHANIC SHOP.postman_collection.json`) for testing all API endpoints. Import this collection into Postman to get started with testing the API.

## Error Handling

The API returns appropriate HTTP status codes:

- `200 OK`: Successful GET, PUT, DELETE requests
- `201 Created`: Successful POST requests
- `400 Bad Request`: Invalid input or validation errors
- `404 Not Found`: Resource not found

Error responses include JSON with descriptive error messages.

## Future Enhancements

- [ ] Add authentication and authorization
- [ ] Implement password hashing for customer accounts
- [ ] Add pagination for list endpoints
- [ ] Implement search and filtering capabilities
- [ ] Add unit and integration tests
- [ ] Create API documentation with Swagger/OpenAPI
- [ ] Add logging functionality
- [ ] Implement rate limiting
- [ ] Add email notifications for ticket updates

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is available for educational purposes.

## Author

Shane YK

## Acknowledgments

- Flask documentation
- SQLAlchemy documentation
- Marshmallow documentation
