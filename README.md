# Техническое задание


Разработать REST API (Json)


Ниже перечислены основные сущности и их поля, авторизации не требуется, итоговый результат работы должен представлять собой архив исходного кода и Dockerfile, который будет запускать тестовый сервер Django.


Сущности: 

+	Исполнитель
    + Имя
+ Задача

  + Дата создания

  + Исполнитель

  + Приоритет (допустимые значения: 1,2,3)

  + Заголовок

  + Комментарий


Endpoints:

  + task/update (Обновить задачу)

  + task/create (Создать задачу)

  + task/destroy (Удалить задачу)

Стек: Python, Django (Djangorestframework)

## Инструкция по запуску проекта:
1. Установить Docker Desktop [ссылка](https://www.docker.com/products/docker-desktop/)
2. Вставить/создать файл ".env" в корень проекта
3. Запустить команду:
+     docker-compose up

