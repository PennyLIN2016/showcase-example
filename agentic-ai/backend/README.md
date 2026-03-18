# Backend FastAPI Application

This directory contains the backend implementation of the agentic application using FastAPI. The backend is responsible for handling incoming requests, processing them through various agents, and interacting with the database.

## Project Structure

- **app/**: Contains the main application code.
  - **main.py**: Entry point of the FastAPI application.
  - **api/**: Contains the API routes and health check.
    - **routes.py**: Defines the API routes for handling requests.
    - **health.py**: Provides a health check endpoint.
  - **agents/**: Contains the logic for the agents.
    - **planner.py**: Implements the planning agent.
    - **task_agent.py**: Implements the task agent.
  - **core/**: Contains core functionalities.
    - **config.py**: Manages configuration settings.
    - **llm_client.py**: Interacts with the OpenAI LLM.
  - **db/**: Contains database-related code.
    - **database.py**: Manages database connection and setup.
    - **repository.py**: Contains functions for database interactions.
  - **models/**: Defines data models.
    - **customer.py**: Represents the customer data structure.
  - **schemas/**: Defines request and response schemas.
    - **request_schema.py**: Validates incoming requests.
    - **response_schema.py**: Formats outgoing responses.

## Setup Instructions

1. **Install Dependencies**: Navigate to the `backend` directory and run:
   ```
   pip install -r requirements.txt
   ```

2. **Configuration**: Update the `config/config.yaml` file with the necessary parameters, including the path to the `customers-1000.csv` database.

3. **Run the Application**: Start the FastAPI application by running:
   ```
   uvicorn app.main:app --reload
   ```

4. **Access the API**: The API will be available at `http://localhost:8000`. You can check the health endpoint at `http://localhost:8000/health`.

## Docker Support

To run the backend application using Docker, build the Docker image with:
```
docker build -t agentic-fastapi .
```
Then, run the container:
```
docker run -p 8000:8000 agentic-fastapi
```

## Additional Notes

- Ensure that the OpenAI API key and other sensitive information are managed securely, possibly using environment variables.
- The frontend application is located in the `frontend` directory and communicates with this backend via the defined API routes.
