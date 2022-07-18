<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Microservice N-Layered Domain Driven Design Template</h3>

  <p align="center">
    Domain Driven Design Template to implement on microservice
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
  </ol>
</details>


<!-- GETTING STARTED -->
## Getting Started 🚀

Setting up these environment constants to execute the microservice.

### Prerequisites ✔️

These are the environment constants to build and run microservice project on staging or test environment.
Production environment needed.

* Environment variables required
  ### ms Envs
  - FLASK_SECRET_KEY=The flask secret key
  - FLASK_APP=Directory to en-route the flask application and config
  - FLASK_ENV=Flask API web framework working environment
  - FLASK_RUN_PORT=Flask API port to run ms API

  - ENVIRONMENT=The environment, can be: "local", "test", "producccion"

  - FERNET_SECRET_KEY=The user's password encrypt secret key

  - CONTENT_TYPE=The content type available to response and request or response API
  - HEADERS=The dictionary to set headers of an API endpoint request

  - CORS_METHOD_GET=It's the HTTP method to accept by the CORS
  - HTTP_METHODS_ALLOW=It's the list of the methods accepted on the CORS
  - ORIGINS=It's the list of the URL host to consider by the CORS

  ### Database Envs
  - DB_NAME=Database name
  - DB_ROOT_USERNAME=Database user
  - DB_ROOT_PASSWORD=Database password
  - MONGODB_HOST=Database host
  - MONGODB_PORT=Database port
  - MONGO_CLUSTER_CONN=URL to MongoDB database server



Make with ❤️ by Jorge Morfinez Mojica
