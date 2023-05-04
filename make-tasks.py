
from hab import HabUser, generate_task_data

from rich.console import Console
console = Console()
console.print('Creating tasks: ', style='bold green', end='')




t1 = generate_task_data('Clean room', 'todo', 'cleanroom_xyzpa',
        list_texts=['Tidy items.','Vacuum floor.', 'Wipe surfaces.'], ndays=None)


t2 = generate_task_data('Do washing.', 'todo', 'washing_xyzpa',
        list_texts=['Bring downstairs.', 'Load machine.', 'Dry.', 'Put away.'], ndays=None)


t3 = generate_task_data('Go to gym.', 'todo','gym_xyzpa',
        list_texts=['Yoga', '1/3', '2/3', '3/3'], ndays=None)


t4 = generate_task_data( 'Cook dinner.', 'todo', 'cookdinner_xyzpa',
        list_texts=[ '1/2', '2/2' ], ndays=None)


t5 = generate_task_data( 'Driving practice.', 'todo', 'drivingpractice_xyzpa',
        list_texts=[ '1/3', '2/3', '3/3'], ndays=None)


t6 = generate_task_data( 'Practice bass.', 'todo', 'bass_xyzpa',
        list_texts=['1/5','2/5','3/5','4/5','5/5'], ndays=None)

t7 = generate_task_data( 'Shave.', 'todo', 'shave_xyzpa', ndays=None)




user = HabUser()
user.post_tasks(data=[t1, t2, t3, t4, t5, t6, t7])

console.print('Done.', style='bold green')
