from flask import Flask
import json
import requests

app = Flask(__name__)

URL_DEP = 'http://127.0.0.1:5001/get-dep'
URL_EMPL = 'http://127.0.0.1:5001/get-empl'
URL_TEAM = 'http://127.0.0.1:5001/get-team'
URL_ALL = 'http://127.0.0.1:5001/get-info'


def get_dep():
    r = requests.get(URL_DEP)
    return r.content

def get_empl():
    re = requests.get(URL_EMPL)
    return re.content

def get_team():
    req = requests.get(URL_TEAM)
    return req.content

def parse_json(arg1, arg2, arg3):
    dictionary = {}
    dictionary = {**arg1, **arg2, **arg3}
    return json.dumps(dictionary)

#Employee

#def salary_employee(dict_team, dict_emp):
#    if self.exp > 2 and self.exp < 5:
#        self.salary = int(self.salary) + 200
#    elif self.exp > 5:
#        self.salary = int(self.salary)*1.2 +  500
#    return int(self.salary)



#Manager
#def salary_manager(dict_team, dict_emp):
#    if len(self._team) > 5:
#        self.salary = super().get_salary() + 200
#    elif len(self._team) > 10:
#        self.salary = super().get_salary() + 300
#    elif sum(type(i) == developer for i in self._team) > len(self._team) / 2:
#        self.salary = super().get_salary()*1.1
#    print(int(self.salary))
#    return (int(self.salary))

#Designer

def salary_designer(dict_emp):
    for i in dict_emp['Employee']:
        if i['position'] == "Designer":
            i['salary'] = int(i['salary'])*i['coefficient']
        else:
            pass


@app.route('/get', methods=['GET'])
def get_info():
    req = requests.get(URL_ALL)
    return json.dumps(req)

@app.route('/get-one', methods=['GET'])
def get_one():
    emp = get_empl()
    team = get_team()
    dep = get_dep()
    dep = json.loads(dep)
    emp = json.loads(emp)
    team = json.loads(team)
    salary_designer(emp)
    res = parse_json(dep, team, emp)
    return res


if __name__== '__main__':
    app.run(debug=True)

