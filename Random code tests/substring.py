test_list = ['NINE', 'Geeky', 'Computers', 'Algorithms'] 
  
 
print ("The original list is : " + str(test_list)) 
  

subs = 'ELEPHANTINE  '
chars = set('NINE')
if any((c in chars) for c in test_list):
    print('Found')
else:
    print('Not Found')
