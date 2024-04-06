# Vue3 & FastAPI WebApp template

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-1c4a6c.svg)](https://flake8.pycqa.org/en/latest/)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

This is a template for a fullstack web application using [Vue3](https://vuejs.org/) and [FastAPI](https://fastapi.tiangolo.com/). It includes a basic example of a web application with a simple API and a frontend that consumes it.

This app template example is a simple web application that allows users to create notes. New notes and deleted notes are broadcasted to all connected clients using web sockets.

## Features

- Modern Frameworks and Tools:

  - [**FastAPI**](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
  - [**Vue3**](https://vuejs.org/): A progressive JavaScript framework for building user interfaces.
    - Router: [**Vue Router**](https://router.vuejs.org/): The official router for Vue.js.
    - State management: [**Pinia**](https://pinia.esm.dev/): A Vue Store that is designed to be used in a modular way.
    - HTTP client: [**Axios**](https://axios-http.com/): Promise based HTTP client for the browser and Node.js.
    - [**Vuetify**](https://vuetifyjs.com/): A Material Design component framework for Vue.js.
    - [**Web sockets**](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API): The backend includes an example of a WebSocket endpoint that the frontend connects to.
  - [**ArangoDB**](https://www.arangodb.com/): A multi-model database system that supports document, key/value, and graph data models.

- Containerization:

  - [**Docker**](https://www.docker.com/): A platform for developing, shipping, and running applications using containerization. This project includes a `Dockerfile` that builds an image of the application.
  - [**Docker Compose**](https://docs.docker.com/compose/): A tool for defining and running multi-container Docker applications. This project includes a `docker-compose.yml` file that defines the services for the frontend and backend.
  - **Configuration with environment variables**: The backend uses environment variables to configure the application.

- Code Quality:

  - [**Black**](https://pypi.org/project/black/) and [**Prettier**](https://prettier.io/): Code formatters that automatically format the code.
  - [**Flake8**](https://flake8.pycqa.org/en/latest/): A tool that checks the code for style and quality.
  - [**Cspell**](https://cspell.org/): A spell checker that checks the spelling in the code, edit the [`cspell.json`](cspell.json) file to add custom words or languages.

- Testing:

  - [**Pytest**](https://docs.pytest.org/): A testing framework for Python that makes it easy to write small tests.

- Continuous Integration and Continuous Deployment:

  - **GitHub Actions**: This project includes a GitHub Actions workflow that runs the tests, linters, pushes the Docker image to the Docker Hub image registry, and deploys the application by calling an SSH script.

## Getting started

### Database prerequisites

- This project uses [ArangoDB](https://www.arangodb.com/) as the database system. You can [install it locally](https://arangodb.com/download-major/docker/) or [use a cloud service](https://cloud.arangodb.com/).

### Development prerequisites

- [Python](https://www.python.org/downloads/) v3.8+
- [Node.js](https://nodejs.org/en/download/) v19.0.0c
- [npm](https://www.npmjs.com/get-npm) v8.19.2

### Production prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Running the application in development mode

1. Clone the repository:

```bash
git clone https://github.com/Tomansion/Vue3-FastAPI-WebApp-template.git
cd Vue3-FastAPI-WebApp-template
```

2. Install the backend and frontend dependencies:

```bash
make install

# Or manually:
cd backend
pip install -r requirements.txt
cd ../frontend
npm install
```

3. Modify the configuration:

Follow the instructions in the [`backend/config/README.md`](backend/config/README.md) file to configure the application.

4. Run the backend and frontend:

```bash
make run

# Or manually:
cd backend
uvicorn websrv:app --reload --host 0.0.0.0 --port 3000

# In another terminal:
cd frontend
npm run serve
```

5. Open the different services in your browser:

- The application frontend: [http://localhost:8080](http://localhost:8080)
- The FastAPI backend: [http://localhost:3000](http://localhost:3000)
- The API SwaggerUI documentation: [http://localhost:3000/docs](http://localhost:3000/docs)
- The API Redoc documentation: [http://localhost:3000/redoc](http://localhost:3000/docs)

### Running the tests

```bash
# Install the test dependencies:
make install_test

# Run the tests:
make test

# Or manually:
cd backend
pytest --cov-report term --cov=. --cov-report=html -sx
firefox htmlcov/index.html
```

### Code quality

This application provide a [Makefile](./makefile) with some commands to help you with the code quality:

```bash
# Format the code with Black and Prettier:
make format

# Check the code with Black, Prettier, Flake8, and cSpell:
make check

# A pipeline is included in the GitHub Actions workflow that runs the linters, so make sure to fix any issues before pushing the code.
```

### Running the application with Docker Compose

```bash
# Clone the repository:
git clone https://github.com/Tomansion/Vue3-FastAPI-WebApp-template.git
cd Vue3-FastAPI-WebApp-template

# Build and run the application with Docker Compose:
docker-compose up --build
```

The application should be available at: [http://localhost:8080](http://localhost:8080)

### Running the application with Docker

```bash
# Clone the repository:
git clone https://github.com/Tomansion/Vue3-FastAPI-WebApp-template.git
cd Vue3-FastAPI-WebApp-template

# Build and run the application with Docker:
docker build -t vue3-fastapi-webapp-template .

# Run the Docker container:
docker run -d -p 3000:3000 vue3-fastapi-webapp-template
```

The application should be available at: [http://localhost:8080](http://localhost:8080).

More information about how to run a Docker image can be found in the [Docker documentation](https://docs.docker.com/get-started/).

### Recommended VSCode extensions

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur)
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
- [cSpell](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

## TODO

- [ ] Add i18n
- [ ] Add demo link
- [ ] Add custom styles
- [ ] Add authentication
- [ ] Add CI/CD pipeline
- [ ] Add frontend tests
- [x] Pinia store
- [x] Arango Database
- [x] Backend tests and coverage
