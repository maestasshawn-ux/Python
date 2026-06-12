# MaestasP4
# Programmer: Shawn Maestas
# Email: smaestas52@student.cnm.edu
# Purpose: provides user capability to find fruit in a string
# Python Version: 3.14

#http://www.learnspanishtoday.com/learning_module/grammar.htm
english2spanish={'Good morning.':'Buenos días.',
'Good afternoon.':'Buenas tardes.',
'Good evening. (greeting)':'Buenas noches.',
'Hello, my name is John.':'Hola, me llamo Juan.',
'What is your name?':'¿Cómo se llama usted?',
'How are you?':'¿Cómo está usted?',
'I am fine.':'Estoy bien.',
'Nice to meet you.':'Mucho gusto.',
'Goodbye.':'Adiós.',
'See you later.':'Hasta luego.',
'I am lost. Where is the restroom?':'Estoy perdido. ¿Dónde está el baño?',
'Excuse me.':'Con permiso. OR Perdóname',
'Please.':'Por favor.',
'Thank you.':'Gracías.',
'Bless you.':'Salud.',
'You are welcome (it was nothing).':'De nada.',
'How much does it cost?':'¿Cuánto cuesta?',
'How many are there?':'¿Cuántos hay?',
'There are many.':'Hay muchos.',
'Do you want to buy this?':'¿Quiere comprarlo usted?',
'What time is it?':'¿Qué hora es?',
'How do you say maybe in Spanish?':'¿Cómo se dice maybe en Español?',
'Yes.':'Sí.',
'No.':'No.',
'I do not understand.':'Yo no comprendo.',
'Would you speak slower, please.':'Por favor, habla mas despacio.',
'Who?':'¿Quièn?',
'Why?':'¿Por què?'}

#present the list of phrases to the user and assign a number to each
print("Below is a list of English phrases to translate to Spanish:\n")
print("Available phrases:")
numerical_list = []
for english_phrase in english2spanish.keys():
    numerical_list.append(english_phrase)
    print(numerical_list.index(english_phrase), "-", english_phrase)

# Prompt user for a phrase and validate input
user_selection = input("\nEnter a number from the list: ")
while True:
    if user_selection.isdigit():
        user_selection = int(user_selection)
        if user_selection <0 or user_selection >= len(numerical_list):
            print("\nInvalid selection.")
            user_selection = input("\nEnter a number from the list: ")
        else:
            break
    else:
        print("\nInvalid selection. Please enter a number.")
        user_selection = input("\nEnter a number from the list: ")

#Translate the phrase to Spanish
print(f'\nThe Spanish translation of "{numerical_list[user_selection]}" is: \n{english2spanish[numerical_list[user_selection]]}')

#Request if the user would like to make another selection
while True:
    follow_up_request = input('Would you like to translate another phrase? (yes or no):').lower()
    if follow_up_request == 'yes':
        print('\nAvailable phrases')
        for english_phrase in english2spanish.keys():
            print(numerical_list.index(english_phrase), "-", english_phrase)
        user_selection = input("\nEnter a number from the list: ")
        while True:
            if user_selection.isdigit():
                user_selection = int(user_selection)
                if user_selection <0 or user_selection >= len(numerical_list):
                    print("\nInvalid selection.")
                    user_selection = input("\nEnter a number from the list: ")
                else:
                    print(f'\nThe Spanish translation of "{numerical_list[user_selection]}" is: \n{english2spanish[numerical_list[user_selection]]}\n')
                    break
            else:
                print("\nInvalid selection. Please enter a number.")
                user_selection = input("\nEnter a number from the list: ")
    elif follow_up_request == 'no':
        print('\nThank you for using this program!')
        break
    else:
        print('Invalid selection. Please enter "yes" or "no".')