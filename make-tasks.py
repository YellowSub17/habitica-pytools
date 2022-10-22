
from hab import HabUser, generate_task_data

from rich.console import Console
console = Console()
console.print('Creating tasks: ', style='bold green', end='')


t1 = generate_task_data('Clean room', 'todo', 'cleanroom_xyzpa', ndays=6)


t2 = generate_task_data('Do washing.', 'todo', 'washing_xyzpa', ndays=6)


t3 = generate_task_data('Go to gym.', 'todo','gym_xyzpa',
        list_texts=['Yoga', '1/3', '2/3', '3/3'], ndays=6)


t4 = generate_task_data( 'Cook dinner.', 'todo', 'cookdinner_xyzpa',
        list_texts=[ '1/3', '2/3', '3/3'], ndays=6)


t5 = generate_task_data( 'Driving practice.', 'todo', 'drivingpractice_xyzpa',
        list_texts=[ '1/3', '2/3', '3/3'], ndays=6)


t6 = generate_task_data( 'Practice bass.', 'todo', 'bass_xyzpa',
        list_texts=['1/5','2/5','3/5','4/5','5/5'], ndays=6)



user = HabUser()
user.post_tasks(data=[t1, t2, t3, t4, t5, t6])

console.print('Done.', style='bold green')
