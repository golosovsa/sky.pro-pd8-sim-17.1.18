# У вас настроенный фласк и список с данными.
#
# Вам необходимо:
#
# 1. Создать переменную app c экземпляром
#    класса App из библиотеки flask_restx
#
# 2. Создать неймспейc note_ns с адресом `notes`
#
# 3. Создать Сlass based view который позволяет
#    с помощью POST-запроса по адресу `/notes/`
#    добавить в список соответствующий объект
#
# Пример POST-запроса:
#
# {
#  "id": 4,
#  "text": "Текст заметки идет здесь",
#  "author": "Кто ты?"
# }

from flask import Flask, request
from pprint import pprint
from flask_restx import Api, Resource

app = Flask(__name__)
app. config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}

api = Api(app)
note_ns = api.namespace("notes")

notes = [
    {
        "id": 1,
        "text": "This is my note!",
        "author": "me",
    },
    {
        "id": 2,
        "text": "This is also my note!",
        "author": "me",
    }
]

# TODO напишите Class Based View

@note_ns.route("/")
class NotesView(Resource):

    def post(self):
        notes.append(request.json)
        return "", 201

                                                
     
                                                # Не удаляйте этот код, он нужен для
if __name__ == '__main__':                      # имитации post-запроса и вывода
    client = app.test_client()                  # результата в терминал
    response = client.post('/notes/', json={"id": 3, "text": "test text", "author": "test author"})  # TODO для самопроверки вы можете добавить
    pprint(notes, indent=2)                     # свой json в соответствующий аргумент
                                                # функции post
