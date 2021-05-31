from flask import Flask,jsonify,request

app=Flask(__name__)

tasks=[
    {
    'Contact':'2345678901',
    'Name':'Raju',
    'done':False ,
    'id':1
    },
    {
    'Contact':'2345678931',
    'Name':'Sid',
    'done':False ,
    'id':2
    }
]

@app.route('/')
def hello_world() :
    return 'Hello World'

@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'error-400'
        },400)
    contact={
        'Contact':request.json.get('Contact',''),
        'Name':request.json['Name'],
        'done':False ,
        'id':tasks[-1]['id']+1 
    }    
    tasks.append(contact)
    return jsonify({
        'status':'success',
        'message':'contact_added'
    })
   
@app.route('/get-data')
def get_task():
    return jsonify({
        'data':tasks
    })


if (__name__=='__main__'):
    app.run(debug=True)