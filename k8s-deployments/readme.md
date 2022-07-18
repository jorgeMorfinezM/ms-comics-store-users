## Explicit is better than implicit. Simple is better than complex.

> Run this from the root, this is just an example of what you should do there

* Build

  ```sh
  docker build -t ms-comics-store-users -f k8s-deployments/Dockerfile .
  ```

* Run

  ```sh
  docker run -p 9000:9000  --env-file=.env ms-comics-store-users   
  ```