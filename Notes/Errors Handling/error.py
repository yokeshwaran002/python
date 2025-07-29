a="something error"
try:
    print(a)
except:
    print("something error")
    
try:
    print(a)
except NameError:
    print("name error")
except:
    print("something error")
    
try:
    print(a)
except:
    print("something error")
else:
    print("something wrong")
    
try:
    print(a)
except:
    print("something")
finally:
    print("finished")