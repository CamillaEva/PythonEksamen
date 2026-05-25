# Health app

A full-stack meal tracking application built with FastAPI and Python.  
The project includes a backend REST API, a frontend interface, automated testing with pytest, and Docker support using Docker Compose.


## Features

- Create meals
- Retrieve all meals
- Update meals
- Delete meals
- Store data in CSV format
- Automated testing with pytest


## Installation

Clone the repository:

```bash
git clone https://github.com/CamillaEva/PythonEksamen


### Running with Docker

the application can be started using Docker Compose

### start the application:

```bash
docker compose up --build


### to stop the containers:

```bash
docker compose down


## Environment Variables

The project uses environment variables stored in a `.env` file.

A template file named `.env.example` is included in the project.

Create your own `.env` file based on the example.

you can create your own api keys here:

Mistral: https://admin.mistral.ai/organization/api-keys

USDA: https://fdc.nal.usda.gov/api-key-signup
