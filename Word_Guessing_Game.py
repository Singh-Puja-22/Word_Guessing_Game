import random

animals=['elephant', 'bear', 'cheetah', 'giraffe',
         'wolf', 'tiger', 'penguin', 'rabbit', 'lion',
         'monkey', 'rhinoceros', 'sheep', 'kangaroo',
         'zebra']
fruits=['apple', 'banana', 'grapes', 'mango', 'lime',
        'watermelon', 'jackfruit', 'guava', 'orange',
        'papaya', 'pear', 'peach', 'pomegranate',
        'strawberry']
stationary=['pencil', 'eraser', 'sharpner', 'envelope',
            'paper', 'stapler', 'folder', 'maker',
            'inkpot', 'calculator', 'glue', 'notebook',
            'scissors', 'ruler']

while 1:
    words= animals + fruits + stationary

    random_word = random.choice(words)
    print("Word Guessing Game")

    if random_word in animals:
        print("Hint: It is an animal")
    elif random_word in fruits:
        print("Hint: It is a fruit")
    else:
        print("Hint: It is a stationary")

    user_guesses = ''
    chances = 5

    while chances > 0:
        wrong_guess = 0
        for ch in random_word:
            if ch in user_guesses:
                print(ch, end=' ')
            else:
                wrong_guess+=1
                print("_", end=' ')

        if wrong_guess == 0:
            print('\nCongrates. You Win. The word is ',random_word)
            again= input('Would you like to paly again?(Y or N) : ')
            if again in 'Yy':
                break
            else:
                quit()
    
        guess = input('\nMake a guess : ')
        user_guesses+=guess

        if guess not in random_word:
            chances-=1
            print(f'wrong. You have {chances} more chances')
            if chances == 0:
                print('Game Over. You Lose, The word is ',random_word)
                restart= input('Would you like to restart?(Y or N) : ')
                if restart in 'Nn':
                    quit()
