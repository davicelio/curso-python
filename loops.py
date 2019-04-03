#bucles for & while

foods = ['apples', 'bread','cheese','milk','bananas']

for food in foods:
    if food == 'bread':
        print('tienes que comprar: '+ food)
        break
    else: 
        print(food)



for letter in 'hellow':
    print(letter)


count = 4
while count <= 10:
    print(count)
    count = count + 1