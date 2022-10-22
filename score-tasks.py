
from hab import HabUser




user = HabUser()



ntasks = 0
tasks = user.tasks('GET')

for task in tasks:

    if 'alias' in task.keys():
        ntasks +=1

print(ntasks)



dummy_habit_data ={
    'text':'Dummy Habit',
    'type':'habit',
    'alias': 'dummyhabit_xyzpa',
    'priority':2,
    'up':False,
    'down':True,
}



for _ in range(ntasks):

    user.











