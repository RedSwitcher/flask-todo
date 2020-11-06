import pytest

from app import app


@pytest.fixture
def client():
    """ get test client """

    app.config['TESTING'] = True
    with app.app_context():
        client = app.test_client()
        # https://stackoverflow.com/a/48745985/8397149
        client.environ_base['HTTP_TOKEN'] = 'Bearer your_token'
        yield client


# 改善 404 测试
# @app.errorhandler(404)
def test_not_found(client):
    url = 'http://127.0.0.1:5000/todo/api/v1.0/todos/username01/event01'
    # post请求
    resp = client.post(url)
    assert resp.status_code == 404
    assert resp.json == {
        "error": "Not found"
    }


# 创建 todo 测试
def test_create_todo(client):
    url = 'http://127.0.0.1:5000/todo/api/v1.0/todos/1/username01/event01'
    # post请求
    resp = client.post(url)
    assert resp.status_code == 201
    # 判断接口返回的数据是否与待验证数据一致
    assert resp.json == {
        "ID": 1,
        "event": "event01",
        "username": "username01"
    }


# 列出所有的 todo 测试
def test_show_todos(client):
    url = 'http://127.0.0.1:5000/todo/api/v1.0/todos'
    resp = client.get(url)
    assert resp.status_code == 200
    assert resp.json == [
        {
            "event": "event01",
            "id": 1,
            "username": "username01"
        }
    ]


# 更新 todo 测试
def test_update_todo(client):
    url = 'http://127.0.0.1:5000/todo/api/v1.0/todos/1/event02'
    resp = client.patch(url)
    assert resp.status_code == 201
    assert resp.json == {
        "event": "event02",
        "id": 1,
        "username": "username01"
    }


# 删除 todo 测试
def test_delete_todo(client):
    url = 'http://127.0.0.1:5000/todo/api/v1.0/todos/1'
    resp = client.delete(url)
    assert resp.status_code == 204
    # assert resp.json == {
    #
    # }
