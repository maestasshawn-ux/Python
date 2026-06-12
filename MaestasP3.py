# MaestasP3
# Programmer: Shawn Maestas
# Email: smaestas52@student.cnm.edu
# Purpose: provides user capability to find fruit in a string
# Python Version:3.14.5

fruits = ('Apricot', 'Asian Pear', 'Avocado', 'Banana', 'Blackberries', 'Blueberries', 'Boysenberries', 'Cactus Pear', 'Cantaloupe', 'Cherries', 'Coconut', 'Cranberries', 'Figs', 'Gooseberries', 'Grapefruit', 'Grapes', 'Honeydew Melon', 'Kiwifruit', 'Limes', 'Longan', 'Loquat', 'Lychee', 'Madarins', 'Malanga', 'Mandarin Oranges', 'Mangos', 'Mulberries', 'Nectarines', 'Oranges', 'Papayas', 'Passion Fruit', 'Peaches', 'Pears', 'Persimmons', 'Pineapple', 'Plums', 'Pomegranate', 'Prunes', 'Quince', 'Raisins', 'Raspberries', 'Rhubarb', 'Strawberries', 'Tangelo', 'Tangerines', 'Tomato', 'Ugli Fruit', 'Watermelon')

#Solve for single and double worded fruits
double_word_fruit = []
single_word_fruits = []
for fruit in fruits:
    if fruit.find(' ') >= 1:
        double_word_fruit.append(fruit)
    else:
        single_word_fruits.append(fruit)

#Sentence input from the user
sentence = input('Please type out a sentence.'\
                 '\nTry to include some fruits in your sentence!: ')

#determining how many fruits the user provided are in the list
refined_sentence = sentence.replace(',', '').replace('.', '').replace('!','').replace('?','')
matching_fruits = []
for fruit in fruits:
    if fruit in refined_sentence:
        matching_fruits.append(fruit)
    elif fruit.endswith('s') and fruit[:-1] in refined_sentence:
        fruit_singular1 = fruit[:-1]
        matching_fruits.append(fruit_singular1)
    elif fruit.endswith('ies') and fruit[:-3] + 'y' in refined_sentence:
        fruit_singular = fruit[:-3] + 'y'
        matching_fruits.append(fruit_singular)

#formatting the matching fruits to reflect the order found in the sentence
sentence_ordered_fruits = matching_fruits.copy()
sentence_ordered_fruits.sort(key=lambda x: refined_sentence.find(x))

#Display to the user how many fruits from the sentence are in the list.
print(f'\nyour sentence contains {len(matching_fruits)} fruits that are in the list:\n {(sentence_ordered_fruits)}')

#replacing the first matching fruit with Brussel Sprouts
vegitable_addin = sentence.replace(sentence_ordered_fruits[0], 'Brussel Sprouts')

#Display new sentence to the user:
print(f'\nYour sentence with {sentence_ordered_fruits[0]} replaced as a vegitable:\n')

if sentence_ordered_fruits[0].endswith('s'):
    print(vegitable_addin)
else:
    print(vegitable_addin.replace('Brussel Sprouts', 'Brussel Sprout'))