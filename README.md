# FastAPI Dockerized Application

## Overview
This is a simple FastAPI application that exposes three endpoints:
- `GET /`: Returns a hello message.
- `GET /users`: Returns a list of users stored in a JSON file (`users.json`).
- `POST /users`: Accepts and stores user data in a JSON file.

This project is dockerized using `Dockerfile` and `docker-compose.yml`, and it stores the user data in a persistent `users.json` file.

## Setup Instructions

### Prerequisites
Ensure that you have the following installed:
- Docker
- Docker Compose

### Running the Application

Clone the repository:
   ```bash
   git clone https://github.com/himanshunagapure/fastapi-dockerized-app.git
   cd docker-fastapi-test
```

Swagger UI: '/' response 

<img width="446" alt="fastapi1" src="https://github.com/user-attachments/assets/e17c816b-6e4e-4ee5-81c1-d2a53d0b3b4e" />

Swagger UI: Create User POST

<img width="371" alt="fastapi2" src="https://github.com/user-attachments/assets/1ac45c1d-7c0c-4ca3-86f7-ffa584102d47" />

SWagger UI: Users List

<img width="266" alt="fastapi3" src="https://github.com/user-attachments/assets/750b055c-abf2-41bf-8e07-bc5f77b034da" />
