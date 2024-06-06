import threading
import random
import queue


list_size = 5
number_range = (1, 50)


numbers = []
list_ready = threading.Event()
result_queue = queue.Queue()

def fill_list():
    global numbers
    for i in range(list_size):
        numbers.append(random.randint(*number_range))
    list_ready.set()

def calculate_sum():
    list_ready.wait()
    total_sum = sum(numbers)
    result_queue.put(('Součet čísel seznamu', total_sum))

def calculate_average():
    list_ready.wait()
    average = sum(numbers) / len(numbers)
    result_queue.put(('Průměrné číslo seznamu', average))


thread_fill = threading.Thread(target=fill_list)
thread_sum = threading.Thread(target=calculate_sum)
thread_avg = threading.Thread(target=calculate_average)

thread_fill.start()
thread_sum.start()
thread_avg.start()


thread_fill.join()
thread_sum.join()
thread_avg.join()


print(f"Seznam náhodných čísel: {numbers}")
while not result_queue.empty():
    result_type, result_value = result_queue.get()
    print(f"{result_type}: {result_value}")