
from hab import HabUser

import time


from rich.console import Console
console = Console()
console.print('Counting incomplete tasks: ', style='bold yellow', end='')


user = HabUser()


n_incomp = 0
tasks = user.get_tasks()

for task in tasks:
    if 'alias' in task.keys():
        n_incomp +=1

console.print(f'{n_incomp}.', style='bold yellow')


dummyhabit_data ={
    'text':'Dummy Habit',
    'type':'habit',
    'alias': 'dummyhabit_xyzpa',
    'priority':1.5,
    'up':False,
    'down':True,
}



for i in range(n_incomp):
    console.print(f'{i+1}', style='bold yellow', end='\r')

    user.post_tasks(dummyhabit_data)
    tasks = user.get_tasks()
    for task in tasks:
        if 'alias' in task.keys():
            if task['alias']=='dummyhabit_xyzpa':

                dummyhabit_id = task['id']

    user.score_task(dummyhabit_id, 'down')
    user.delete_task(dummyhabit_id)


console.print(f'Done.', style='bold yellow')


















