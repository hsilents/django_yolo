import requests


HOST ='http://127.0.0.1:8000'
res = requests.post(HOST + '/api-token-auth/', {
    'username': 'root',
    'password':'root',
})

res.raise_for_status()
token = res.json()['token']
print(token)

#RZ
headers = {'Authorization' : 'JWT ' + token, 'Accept' : 'application/json'}

# Post Create

data = {
'title' :'W by code',
'text' :'APIH by code',
'created_date' :'2022-06-07T18:34:00+09:00',
'published_date' :'2022-06-07T18:34:00+09:00'
}

file = {'image' : open('D:/source/Django_YOLO/myblog/media/2023/10/08/20231010042335.png','rb')}
res = requests.post(HOST + '/api_root/Post/', data=data, files=file, headers=headers)
print(res)
print( res.json( ))