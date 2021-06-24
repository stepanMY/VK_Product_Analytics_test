from concurrent.futures import ThreadPoolExecutor
from counter import Counter
from task import Task

new_counter = Counter()
values = [2] * 10
tasks = []
for value in values:
    tasks.append(Task(value))
with ThreadPoolExecutor(max_workers=2) as executor:
    for task in tasks:
        a = executor.submit(new_counter.update, task.execute())
print(new_counter.value)
