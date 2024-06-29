import requests

data={
    "poet_id":"libai",
    "text":"五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。"
}

response2=requests.post("http://127.0.0.1:9880/verse",json=data)

if response2.status_code == 200:  
    print("请求成功，服务器返回:",response2.content)
else:  
    print("请求失败，状态码:", response2.status_code)  
    print("响应内容:", response2.text)


with open("success.wav","wb") as f:
    f.write(response2.content)