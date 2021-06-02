import requests
re=requests.post("https://fmnist-app.herokuapp.com/predict_class",files={"file":open("test_images/sample__7.png","rb")})
print(re.text) ## will return from the predict_class function from main.py
