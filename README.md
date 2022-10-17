### Используя DRF (Django Rest Framework) разработать REST-сервис для управления виртуальными серверами (VPS).

#### Объект VPS
- uid - идентификатор
- cpu - количество ядер
- ram - объем RAM
- hdd - объем HDD
- status - статус сервера (started, blocked, stopped)

#### API поддерживает операции
- создать VPS
- получить VPS по uid
- получить список VPS с возможностью фильтрации по параметрам
- перевести VPS в другой статус

### Развертывание
`Перед развертыванием автоматически прогоняются тесты`
1. Собрать контейнер `docker-compose build`
2. Запустить контейнер `docker-compose up`

