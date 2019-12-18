"""
Polish:
Napisać program, który pozwoli użytkownikowi:
1) Dodawać nowe definicje
2) Szukać istniejących definicji
3) Usuwać wybrane przez niego definicje
"""
# definitions = dict(key="definition")
# key = list(definitions.keys())[list(definitions.values()).index(definition)] - search for a key by value


def run(**kwargs):
    while True:
        print("1: Add a new word")
        print("2: Search for a definition")
        print("3: Delete selected word")
        print("4: Print actual dictionary")
        print("5: Exit")
        try:
            inp = int(input('What do You want to do? '))
            if inp == 1:
                key = input('Enter a key (word) to define: ').lower()
                while key in kwargs.keys():
                    print(f'The definition of "{key}" already exists. ', end='')
                    key = input('Enter another key to define: ').lower()
                definition = input(f'Give the definition of "{key}": ')
                kwargs[key] = definition
                print(f'Definition of "{key}" has been added to the dictionary\n')
            elif inp == 2:
                key = input('What word do You want to find? ').lower()
                if key in kwargs.keys():
                    definition = kwargs[key]
                    print(f'"{key}" is {definition}\n')
                else:
                    print(f'"{key}" has not been found in the dictionary. ', end='')
                    q = input('Do You want to add this word (yes/no)? ').lower()
                    if q == 'yes':
                        definition = input(f'Give the definition for "{key}": ')
                        kwargs[key] = definition
                        print(f'Definition of "{key}" has been added to the dictionary\n')
                    elif q == 'no':
                        print('As You wish...\n')
                    else:
                        print("Don't understand...\n")
            elif inp == 3:
                key = input('What word do You want to delete from the dictionary? ').lower()
                if key in kwargs.keys():
                    del kwargs[key]
                    print(f'Definition of "{key}" has been deleted from the dictionary\n')
                else:
                    print(f'"{key}" has not been found in the dictionary\n')
            elif inp == 4:
                print(f'The actual dictionary looks like:\n{kwargs}\n')
            elif inp == 5:
                print('See You next time!')
                break
            else:
                print("Don't understand. Please, make the right choice")
        except ValueError:
            print('Please, enter an integer!\n')


if __name__ == '__main__':
    run()
