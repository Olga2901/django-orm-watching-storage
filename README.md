# Пульт охраны банка

Программа для работы с пропускной системой в хранилище банка.

## Установка и запуск

1. Python3 должен быть уже установлен.

2. Клонируйте репозиторий.

3. Создайте виртуальное окружение. Пример:
```
mkdir project
cd project
python -m venv env
cd Python311\project\env\Scripts\activate.bat
```
4. Используйте `pip` (или `pip3`, если конфликт с Python2) для установки зависимостей.
```
pip install -r requirements.txt
```
5. Создайте файл `.env` с переменными окружения. Пример:
```
- DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
- SECRET_KEY=your_secret_key
- DEBUG=False
- ALLOWED_HOSTS=localhost
- USE_L10N=True
- LANGUAGE_CODE=ru-ru
- TIME_ZONE=Europe/Moscow
- USE_TZ=True
```
6. Запустите сервер командой.
```
python manage.py runserver 0.0.0.0:8000
```

## Использование

После запуска 'пульт' доступен по адресу: http://127.0.0.1:8000 и состоит из трех cтраниц:
1. Список всех кодов доступа. доступна по адресу: http://127.0.0.1:8000/active_passcards
2. Список находящихся в данный момент пользователей в хранилище. Доступна по адресу: http://127.0.0.1:8000/storage_information
3. Список всех визитов каждого владельца доступа. Доступна по адресу: http://127.0.0.1:8000/passcard_info/<uuid:passcode>rg/).
