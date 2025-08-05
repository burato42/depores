# DepoRes

DepoRes is a hobby project designed to provide sports fans with a better interface for viewing advanced statistics for their favorite teams and players. The ultimate goal is to offer a comprehensive platform for sports data analysis, starting with a foundational API.

This is currently a work in progress, with the main focus on building the core functionality for data management.

## Key Features

  * **Asynchronous Backend**: Built with **Python** and **FastAPI**, the backend is fully asynchronous for efficient handling of requests.
  * **Persistent Storage**: Uses **PostgreSQL** for reliable data storage.
  * **Docker-based Setup**: Easy to run and get started with `docker compose`.
  * **Database Migrations**: Manages database schema changes with `alembic`.

## Getting Started

### Prerequisites

You'll need to have **Docker** and **Docker Compose** installed on your machine.

### Local Setup

To get the project up and running locally, simply execute the following command in your terminal from the project's root directory:

```bash
docker compose up
```

This command will build the necessary Docker images, set up the containers, and run the application. The API will be available at `http://localhost:8000`.

## API Endpoints

The following are some of the initial API endpoints available. For a full list and interactive documentation, visit `http://localhost:8000/docs`.

### Get a list of all sports

Retrieve a list of all available sports from the database.

```bash
http GET http://localhost:8000/api/sports
```

**Example Response:**

```json
[
    {
        "id": 1,
        "name": "football"
    },
    {
        "id": 2,
        "name": "basketball"
    }
]
```

-----

### Add a new sport

Create a new sport record by sending a POST request with the sport's name.

```bash
http POST http://localhost:8000/api/sports/new name=tennis
```

**Example Response:**

```json
{
    "id": 3,
    "name": "tennis"
}
```

-----

### Get a sport by ID

Fetch a specific sport record using its unique ID.

```bash
http GET http://localhost:8000/api/sports/2
```

**Example Response:**

```json
{
    "id": 2,
    "name": "basketball"
}
```

## Next Steps

Here's a list of upcoming features and improvements:

  * **Security**: Move sensitive information (like database credentials) to environment variables (`.env`).
  * **Testing**: Implement a comprehensive suite of unit tests to ensure code reliability.
  * **Error Handling**: Enhance error processing for a more robust and user-friendly API.
  * **Admin Panel**: Integrate an admin interface for easier data entry (this will be a proof-of-concept initially, with plans for automated data ingestion later).
  * **Expanded Data Models**: Add more tables to the database (e.g., teams, players, matches, statistics) to build out the full platform.
  * **User Management**: Implement a user authentication and management system.