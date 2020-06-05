from flask import Flask, json

students = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_students():
  return json.dumps(students)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=80)
