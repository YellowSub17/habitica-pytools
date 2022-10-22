import datetime
import json
import requests


from rich.console import Console
console = Console()



API_URL = 'https://habitica.com/api/v3'




class HabUser:

    def __init__(self, creds_file='./credentials.json'):

        self.load_credentials(creds_file)
        self.req_headers = {"x-api-user": self.USER_ID,"x-api-key": self.API_TOKEN}


    def load_credentials(self,f):

        with open(f) as creds_file:
            creds_file_cont = creds_file.read()

        self.USER_ID = json.loads(creds_file_cont)["USER_ID"]
        self.API_TOKEN = json.loads(creds_file_cont)["API_TOKEN"]




#     def get_tasks(self):

        # res = requests.request('GET', f'{API_URL}/tasks/user',
                               # headers=self.req_headers)
        # res_json = res.json()

        # if not res_json['success']:
            # console.print('Request Failed', style='bold red')
            # console.print(res_json)
            # quit()


        # console.print('Request Success', style='bold green')
        # console.print(res_json)

        # return res_json['data']


    # def post_tasks(self, data):
        # res = requests.request('POST', f'{API_URL}/tasks/user',
                               # headers=self.req_headers, json=data)
        # res_json = res.json()

        # if not res_json['success']:
            # console.print('Request Failed', style='bold red')
            # console.print(res_json)
            # quit()

        # console.print('Request Success', style='bold green')
        # console.print(res_json)


    def tasks(self, method, data=[]):
        res = requests.request(method, f'{API_URL}/tasks/user',
                               headers=self.req_headers, json=data)
        res_json = res.json()

        if not res_json['success']:
            console.print('Request Failed', style='bold red')
            console.print(res_json)
            quit()


        console.print('Request Success', style='bold green')
        console.print(res_json)

        return res_json['data']









    def delete_task(self, task_id):
        res = requests.request('DELETE', f'{API_URL}/tasks/{task_id}',
                               headers=self.req_headers)
        res_json = res.json()

        if not res_json['success']:
            console.print('Request Failed', style='bold red')
            console.print(res_json)
            quit()

        console.print('Request Success', style='bold green')
        console.print(res_json)


    def score_task(self, task_id, updown):
        res = requests.request('post', f'{API_URL}/tasks/{task_id}/score/{updown}',
                               headers=self.req_headers)
        res_json = res.json()

        if not res_json['success']:
            console.print('Request Failed', style='bold red')
            console.print(res_json)
            quit()

        console.print('Request Success', style='bold green')
        console.print(res_json)





def generate_task_data(text, task_type, alias, notes='', list_texts=None, ndays=None):

    data = {}
    data['text'] = text
    data['type'] = task_type
    data['alias'] = alias
    data['notes'] = notes

    if list_texts is not None:
        checklist = []
        for list_text in list_texts:
            checklist.append({'text':list_text, 'completed':False})
        data['checklist'] = checklist

    if ndays is not None:
        time_now = datetime.datetime.now()
        time_delta = datetime.timedelta(days=ndays)
        time_due = time_now + time_delta
        data['date'] = time_due.isoformat()

    return data





















