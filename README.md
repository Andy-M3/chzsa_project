Создайте и активируйте виртуальное окружение
python3 -m venv venv
source venv/bin/activate

Установите зависимости 
pip install -r requirements.txt

Выполните миграции базы данных
python manage.py makemigrations
python manage.py migrate

Загрузите тестовые данные
python manage.py loaddata groups.json
python manage.py loaddata users.json
python manage.py loaddata initial_data.json

Запустите сервер разработки
python manage.py runserver
