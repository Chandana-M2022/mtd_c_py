import sys

def insertqueue(queue):
    element = input('Enter the element to be queued: ')
    queue.insert(0, element)

def deletequeue(queue): # Mutator
    if len(queue) == 0:
        print('queue is empty')
        return
    print(f'deleted queue element is {queue[-1]}')
    del queue[-1]

def Listqueue(queue): # Accessor
    if len(queue) == 0:
        print('queue is empty')
        return
    print(f'The queue is {queue[::-1]}')

def top(queue): # read only function 
    if len(queue) == 0:
        print('Stack is empty')
        return
    print('The top element is', queue[0])

def exit_program(queue):
    sys.exit('End of Program')

def invalid_choice(queue):
    print('Invalid choice entered')

def get_menu(choice, queue):
    menu = {
        1 : insertqueue,
        2 : deletequeue,
        3 : Listqueue ,
        4 : exit_program
    }
    menu.get(choice, invalid_choice)(queue)

def start_app(queue):
    choice = 0
    while True:
        print('1:insertqueue 2:deletequeue 3:Listqueue 4:Exit')
        choice = int(input('Enter your choice: '))
        get_menu(choice, queue)

queue = [] # this list is gonna work as queue
start_app(queue) # type: ignore