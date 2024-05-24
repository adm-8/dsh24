# Подняте риложки
```bash
docker compose up -d
```

# Перезапуск с очисткой данных и пересозданием схемы БД
```bash
docker rm -f dsh24-bot_db-1
docker volume rm -f dsh24_bot-db-data
docker compose up -d 
```
