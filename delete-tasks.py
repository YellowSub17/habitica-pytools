
from hab import HabUser


from rich.console import Console
console = Console()
console.print('Deleting tasks: ', style='bold red', end='')




user = HabUser()


tasks = user.get_tasks() + user.get_tasks('completedTodos')

for task in tasks:
    if 'alias' not in task.keys():
        continue
    if 'xyzpa' in task['alias']:
        user.delete_task(task['id'])


console.print('Done.', style='bold red')
