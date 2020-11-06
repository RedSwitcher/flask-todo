#### Todo功能

##### 1、创建新的todo

---cmd---

```powershell
C:\WINDOWS\system32>curl -d POST -v http://127.0.0.1:5000/todo/api/v1.0/todos/1/username01/event01
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> POST /todo/api/v1.0/todos/1/username01/event01 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.55.1
> Accept: */*
> Content-Length: 4
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 4 out of 4 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 51
< Server: Werkzeug/1.0.1 Python/3.6.8
< Date: Fri, 06 Nov 2020 11:48:13 GMT
<
{"ID":1,"event":"event01","username":"username01"}
* Closing connection 0
```



##### 2、删除某条todo

---cmd---

```powershell
C:\WINDOWS\system32>curl -X DELETE -v http://127.0.0.1:5000/todo/api/v1.0/todos/1
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> DELETE /todo/api/v1.0/todos/1 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.55.1
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 204 NO CONTENT
< Content-Type: application/json
< Server: Werkzeug/1.0.1 Python/3.6.8
< Date: Fri, 06 Nov 2020 11:49:43 GMT
<
* Closing connection 0
```



##### 3、更新某条todo

---cmd---

```powershell
C:\WINDOWS\system32>curl -X PATCH -v http://127.0.0.1:5000/todo/api/v1.0/todos/1/event02
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> PATCH /todo/api/v1.0/todos/1/event02 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.55.1
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 51
< Server: Werkzeug/1.0.1 Python/3.6.8
< Date: Fri, 06 Nov 2020 11:49:05 GMT
<
{"event":"event02","id":1,"username":"username01"}
* Closing connection 0
```



##### 4、列出所有的todo

---cmd---

```powershell
C:\WINDOWS\system32>curl -X GET -v http://127.0.0.1:5000/todo/api/v1.0/todos
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET /todo/api/v1.0/todos HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.55.1
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 53
< Server: Werkzeug/1.0.1 Python/3.6.8
< Date: Fri, 06 Nov 2020 11:48:40 GMT
<
[{"event":"event01","id":1,"username":"username01"}]
* Closing connection 0
```



#### 要求：

**1、Flask作为开发框架**

**2、todo数据存储在Cassandra里**

**3、遵循RESTfulAPI开发规范**

**4、每个api都有对应的测试**

**5、使用Docker和docker-compose对应用进行打包和部署**

**6、使用pytest 对每个功能进行测试，有生成测试文件report.html**

