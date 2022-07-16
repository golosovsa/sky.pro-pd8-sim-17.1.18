# У Вас настроенный фласк
# и список словарей с данными.
#
# Вам необходимо:
#
# 1. Создать переменную app c экземпляром
#    класса App из библиотеки flask_restx
#
# 2. Создать неймспейc note_ns с адресом `/notes`
#
# 3. Cоздать Class Based View, который позволяет:
#
# - С помощью PATCH-запроса на адрес `/notes/{id}`
#   частично обновить содержащуюся в в списке
#   сущность с соответствующим id
#
# - С помощью PUT-запроса на адрес `/notes/{id}`
#   перезаписать в списке сущность
#   с соответствующим id
#
# - С помощью DELETE-запроса на адрес `/notes/1`
#   удалить данные о сущности с соответсвующим id

from flask import Flask, request
from flask_restx import Api, Resource
from pprint import pprint

app = Flask(__name__)

api = Api(app)
app. config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}

note_ns = api.namespace("notes")

notes = {
    1: {
        "id": 1,
        "text": "this is my super secret note",
        "author": "me"
    },
    2: {
        "id": 2,
        "text": "oh, my note",
        "author": "me"
    }
}

# TODO Допишите Class Based View здесь
@note_ns.route("/<int:uid>")
class NoteView(Resource):
    def put(self, uid):
        if uid not in notes:
            return "", 404
        notes[uid].update(request.json)
        return "", 204

    def patch(self, uid):
        if uid not in notes:
            return "", 404
        notes[uid].update(request.json)
        return "", 201

    def delete(self, uid):
        if uid not in notes:
            return "", 404
        del notes[uid]
        return "", 200


# # # # # # # # # # # #                                    
if __name__ == '__main__':
    client = app.test_client()                          # TODO вы можете раскомментировать
    # response = client.put('/notes/1', json=PUT)       # соответсвующе функции и
    # response = client.patch('/notes/1', json=PATCH)   # воспользоваться ими для самопроверки
    # response = client.delete('/notes/1')              # аналогично заданию `post`
    pprint(notes, indent=2)
