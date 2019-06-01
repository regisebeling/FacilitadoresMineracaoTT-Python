import requests
face_detect = 'https://api-us.faceplusplus.com/facepp/v3/detect'
face_analyze='https://api-us.faceplusplus.com/facepp/v3/face/analyze'

# Parâmetros para enviar à API Face++
params ={
    'api_key':'API_KEY_FACE++',
    'api_secret':'API_SECRET_FACE++',
    'image_url':'http://cdn.shopify.com/s/files/1/0075/6878/5472/articles/torres.jpg?v=1553081719',
    'return_attributes':'gender,age'
}
req= requests.post(face_detect,params=params)

# Se a consulta não detecta face na foto, não há como inferir idade e gênero
if(len(req.json()['faces']) == 0):
    print('No age');
# Se detecta face então analisa idade e gênero
else:
    token = req.json()['faces'][0]['face_token']
    params2['face_tokens']=token
    req2=requests.post(face_analyze,params=params2)
    print(req2.json()['faces'][0]['attributes']['age']['value'])
    print(req2.json()['faces'][0]['attributes']['gender']['value'])
