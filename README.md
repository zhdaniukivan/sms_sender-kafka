скачиваем проеrт по ссылке git clone ...

pip install -r requirements.txt
находясь в директории проета запускаем виртуальное окружение в трех окнах терминала:
source PRG1/bin/activate
в двух окнах терминала переходим в паку с распоковоной кафкой и выполняем команды:
в первом окне запуск Zookeeper:
bin/zookeeper-server-start.sh config/zookeeper.properties
во втором окне запуск Kafka сервер:
bin/kafka-server-start.sh config/server.properties
в тертьем окне просто запкскаме сервер django:
python manage.py runserver
