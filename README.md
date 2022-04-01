# Test user API

### deploy:
1. Активировать виртуальное окружение с помощью poetry shell.
2. Установить пакеты для подсказок IDE `poetry install`.
3. Запустить контейнеры `docker-compose up`.
4. Войти в контейнер джанго `docker-compose exec app bash
`.
5. Создать админа `./manage.py createsuperuser`.

### API
**Ссылки локальной/дев конфигурации проекта**
- Django-admin: .../admin/
- Silk: .../silk/
- Swagger: .../docs/swagger/
