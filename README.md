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

1. Clone the repository:
   ```bash
   git clone https://github.com/himanshunagapure/fastapi-dockerized-app.git
   cd docker-fastapi-test
