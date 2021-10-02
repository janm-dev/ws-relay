# ws.janm.dev

This is the WebSocket relay server used by qna.

The qna web app is available on [https://github.com/janm-dev/qna](https://github.com/janm-dev/qna).

## Running locally

### With Docker

0. Make sure [Docker](https://www.docker.com/) is installed. Start Docker Engine.
1. Run `docker run -p 4000:80 janmdev/ws-relay`. This will download and start the ws-relay Docker container on port 4000. You can check by visiting [http://localhost:4000/healthcheck](http://localhost:4000/healthcheck), which should respond with `OK` and [a number](https://en.wikipedia.org/wiki/Unix_time).

### With Docker (from source)

0. Make sure [Docker](https://www.docker.com/) is installed. [Clone this repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository). Start Docker Engine.
1. In the root directory of this project, run `docker build -t ws-relay .` to build the Docker container.
2. Run `docker run -p 4000:80 ws-relay`. This will start the ws-relay Docker container on port 4000. You can check by visiting [http://localhost:4000/healthcheck](http://localhost:4000/healthcheck), which should respond with `OK` and [a number](https://en.wikipedia.org/wiki/Unix_time).

### Without docker (recommended for development)

0. Make sure [Python 3](https://www.python.org/) is installed. [Clone this repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
1. In the root directory of this project, run `pip install -r requirements.txt` or `python -m pip install -r requirements.txt` to install all dependencies.
2. Run `uvicorn --port 4000 --reload relay:relay` or `python -m uvicorn --port 4000 --reload relay:relay`. This will start ws-relay on port 4000. You can check by visiting [http://localhost:4000/healthcheck](http://localhost:4000/healthcheck), which should respond with `OK` and [a number](https://en.wikipedia.org/wiki/Unix_time).

## License

This project is licensed under the GNU AGPLv3 or later (`AGPL-3.0-or-later`). You can find the full license text in the LICENSE file.
