from flask import Flask, request, jsonify
from utils import predict_it, image_transform
application=Flask(__name__)
image_extensions={"png","jpg","jpeg"}

## check file type
def file_list(file):
    return "." in file and file.rsplit(".",1)[1].lower()

clothes_class={0:"T-shirt/top",
1 :"Trouser",
2 :"Pullover",
3 :"Dress",
4 :"Coat",
5 :"Sandal",
6 :"Shirt",
7 :"Sneaker",
8 :"Bag",
9 :"Ankle boot"}

@application.route("/predict_class",methods=["POST"])
def predict_class():
    if request.method=="POST":

        ## check for file
        file=request.files.get('file')
        if file==None or file.filename=="":
            return jsonify({"Error":"no file"})

        ## check file type
        if not file_list(file.filename):
            return jsonify({"Error":"Format not supported"})

        try:
            image=file.read()
            tensor=image_transform(image)
            prediction=predict_it(tensor)
            data={"Prediction":prediction.item(),"Class_name":clothes_class[prediction.item()]}
            return jsonify(data)
        except:
            return jsonify({"Error"})
    return jsonify({'result':1})


