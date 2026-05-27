# Health App

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
cd PythonEksamen
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running with Docker

The application can be started using Docker Compose.

### Build and start the application the first time:

```bash
docker compose up --build
```

### after the first build, start application with: 

```bash
docker compose up
```

### To stop the containers:

```bash
docker compose down
```

## Environment Variables

The project uses environment variables stored in a `.env` file.

A template file named `.env.example` is included in the project.

Create your own `.env` file based on the example.

You can create your own API keys here:

### Mistral

https://admin.mistral.ai/organization/api-keys

### USDA

https://fdc.nal.usda.gov/api-key-signup


## Tests

The project includes automated tests using pytest.

To run the tests manually:

```bash
cd backend
$ PYTHONPATH=. uv run pytest
```