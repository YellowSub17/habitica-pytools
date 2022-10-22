
from hab import HabUser




user = HabUser()


tasks = user.tasks('GET')

for task in tasks:
    if 'alias' not in task.keys():
        continue
    if 'xyzpa' in task['alias']:
        user.delete_task(task['id'])


