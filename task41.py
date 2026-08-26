'''Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color':
'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]'''
original_list=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color':
'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
original_list.sort(key=lambda x: int (x['model']))
print(original_list)