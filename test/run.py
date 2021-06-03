import requests

# Image directory
print("New Image? (y/n)")
check_input=input()
if check_input=="y":
    directory=input("Enter the directory: ")
else:
    print("Using default directory (test image): test_images/sample__1.png")
    directory=("test_images/sample__1.png")

# request prediction from heroku
re=requests.post("https://fmnist-app.herokuapp.com/predict_class",files={"file":open(directory,"rb")})
print(re.text) ## will return from the predict_class function from main.py
