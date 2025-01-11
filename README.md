# FastAPI Dockerized Application

## Overview
This is a simple FastAPI application that exposes three endpoints:
- `GET /`: Returns a hello message.
- `GET /users`: Returns a list of users stored in a JSON file (`users.json`).
- `POST /users`: Accepts and stores user data in a JSON file.

This project is dockerized using `Dockerfile` and `docker-compose.yml`, and it stores the user data in a persistent `users.json` file.

## Project Structure
<img width="343" alt="project-structure" src="https://github.com/user-attachments/assets/3349194b-3060-41d4-9aac-da4603f95326" />

### Project Files Explained

- Dockerfile: Contains instructions for building the Docker image.

- docker-compose.yml: Defines the services for running the application and ensures the data directory is mounted for persistence.

- app/main.py: Contains the FastAPI application logic.

- app/schema.py: Defines the data models.

- app/services.py: Contains business logic.

- app/data/info.txt: Placeholder file in the data directory.

- requirements.txt: Lists the Python dependencies.

- .gitignore: Specifies files to be excluded from version control.

---

## Setup Instructions
### Prerequisites
Ensure that you have the following installed:
- Docker
- Docker Compose

### Running the Application

Step 1: Clone the repository:
   ```bash
   git clone https://github.com/himanshunagapure/fastapi-dockerized-app.git
   cd docker-fastapi-test
   ```
Step 2: Build and Run the Application
   ```bash
   docker-compose up --build
   ```
This will build the Docker image and run the container.

Step 3: Access the Application

- Open Swagger UI: http://localhost:8000/docs
- Open API root endpoint: http://localhost:8000

Step 4: Test API Endpoints

Example Swagger UI results : 

Swagger UI: '/' response 

<img width="446" alt="fastapi1" src="https://github.com/user-attachments/assets/e17c816b-6e4e-4ee5-81c1-d2a53d0b3b4e" />

Swagger UI: POST /users

<img width="371" alt="fastapi2" src="https://github.com/user-attachments/assets/1ac45c1d-7c0c-4ca3-86f7-ffa584102d47" />

GET /users

<img width="266" alt="fastapi3" src="https://github.com/user-attachments/assets/750b055c-abf2-41bf-8e07-bc5f77b034da" />

Step 5: Stop the Application

To stop the containers, run
   ```bash
   docker-compose down
   ```
---

## Data Persistence

The user data is stored in a users.json file inside the data directory. The data persists even when the containers are stopped and restarted.

### To test data persistence:

1. Run the app and add a user via the /users POST endpoint.

2. Stop the containers using docker-compose down.

3. Restart using docker-compose up.

4. Check the /users endpoint to verify the previously added data still exists.

---

## Contributing

Feel free to fork the repository and submit a pull request for improvements or additional features.

---

## License

This project is licensed under the MIT License.

---

## Author

Himanshu Nagapure
