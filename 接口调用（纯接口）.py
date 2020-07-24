import json
import requests

# 上传接口的调用
url = 'http://127.0.0.1:8067/upload'
file = './测试.txt'
content = {'file':open(file,'rb')}
data = {'userid':'001'}
resp = requests.post(url,files=content,data=data)
result = json.loads(resp.text)
print(result)
print('上传成功！')


# 下载接口的调用
download_url = 'http://127.0.0.1:8067/download?'
filename = '测试.txt'
data = {'filename':filename,'userid':'001'}
res = requests.get(url=download_url,params=data)
# 保存结果
f = open('./download/'+filename,'wb')
f.write(res.content)
f.close()
print('下载成功！')