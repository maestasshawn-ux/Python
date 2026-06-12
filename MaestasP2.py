# MaestasP2
# Programmer: Shawn Maestas
# Email: smaestas52@student.cnm.edu
# Purpose: provides user capability to view contact info
# Python Version: 3.14.5
#Initial statement:
print("By entering your state, this program will output it's captial, number of congressional districts, and the order it joined the union.\n")


#Lists for the states, capitals, number of congressional districts, the order the state joined the union, and the endings
#Each list is sorted in 10s
states = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 
          'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
          'Massachusetts','Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
          'New Mexico','New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
          'South Dakota','Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')

capitals = ('Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta',
            'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis',
            'Boston', 'Lansing', 'St. Paul', 'Jackson', 'Jefferson City', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton',
            'Santa Fe', 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence', 'Columbia',
            'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne')

congressional_districts = [7, 1, 8, 4, 53, 7, 5, 1, 25, 13,
                           2, 2, 19, 9, 5, 4, 6, 7, 2, 8,
                           10, 15, 8, 4, 9, 1, 3, 3, 2, 13,
                           3, 29, 13, 1, 18, 5, 5, 19, 2, 6,
                           1, 9, 32, 3, 1, 11, 9, 3, 8, 1]

union_order = (22, 49, 48, 25, 31, 38, 5, 1, 27, 4,
               50, 43, 21, 19, 29, 34, 15, 18, 23, 7,
               6, 26, 32, 20, 24, 41, 37, 36, 9, 3,
               47, 11, 12, 39, 17, 46, 33, 2, 13, 8,
               40, 16, 28, 45, 14, 10, 42, 35, 30, 44)

sorted_union_order =sorted(union_order)

endings = ['st', 'nd', 'rd'] + 17*['th'] + ['st', 'nd', 'rd'] + 7*['th'] + ['st', 'nd', 'rd'] + 7*['th'] + ['st', 'nd', 'rd'] + 7*['th']


#Below is an error check to ensure the sum of the congressional districts matches the total.
# print(sum(congressional_districts)==435)


#variables
state = input('What is your selected state?: ')
indexed_state = states.index(state)
capital = capitals[indexed_state]
state_districts = congressional_districts[indexed_state]
joined_union = union_order[indexed_state]
indexed_union_placement = sorted_union_order.index(joined_union)
appropriate_ending = endings[indexed_union_placement]


#Statements to the user
print(f'\nThe capital of {state} is {capital}.')
print(f'{state} has {state_districts} congressional districts.')
print(f'{state} was the {str(joined_union)+appropriate_ending} state to join the union!')