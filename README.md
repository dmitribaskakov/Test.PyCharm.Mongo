# Test.PyCharm.Mongo
Test Mongo Project in Python into PyCharm

#Обновление зависимостей

pip install -r requirements.txt

#Команды для докера:

Для запуска контейнера с монгой

docker run --detach --rm --name mongodb --publish 27017:27017 mongo

docker stop mongodb


docker build -t test.pycharm.mongo .

docker images

docker ps -a

docker run --detach --rm --name mongo --publish 8080:8080 --env TZ=Asia/Novosibirsk test.pycharm.mongo

docker run --detach --rm --name mongo --publish 8080:8080 --env TZ=Asia/Novosibirsk --volume C:\Projects\Test.PyCharm.Web\resources\:/usr/src/app/resources/ test.pycharm.mongo

docker volume ls

docker volume create mongo

docker run --detach --rm --name mongo --publish 8080:8080 --env TZ=Asia/Novosibirsk --volume web:/usr/src/app/resources/ test.pycharm.mongo





