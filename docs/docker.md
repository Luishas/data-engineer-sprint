# Docker — PostgreSQL

## Levantar la base de datos
docker compose up -d

## Ver que está corriendo
docker ps

## Conectarse
psql -h localhost -p 5433 -U postgres -d data_engineer_sprint

## Detener (conserva los datos, gracias al volumen)
docker compose down

## Detener Y borrar los datos (usar con cuidado)
docker compose down -v