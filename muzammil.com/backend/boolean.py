print(bool(""))
print(bool("Hello"))
print(bool(0))
print(bool(25.5))
print(bool(None))
print(bool([]))

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

True_value = True
False_value = False