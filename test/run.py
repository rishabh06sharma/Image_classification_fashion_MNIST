import requests
re=requests.post("http://127.0.0.1:5000/predict_class",files={"file":open("test_images/sample__4.png","rb")})
print(re.text) ## will return from the predict_class function from main.py
