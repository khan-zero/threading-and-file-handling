import threading, os


def ct_vowels_from_files(fn): #ct : means count, fn : means file name

    count = 0
    with open(fn, "r") as file:
        for i in file.read():
            if i in "euioa":
                 count += 1  
    
    print(f"count of vowels in {fn}: {count}")
    #return f"count of vowels in {fn}: {count}"



"""\___________| main code |______________/"""

for i in os.listdir():
    #print(f"file from <{os.getcwd()}>: {i}")
    #x = ct_vowels_from_files(i)
    #print(x)
    
    t1 = threading.Thread(target=ct_vowels_from_files, args=(i,))
    t1.start()
    #print(t1)
    t1.join()
    
print("Program was ended")
























































'''
def myfunc1():
    a = 10
    while a >= 0:
        print(f"While: {a}")
        time.sleep(0.5)        
        a-=1
        
def myfunc2():
    for i in range(10):
        time.sleep(0.5)
        print(f"for: {i}")
        
t1 = threading.Thread(target=myfunc1)
t2 = threading.Thread(target=myfunc2)

t1.start()
t2.start()

t1.join()
t2.join()
'''
