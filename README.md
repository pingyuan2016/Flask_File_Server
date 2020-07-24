# Flask file server
用flask实现文件上传下载服务,包括简单前端，和纯接口实现，以及接口调用的实现

### 上传服务
启动python app.py

访问地址http://127.0.0.1:8067/

#### 注：纯接口上传下载服务
启动 python app(纯接口).py

接口调用（纯接口）.py 为接口调用的实现

### 下载服务（后面跟文件名称）
#### 方法一
访问地址http://127.0.0.1:8067/download?filename=1.png

#### 方法二 用http.server
到需要下载的目录

python -m http.server
