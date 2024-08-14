# Vue3 & FastAPI WebApp template

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-1c4a6c.svg)](https://flake8.pycqa.org/en/latest/)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

![ci](https://github.com/tomansion/Vue3-FastAPI-WebApp-template/actions/workflows/pull-request-checks.yml/badge.svg)
![cd](https://github.com/tomansion/Vue3-FastAPI-WebApp-template/actions/workflows/continuous-deployment.yml/badge.svg)

---

This project is a template for a fullstack web application using [Vue3](https://vuejs.org/) and [FastAPI](https://fastapi.tiangolo.com/). It includes a basic example of a web application with a simple API and a frontend that consumes it, a simple web application that allows users to create notes. New notes and deleted notes are broadcasted to all connected clients using web sockets.

![](Easy%20notes.png)

<div align="center">
  <b>
  <a href="https://easynotes.tomansion.fr/">Live demo</br>https://easynotes.tomansion.fr/</a>
  </b>
</div>

## Template features

- Modern Frameworks and Tools:

  - [**FastAPI**](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
    - [**Web sockets**](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API): The backend includes an example of a WebSocket endpoint that the frontend connects to.q
  - [**Vue3**](https://vuejs.org/): A progressive JavaScript framework for building user interfaces.
    - Router: [**Vue Router**](https://router.vuejs.org/): The official router for Vue.js.
    - State management: [**Pinia**](https://pinia.esm.dev/): A Vue Store that is designed to be used in a modular way.
    - HTTP client: [**Axios**](https://axios-http.com/): Promise based HTTP client for the browser and Node.js.
    - [**Vuetify**](https://vuetifyjs.com/): A Material Design component framework for Vue.js.
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

### Running the application in development mode

#### Prerequisites

- [Python](https://www.python.org/downloads/) v3.9+ for the backend.
- [Node.js](https://nodejs.org/en/download/) v19.0.0c and [npm](https://www.npmjs.com/get-npm) v8.19.2 for the frontend.
- A running [ArangoDB](https://www.arangodb.com/) instance. [Install it locally](https://arangodb.com/download-major/docker/) or [use a cloud service](https://cloud.arangodb.com/).

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

Follow the instructions in the [`backend/config/README.md`](backend/config/README.md).
Modifying the configuration is required to give the application access to the ArangoDB instance.

4. Run the backend and frontend:

```bash
make run

# Or manually:
cd backend
uvicorn websrv:app --reload --host 0.0.0.0 --port 3000
cd frontend # In another terminal
npm run serve
```

```bash
# Backend expected output
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [125657] using WatchFiles
No build directory found. Running in development mode.

Initializing configuration...
 - Set NOTES / NOTES_NUMBER_MAX
 - Set NOTES / NOTES_TITLE_LENGTH_MAX
 - Set NOTES / NOTES_CONTENT_LENGTH_MAX
 - Set ARANGODB / HOST
 - Set ARANGODB / PORT
 - Set ARANGODB / DATABASE
 - Set ARANGODB / USER
 - Set ARANGODB / PASSWORD

Connecting to ArangoDB...
 - Host: ***
 - Port: ***
 - Database: WebAppTemplate
 - User: WebAppTemplate
 - Connection to Arango Arango 3.11.5 established

Running FastAPI app...
 - FastAPI is available at http://localhost:3000/api
 - Swagger UI is available at http://localhost:3000/docs
 - Redoc is available at http://localhost:3000/redoc

INFO:     Started server process [125659]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
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

```bash
# Expected output
Name                         Stmts   Miss  Cover
------------------------------------------------
config/init_config.py           51     14    73%
services/notes_services.py      36      0   100%
utils/database_utils.py         76      6    92%
------------------------------------------------
TOTAL                          163     20    88%

============= 10 passed in 1.52s ===============
# The detailed coverage report wil be available in the `htmlcov` directory.
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

### Running the application with [Docker Compose](https://docs.docker.com/compose/)

```bash
# Clone the repository:
git clone https://github.com/Tomansion/Vue3-FastAPI-WebApp-template.git
cd Vue3-FastAPI-WebApp-template

# Set the docker-compose environment variables
# More information in the backend/config/config.env file
nano docker-compose.yml

# Build and run the application with Docker Compose:
docker-compose up --build
```

The application should be available at: [http://localhost:3000](http://localhost:3000)

### Setting up the GitHub continuous deployment pipeline

This project includes a GitHub Actions workflow that builds the Docker image, pushes it to the Docker Hub image registry, and deploys the application by calling an SSH script.

#### Prerequisites

- A Linux server with Docker and Docker Compose installed.
- A [Docker Hub](https://hub.docker.com/) account.

#### Steps

1. Create a new repository from this template and push it to GitHub.
2. Copy and edit the [`docker-compose.yml`](docker-compose.yml) file to your server.
   - Edit the images to point to your Docker Hub repository.
   - Edit the environment variables to match your configuration.
   - Edit the container names and the other configurations as needed.
   - Add your Nginx or Traefik configuration if needed.
3. Create, on your server a `deploy.sh` script with the following content:

```bash
# deploy.sh
cd /path/to/your/application
docker-compose pull
docker-compose up -d
# Use chmod +x deploy.sh to make the script executable
```

4. Add the following secrets to your repository:
   - `DOCKER_USERNAME`: Your Docker Hub username.
   - `DOCKER_PASSWORD`: Your Docker Hub password.
   - `SSH_HOST`: The IP address of the server where you want to deploy the application.
   - `SSH_PORT`: The port to connect to the server.
   - `SSH_USERNAME`: The username to connect to the server.
   - `SSH_PASSWORD`: The user password to connect to the server.
   - `SSH_SCRIPT_PATH`: The absolute path to the `deploy.sh` script on the server.
5. Modify the `APP_NAME`in the [continuous-deployment.yml](./.github/workflows/continuous-deployment.yml) file to match your application name.
6. Push the changes to your repository.

The GitHub Actions workflow will run when you push the changes to the repository `main` branch. It will build the Docker image, push it to the Docker Hub image registry, and deploy the application by calling the `deploy.sh` script on your server.

### Recommended VSCode extensions

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur)
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
- [cSpell](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

## Help

If you have any questions or need help, feel free to [open an issue](https://github.com/Tomansion/Vue3-FastAPI-WebApp-template/issues).

## Contributing

I'm open to contributions and suggestions. Feel free to [open an issue](https://github.com/Tomansion/Vue3-FastAPI-WebApp-template/issues) or a make a pull request.

## TODO

- [ ] Generate `config.ini.example` and `config.env` files automatically 
- [ ] Custom styles
- [ ] I18n
- [ ] Documentation
- [ ] Authentication
- [ ] Frontend tests
- [ ] Frontend to mobile app
- [x] CI/CD pipeline
- [x] Demo link
- [x] Pinia store
- [x] Arango Database
- [x] Backend tests and coverage
