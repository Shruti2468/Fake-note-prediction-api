import uvicorn
from fastapi import FastAPI
import pickle
from BankNote import BankNote
#py -m ensurepip --upgrade
app=FastAPI()
pickle_in=open('classifier.pkl','rb')
model=pickle.load(pickle_in)

@app.get('/')
def hello():
    return {'message':'hello,world'}

@app.post('/predict')
def predict(data:BankNote):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']

    prediction= model.predict([[variance,skewness,curtosis,entropy]])

    #-3.75030, -13.45860 ,  17.5932, -2.77710

    if prediction[0]>0.5:
        prediction = "Fake note"
    else:
        prediction="Real note"
    return {'prediction':prediction}



if __name__=='__main__':
    uvicorn.run(app)