""" Finding number in a given list using binary searching technique """

from random import randint


def element_search(input_list, number):
    ordered_list = sorted(list(set(input_list)))  # excluding duplicates and sorting
    new_elem = ordered_list[len(ordered_list) // 2]
    while not len(ordered_list) == 1:
        new_index = ordered_list.index(new_elem)
        if number < new_elem:
            ordered_list = ordered_list[:new_index]
            new_elem = ordered_list[len(ordered_list) // 2]
        elif number > new_elem:
            ordered_list = ordered_list[new_index:]
            new_elem = ordered_list[len(ordered_list) // 2]
        else:
            return True
    if ordered_list[0] == number:
        return True
    return False


if __name__ == '__main__':
    a = [randint(0, 100) for _ in range(randint(5, 20))]
    num = randint(0, 100)
    print(sorted(list(set(a))))
    print(num)
    print(element_search(a, num))
