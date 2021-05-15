
sudo = [
    9,0,2,  4,1,5,  0,0,0,
    0,0,5,  0,6,0,  0,0,0,
    3,7,0,  0,0,0,  0,6,1,
               
    2,1,0,  3,9,6,  0,0,5,
    4,0,6,  0,0,0,  0,0,2,
    0,0,3,  0,8,0,  0,9,0,
               
    6,4,9,  0,3,1,  0,5,7,
    5,0,0,  6,0,0,  0,0,4,
    8,0,7,  5,0,9,  0,0,0
    
]


arr = [[]] * 81

for i in range(81):
    if sudo[i] != 0:
        arr[i] = [sudo[i]]
    else:
        arr[i] = list(range(1,10))
    
    #print(len(arr[i]))    


for j in range(81):
    if len(arr[j]) == 1:
        print(arr[j])
    elif sudo[] 
        
      


