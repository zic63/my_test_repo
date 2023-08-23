names = ['Larry', 'Kehrly', 'Moo', 'Bubby', 'Scanny']
#it's just for test digga
#it's just for second test digga

def num_of_idiots(names_list):
    example_dict = {1: 'One',
                  2: 'Two',
                  3: 'Three',
                  4: 'Four',
                  5: 'Five'}
    
    return example_dict[len(names_list)]
message = f'{num_of_idiots(names)} idiots: '

for index, name in enumerate(names, start=1):
    if index > 1 and index != len(names):
        message += ', '
    if index == len(names):
        message += ' and '
    message += name
print(message)
