# Queue definition
queue = []

# add value to the rear of the queue
def enqueue(value):
    queue.append(value)

# remove and return the front element of the queue
def dequeue():
    if not is_empty():
        return queue.pop(0)
    else:
        return None

# return true if the queue is empty
def is_empty():
    return len(queue) == 0

# display queue
def display():
    print("Queue:", queue)