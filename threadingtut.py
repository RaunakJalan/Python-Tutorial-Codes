# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:35:59 2018

@author: Raunak
"""

import threading
import queue
import time
import numpy as np

'''

print_lock = threading.Lock()

def exmapleJob(worker):
    
    time.sleep(0.5)
    
    with print_lock:
        print(threading.current_thread().name, worker)
        

def threader():
    
    while True:
        
        worker = q.get()
        exmapleJob(worker)
        
        q.task_done()


q = queue.Queue()

for x in range(10):
    
    t = threading.Thread(target = threader)
    
    t.daemon = True
    t.start()
    
start = time.time()
for worker in range(20):
    
    q.put(worker)
    
q.join()


print('Entire job took: ', time.time()-start)

'''

#For 1 thread
'''
def sleeper(n, name):
    
    print('Hi, I am {}. Going to sleep for 5 seconds.\
          \n'.format(name))
    
    time.sleep(n)
    
    print('{} has woken up from sleep \n'.format(name))
    
    
    
t = threading.Thread(target = sleeper, name = 'Thread1',
                     args = (5, 'Thread1'))

t.start()
t.join()

    
print('HELLO')
print('HELLO')
print('HELLO')
'''
'''
#For multiple thread
def sleeper(n, name):
    
    print('Hi, I am {}. Going to sleep for 5 seconds.\
          \n'.format(name))
    
    time.sleep(n)
    
    print('{} has woken up from sleep \n'.format(name))
    

threads_list = []


start = time.time()

for i in range(5):
    
    t = threading.Thread(target = sleeper,
                         name = 'Thread {}'.format(i),
                         args = (5, 'Thread {}'.format(i)))
    
    
    threads_list.append(t)
    
    t.start()
    print('{} has started.'.format(t.name))
    

    
    
for t in threads_list:
    t.join()    


print('TOTAL TIME :',time.time()-start)

print('All five threads have finished their jobs.')
'''

'''

#Daemon: Threads are terminated with use of 
        #this daemon value when the main program
        #terminates. Runs only in CMD and not in 
        #Ipython console or IDLE.

total = 4

def creates_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('added item')
        total += 1
    print('creation is done')


def creates_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('added item')
        total += 1
    print('creation is done')


def limits_items():
    
    #print('finished sleeping')
    
    global total
    while True:
        if total > 5:

            print ('overload')
            total -= 3
            print('subtracted 3')
        else:
            time.sleep(1)
            print('waiting')


creator1 = threading.Thread(target  = creates_items)
creator2 = threading.Thread(target = creates_items_2)
limitor = threading.Thread(target = limits_items, daemon = True)

print(limitor.isDaemon())


creator1.start()
creator2.start()
limitor.start()


creator1.join()
creator2.join()
#limitor.join()



print('our ending value of total is' , total)

'''


#SUBCLASSING: 
'''
 RUN METHOD:
        Method representing the thread's activity.
        You may override this method in a subclass. 
        The standard run() method
        invokes the callable object passed to 
        the object's constructor as the
        target argument, if any, with sequential and 
        keyword arguments taken
        from the args and kwargs arguments, respectively.

   
'''
'''
def run(self):

        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs


#t = threading.Thread(target = sleeper, name = 'thread1',\
 #                    args = (5, 'thread1')) 


class MyThread(threading.Thread):
    
    def run(self):
        
        print('{} has started.'.format(self.getName()))
        
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
        print('{} has finished. '.format(self.getName()))


def sleeper(n, name):
    
    print('Hi, I am {}. Going to sleep for 3 seconds.\
          \n'.format(name))
    
    time.sleep(n)
    
    print('{} has woken up from sleep \n'.format(name))


for i in range(4):
    
    t = MyThread(target = sleeper,
                 name = 'Thread {}'.format(i+1),
                 args = (3, 'Thread {}'.format(i+1)))

    t.start()


'''
'''
 __init__ METHOD:

#TEST TWO, 
 
 
 #Changing overriding __init__
         
     def __init__(self, group=None, target=None, name=None,
args=(), kwargs=None, *, daemon=None):

'''
    
'''
    
class MyThread(threading.Thread):
    
    def __init__(self, number, func, args):
        
        threading.Thread.__init__(self) #necessary to call this first
        self.number = number
        self.func = func
        self.args = args
        
        
    def run(self):
        
        print('Thread {} has started.'.format(self.number))
        self.func(*self.args)   #asterics(*) (pointer of args) because args is a tuple and tuples cannot be called with function
        print('Thread {} has finished.'.format(self.number))        
        


def double(number, cycles):
    
    for i in range(cycles):
        
        number += number
        
    print(number)



threadList = []

for i in range(50):
    
    t = MyThread(number = i + 1, func = double,
                 args = [i, 3])
    
    threadList.append(t)
    
    t.start()
    
    
for t in threadList:
    t.join()


'''


'''

#Test 3 SUPER
# METHOD 1 retaining all content of __init__ and 
            #adding extra methods
    
class MyThread(threading.Thread):
    
    def __init__(self, number, style, *args, **kwargs):
        
        super(MyThread, self).__init__(*args, **kwargs)
        
        self.number = number
        self.style = style
        
        
    def run(self, *args, **kwargs):
        print('thread starting')
        super(MyThread, self).run(*args, **kwargs)
        print('thread has ended')
        
        
        
def sleeper (num, style):
    print('we are sleeping for {} seconds as {}'.format(num, style))
    time.sleep(num)   



t = MyThread(number =3, style = 'yellow', target = sleeper, 
             args = [3, 'yellow']) 

t.start()    

'''




#LOCKS

'''

with keyword: 
    lock.acquire():
        
        //BLOCK OF STATEMENT
        
    lock.release()

'''
'''
lock = threading.Lock()

x=0
count = 100000

def adding_1():
    
    global x
    
    with lock :
    
        for i in range(count):
            x+=2
        
def adding_2():
    
    global x
    
    with lock :
    
        for i in range(count):
            x+=3
        

def subtracting_1():
    
    global x
    
    with lock :
    
        for i in range(count):
            x-=4
        
def subtracting_2():
    
    global x
    
    with lock :
    
        for i in range(count):
            x-=1
        
        
        

add1 = threading.Thread(target = adding_1)
add2 = threading.Thread(target = adding_2)
sub1 = threading.Thread(target = subtracting_1)
sub2 = threading.Thread(target = subtracting_2)

add1.start()
add2.start()
sub1.start()
sub2.start()

add1.join()
add2.join()
sub1.join()
sub2.join()

print(x)
'''



#THREADING TUTORIAL : QUEUE

'''
q = queue.Queue()

q.put(5)

print(q.get())
print('First item got')

print(q.get())#script freezes on this(PROBLEM SOLVED BELOWE USING THREADING)
print('finished')

#print(q.empty())

'''
#FREEZING PROBLEM SOLUTION:
'''
def putting_thread(q):
    
    while True:
        
        print("Starting Thread.")
        time.sleep(10)
        q.put(5)
        print("Put Something")



q = queue.Queue()

t = threading.Thread(target = putting_thread,
                     args = (q,), daemon = True)

t.start()

q.put(5)

print(q.get())
print('First item got')

print(q.get())#script freezes on this(PROBLEM SOLVED BELOWE USING THREADING)
print('finished')
'''

#FIFO
'''
for i in range(5):
    q.put(i)
    
while not q.empty():
    print(q.get(), end = '   ')
''' 


#LIFO
'''
q = queue.LifoQueue()

for i in range(5):
    q.put(i)
    
while not q.empty():
    print(q.get(), end = '   ')

'''

#Priority Queue
'''
q = queue.PriorityQueue()

q.put((1, 'Priority 1'))
q.put((3, 'Prioirty 3'))
q.put((4 ,'Priority 4'))
q.put((2 ,'Priority 2'))




for i in range(q.qsize()):
    print(q.get()[1])
    
'''


#EVENTS and EVENT OBJECTS

'''
event = threading.event()

event.set() #set flag to true

event.clear()   #set flag to false

event.wait()    #waits until event.set is true or event.set is called

event.is_set()  #checks if event.set is true
'''
'''
def flag():
    
    time.sleep(3)
    event.set()
    print("Starting Countdown..")
    time.sleep(7)
    print("Event is cleared..")
    event.clear()


def start_operations():
    
    event.wait()
    
    while event.is_set():
        
        print("Starting random integer task")
        x = np.random.randint(1,30)
        time.sleep(0.5)
        if x == 29:
            
            print("True")
            
    print("Event has been cleared, random operation stops..")
    
    
    
event = threading.Event()

t1 = threading.Thread(target = flag)
t2 = threading.Thread(target = start_operations)

t1.start()
t2.start()

'''


#DOWNLOADING IMAGES USING DIFFERENT THREADINGS

#MULTI THREADING

import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from threading import Thread




SAVE_DIR = r'C:\Users\Raunak\Desktop\Puppy_threading'



def decorator_function(func):
    def wrapper(*args,**kwargs):
        session = requests.Session()
        retry = Retry(connect=0, backoff_factor=0.2)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        return func(*args, session = session, **kwargs)
    return wrapper








#Using threading:
image_count = 0

#optional decorator_function
#@decorator_function   
def download_image(SAVE_DIR,q, session = None):
        global image_count
        if not session:
                session = requests.Session()
        while not q.empty():
            
            try:
                #timeout deals with faulty URL's
                    r = session.get(q.get(block = False), timeout = 3)

            except (requests.exceptions.RequestException, UnicodeError) as e:
                print(e)
                image_count += 1
                q.task_done()
                continue

            image_count += 1
            q.task_done()

            print('image', image_count)
            with open(os.path.join(
                        SAVE_DIR, 'image_{}.jpg'.format(image_count)),
                        'wb') as f:

                f.write(r.content)
                
               

q =queue.Queue()
with open(r'C:\Users\Raunak\Desktop\puppies.txt', 'rt') as f:
    for i in range(200):
        line = f.readline()
        q.put(line.strip())
print(q.qsize())


threads = []
start = time.time()
for i in range(20):
     t = Thread(target = download_image, 
                args = (SAVE_DIR,q))
     #t.setDaemon(True)
     threads.append(t)
     t.start()
q.join()

for t in threads:
    t.join()
    print(t.name, 'has joined')

end = time.time()
print('time taken: {:.4f}'.format(end - start))


#time taken: 7.4640
#time taken: 5.0860





















