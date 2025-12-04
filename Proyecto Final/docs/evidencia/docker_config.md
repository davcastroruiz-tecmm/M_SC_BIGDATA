# Configuracion de contenedores docker

## 1. Superset
### Construir el container
```bash
cd .\docker\superset
docker build -t  superset .
```

### Usar el docker-compose para pasar la configuracion al container
```bash
docker compose up --build
```

### Crear el usuario inicial
```bash
docker compose exec superset superset fab create-admin --username admin --firstname Admin --lastname User --email admin@example.com --password admin
```

### Hacer upgrade a la base de datos de superset
```bash
docker compose exec superset superset db upgrade
```

### Inicializar base de datos
```bash
docker compose exec superset superset init
```

### Reiniciar el contenedor
```bash
docker compose restart superset
```
Para conectarse a airflow container, en lugar de usar localhost usa:
"""host.docker.internal""" en el puerto 5432 o 5433 dependiendo de tu configuracion
