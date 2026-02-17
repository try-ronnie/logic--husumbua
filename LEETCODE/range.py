def get_list(num:list):
    for one in range(len(num)):
        print (f'{one}') 

# when range is used like this it gives the indeces
# but to use the actuall value youll have to update the code further abit

def get_list(num:list):
    for one in range(len(num)):
        value = num[one]
        print (f'{one}') 
# vaue here is a variable thats used to store the looped value in the list not the index



get_list( [2,4,56,7,7,8,8] )
