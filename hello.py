from flask import Flask
from flask import request


app = Flask(__name__)
@app.route("/")
def index():
    win32api.MessageBox(0, 'You have just run a python script on the page load!', 'Running a Python Script via Javascript', 0x00001000)
    return render_template('index.html')


@app.route('/res',methods = ['GET'])  
def res():
    '''a=[]
    i=0 
    filter={"rollno":245621733069}
    cursor=collection.find(filter)
    for i in cursor:
          a[i]=cursor
    return a '''
    print(">>>>>>>>>>>>>>>>>>>>>",request.args)    
    return request.args
    
@app.route('/getresults')  
def getresults():  
   rollno = request.args.get('rollno')
   return "<h1>Sucess</h1>"+rollno


    