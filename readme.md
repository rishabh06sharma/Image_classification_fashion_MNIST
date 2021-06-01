## Fashion MNIST
CNN with k-fold cross validation <br /> 

Requirements
* Pytorch <br /> 
* Flask <br /> 
* Requests <br /> 

Setup environment variables (replace set with export in linux) <br /> 
```python
set FLASK_APP=main.py
```
```python
set export FLASK_ENV=development 
```
```python
flask run
```

File details <br/>
* Model training: Train_Fashion MNIST.ipynb <br/>
* Deployment file: run.py <br/>
* Load model & Utils: main.py, utils.py<br/>
* Dataset folder: MNIST<br/>
* Trained model folder: models<br/>
* Image prediction testing dataset: test_images<br/>

## Run test image (seprate terminal)
```python
python run.py
```

