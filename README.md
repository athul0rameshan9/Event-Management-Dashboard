# Event-Management-Dashboard


###########################################################
# Event Management Backend fast api (python)

This project is a simple event management backend built with FastAPI, SQLAlchemy, and Pydantic. It allows users to create events, register for events, and retrieve event and registration information. The application uses SQLite as the database.

We have user registration and events table. This is a basic event management wewbsite.

## Project Structure

```
event-management-backend
├── app
│   ├── main.py         # Entry point of the application
│   ├── models.py       # SQLAlchemy models for Event and Registration
│   ├── schemas.py      # Pydantic schemas for data validation
│   └── database.py     # Database setup and connection
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Requirements

To run this project, you need to have Python installed. You can install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Running the Application

To start the FastAPI application, navigate to the project directory and run the following command:

```
uvicorn app.main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

- **POST /events/**: Create a new event.
- **GET /events/**: List all events.
- **DELETE /events/{id}**: Delete an event by ID.
- **POST /register/**: Register a user for an event.
- **GET /registrations/**: Retrieve all registrations.

## License

This project is open-source and available under the MIT License.
##########################################################################
