from cassandra.cluster import Cluster
from flask import Flask, jsonify, make_response, request, abort

app = Flask(__name__)

cluster = Cluster(['cassandra'])

session = cluster.connect()
# 创建 keyspace
session.execute(
    "CREATE KEYSPACE if not exists todo WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};")
# 指定 keyspace
session.execute('use todo;')
# 创建 table
session.execute('create table if not exists todo.todo(user_id int PRIMARY KEY,username text,event text);')


# 改善 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# 创建 todo
@app.route('/todo/api/v1.0/todos/<int:user_id>/<string:username>/<string:event>', methods=['POST'])
def create_dodo(user_id, username, event):
    ls = [user_id, username, event]
    session.execute('insert into todo.todo (user_id,username, event) values (%s, %s, %s);', ls)
    return jsonify({'ID': user_id, 'username': username, 'event': event}), 201


# 删除 todo
@app.route('/todo/api/v1.0/todos/<int:user_id>', methods=['DELETE'])
def delete_todo(user_id):
    ls = [user_id]
    session.execute('delete from todo.todo where user_id =%s;', ls)
    return jsonify({'result': True}), 204


# 更新 todo
@app.route('/todo/api/v1.0/todos/<int:user_id>/<string:event>', methods=['PATCH'])
def update_todo(user_id, event):
    ls = [event, user_id]
    session.execute('update todo.todo set event = %s where user_id = %s', ls)
    row = session.execute('select * from todo.todo where event =%s and user_id = %s ALLOW FILTERING;', ls)
    for i in row:
        dict1 = {'id': i.user_id, 'username': i.username, 'event': i.event}
    return jsonify(dict1), 201


# 列出所有的 todo
@app.route('/todo/api/v1.0/todos', methods=['GET'])
def show_todos():
    rows = session.execute('select * from todo.todo')
    ls = []
    for i in rows:
        dict1 = {'id': i.user_id, 'username': i.username, 'event': i.event}
        ls.append(dict1)
    print(jsonify(ls).status_code)
    return jsonify(ls), 200


if __name__ == '__main__':
    app.run()
