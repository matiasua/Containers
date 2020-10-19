# ReactJS + Flask (REST API) + PostgreSQL con Docker

Este proyecto permite ejecutar una aplicación rápida con ReactJS (front-end), Flask (backend Python) y PostgreSQL (base de datos relacional) ejecutándolo en contenedores Docker.

### Run the app

Todo está en contenedores desde el frontend, backend a la base de datos, todo lo que necesita es Docker instalado y luego puede ejecutar:

```
docker-compose up --build
```

La aplicacion cliente estara activa en el _puerto 3000_
La aplicacion backend estara activa en el _puerto 8084_

### Notas Especiales

- Este proyecto se implemento con Docker Desktop.
- En esta primera iteracion se creo el contenedor cliente con el proyecto inicial de react js.
- Todavia no existe una comunicacion entre el frontend y el backend.
- Las consultas a los endpoints se pueden realizar mediante POSTMAN 'http://localhost:8084'.
- Antes de realizar consultas se debe hacer el upgrade de la base de datos con el siguiente comando:

```
docker container exec [NAME CONTAINER] flask db upgrade
```

- Quedo pendiente para la segunda iteracion los Testing y la integracion continua del proyecto.
