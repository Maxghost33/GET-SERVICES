from flask import render_template,request,Flask,jsonify
from app import app
# from app.forms import DepForm
import json
import psycopg2
from psycopg2.extras import RealDictCursor
import requests
@app.route("/")

##################################################################################################################################

### GET BEGINS HERE: 
@app.route("/send", methods=['GET'])
def get():

    conn = psycopg2.connect(host='127.0.0.1', user="anton", password="Samsung01", dbname='micro', cursor_factory=RealDictCursor)
    cur = conn.cursor()      
    cur.execute("select name from depart")
    result = cur.fetchall()
    result2 = {"department":[]}
    for i in result:
        result2["department"].append(i)
    print(result2)
    return jsonify(result)

@app.route("/send2", methods=['GET'])
def get2():

    conn = psycopg2.connect(host='127.0.0.1', user="anton", password="Samsung01", dbname='micro', cursor_factory=RealDictCursor)
    cur = conn.cursor()      
    cur.execute("select team_id,name,surname,experience,position,salary,coef from employee")
    result = cur.fetchall()
    result2 = {"department":[]}
    for i in result:
        result2["department"].append(i)
    print(result2)
    return jsonify(result)

@app.route("/send3", methods=['GET'])
def get3():

    conn = psycopg2.connect(host='127.0.0.1', user="anton", password="Samsung01", dbname='micro', cursor_factory=RealDictCursor)
    cur = conn.cursor()      
    cur.execute("select iddepart,name,id_manager  from team")
    result = cur.fetchall()
    result2 = {"department":[]}
    for i in result:
        result2["department"].append(i)
    print(result2)
    return jsonify(result)


# "team_id":2,"name":"Artem","sname":"Kubrachenko","exp":1,"position":"manager","salary":1000,"coefficient":1

##################################################################################################################################

@app.route('/new', methods=['GET'])
def sent():
    sender = {"depart_id":1,"name":"developers","manager_id":"1"}
    result = json.dumps(sender)
    r = requests.post("http://127.0.0.1:5000/teams", data=result)
    return result

@app.route("/department", methods=['GET', 'POST'])
def department():
    form1 = DepForm()
    if form1.validate_on_submit():
        print(form1.DepName.data)
        id_="Type"
        sender = {id_: form1.DepName.data}
        url = "http://127.0.0.1:5000/depart"
        r = requests.post(url, data=json.dumps(sender))
    return render_template("index.html", title="Department", form=form1)



@app.route("/depart", methods=['POST'])
# Connection to the database 
def writer():
    if request.get_json(force=True):
        print("Ok")
        result = request.get_json(force=True)
        print(type(result))
    else: print("Empty")
    conn = psycopg2.connect(host='127.0.0.1', user="anton", password="Samsung01", dbname='micro')
    cur = conn.cursor()
    for i in result:
        print(i)
    cur.execute("select Name from Depart where Name ='" + str(result[i])+"'")
    results = cur.fetchall()
    if results:
        print("Data exist")

    else:
        print("Data not presented in the database")
        cur.execute("insert into Depart (Name) values ('"+ str(result[i])+"')")
        conn.commit()
        cur.execute("select "+result[i]+" from Depart where Name = '"+str(results[i])+"'")
        results = cur.fetchall()


@app.route("/users", methods=['POST'])
def writer2():
    if request.get_json(force=True):
        print("Ok")
        result = request.get_json(force=True)
    else: print("Empty")
    conn = psycopg2.connect(host='127.0.0.1', user="anton", password="Samsung01", dbname='micro', cursor_factory=RealDictCursor)
    cur = conn.cursor()
    cur.execute("select count(*) from employee where name ='"+ str(result['name'])+"' and surname = '" + str(result['sname']) + "'")
    results = cur.fetchall()
    print(result)
    if str(result)=="1":
        print("Data exist")
    else:
        print("Data not presented in the database")
        for i in result:
            if result[i] == None:
                task = "dont write"
                break
            else: task = "write"
        if task == "write":
            cur.execute("insert into employee (team_id,name,surname,experience,position,salary,coef) values ('"+ str(result["team_id"])+"','"+ str(result["name"])+"','"+ str(result["sname"])+"','"+ str(result["exp"])+"','"+ str(result["position"])+"','"+ str(result["salary"])+"','"+ str(result["coefficient"])+"')")
            conn.commit()


@app.route("/teams", methods=["POST"])
def writer3():
    if request.get_json(force=True):
        print("Ok")
        result = request.get_json(force=True)
    else: print("Empty")
    conn = psycopg2.connect(host='127.0.0.1', user="anton", password="Samsung01", dbname='micro')
    cur = conn.cursor()
    cur.execute("select count(*) from employee where name ='" + str(result["depart_id"])+"' and surname = '" + str(result["name"]) + "'")
    results = cur.fetchall()
    if str(result)=="1":
        print("Data exist")
    else:
        print("Data not presented in the database")
        for i in result:
            if result[i] == None:
                task = "dont write"
                break
            else: task = "write"
        if task == "write":
            cur.execute("insert into team (iddepart,name,id_manager ) values ('"+ str(result["depart_id"])+"','"+ str(result["name"])+"','"+ str(result["manager_id"])+"')")
            conn.commit()

# if __name__ == "__main__":
#     app.run()






# from app import app
# from app import jsonify
# import psycopg2
# import sqlite3
# from flask import request
# from flask import json
# import requests

# @app.route("/database/department", methods=['POST'])


# # Connection to the database 
# def writer():
#     conn = psycopg2.connect(host='127.0.0.1', user="anton", password="Samsung01", dbname='micro')
#     cur = conn.cursor()
#     cur.execute("select Name from Depart where Name = 'IT'")
#     results = cur.fetchall()
#     print(result)
#     if results:
#         print("Data exist")
#     else:
#         cur.execute("""insert into Depart (Name) values ('IT')""")
#         conn.commit()

# @app.route("/send", methods=['GET'])

# def get():
#     sender = {"title":"Read a book"}
#     r = requests.post("http://127.0.0.1:5000/base", data=json.dumps(sender))
#     return sender

# @app.route("/base", methods=['POST'])
# # Connection to the database 
# def write():
#     if request.json:
#         print("Ok")
#         result = request.json
#         print(result)
#     else: print("Empty")



# # print(results)




# # task = [{ 'id':1, 'department':"IT"},
# # {"id":1},
# # {'id':1,'Name':'Anton',"Surname":"Golovin"}
# # ]




# # @app.route('/')
# # # @app.route('/index/task', methods=['GET'])
# # #     return jsonify({'task':task})

# # @app.route('/index')
# # def index(results=results):
# #     user = {'Name':'Anton'}
# #     return """
# # <html>
# # <head>
# # <title>Hello Page</title>
# # </head>
# # <body>
# # <h1> Hello """ + user["Name"] + """ </h1>
# # <h1>Yor reqesr has return"""+ str(results) + """ </h1>
# # <buton>Touch me</button>
# # </body>
# # </html>
# # """


# # # @app.route('index/request', methods=['POST'])

# # # def post_request():
# # #     if not request.json or not 'id' in request.json:
# # #         abort(400)
# # #     request = {
# #         'id':task[+1]
        
# #     }
# #     task.append(request)

