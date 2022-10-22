import datetime

import json
import requests


from rich.console import Console
console = Console()




# with open("./credentials.json") as creds_file:
    # creds_file_cont = creds_file.read()

# USER_ID = json.loads(creds_file_cont)["USER_ID"]
# API_TOKEN = json.loads(creds_file_cont)["API_TOKEN"]

# headers = {
        # "x-api-user": USER_ID,
        # "x-api-key": API_TOKEN,
            # }



def print_current_tasks():
    response = requests.request('GET', 'https://habitica.com/api/v3/tasks/user', headers=headers)
    response_dict = json.loads(response.text)
    # print('###Current Tasks')
    # pprint.pprint(response_dict['data'])




def make_todo2():
    data = {"text":"todo2", "type":"todo", "alias":"abc"}
    response = requests.request('POST', 'https://habitica.com/api/v3/tasks/user',
                                headers=headers, data=data)
    response_dict = json.loads(response.text)
    # print('###Adding Task abc')
    # pprint.pprint(response_dict)






def score_up_todo2():
    response = requests.request('POST', 'https://habitica.com/api/v3/tasks/abc/score/up',
                                headers=headers)
    response_dict = json.loads(response.text)
    # print('###Scoring Up')
    # pprint.pprint(response_dict)






def score_down_todo2():
    response = requests.request('POST', 'https://habitica.com/api/v3/tasks/abc/score/down',
                                headers=headers)
    response_dict = json.loads(response.text)
    # print('###Scoring Down')
    # pprint.pprint(response_dict)



def clear_completed():
    response = requests.request('POST', 'https://habitica.com/api/v3/tasks/clearCompletedTodos',
                                headers=headers)
    response_dict = json.loads(response.text)
    # print('###Cleared Completed')
    # pprint.pprint(response_dict)



# print_current_tasks()
# make_todo2()
# print_current_tasks()
# score_up_todo2()
# print_current_tasks()
# score_down_todo2()


# score_up_todo2()


# clear_completed()




class User:

    def __init__(self):

        self.load_credentials()
        self.req_headers = {"x-api-user": self.USER_ID,"x-api-key": self.API_TOKEN}


    def load_credentials(self,f='./credentials.json'):

        with open(f) as creds_file:
            creds_file_cont = creds_file.read()

        self.USER_ID = json.loads(creds_file_cont)["USER_ID"]
        self.API_TOKEN = json.loads(creds_file_cont)["API_TOKEN"]


    def get_tasks(self,):

        res = requests.request('GET', 'https://habitica.com/api/v3/tasks/user', headers=self.req_headers)
        res_dict = json.loads(res.text)

        console.print(res_dict)
        if not res_dict['success']:
            console.print('Request Failed', style='bold red')
            console.print(res_dict)
        tasks = res_dict['data']








# def print_current_tasks():
    # response = requests.request('GET', 'https://habitica.com/api/v3/tasks/user', headers=headers)
    # response_dict = json.loads(response.text)
    # print('###Current Tasks')
    # pprint.pprint(response_dict['data'])



        


class Task:

    def __init__(self, text, notes='', duedate=None, alias=None):
        self.text = text
        self.notes = notes
        self.duedate = duedate
        self.alias = alias


    def create(self):
        pass



if __name__=="__main__":


    user = User()

    user.get_tasks()












