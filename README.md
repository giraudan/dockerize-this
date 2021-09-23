# dockerize-this

This repo contains a very basic 2-parts Python 3 web application: a front-end named `webapp` and a back-end named `backend`.

Both are based on `CherryPy`.

The backend just replies with a string containing the current date and time when you call `GET /`.

The front-end, when you call `GET /`, calls the backend, makes a simple html page with the backend's reply, and replies with that page.

1. Dockerize the backend
2. Dockerize the front-end
3. Write a `docker-compose.yml` that runs both

When you visit <http://localhost:8080>, you should see a web page with `dockerize-this` as the title, and one paragraph that says something like

> The time now is 2021-09-29 11:51:23
