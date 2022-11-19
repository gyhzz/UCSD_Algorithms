import random
random.seed(1000)
random_len = (2, 100)
random_digit = (1, 100000)


def correct_sol(int_list):

    result = 0

    for index1 in range(len(int_list)):
        for index2 in range(len(int_list)):
            
            if index1 != index2 and int_list[index1] * int_list[index2] > result:
                result = int_list[index1] * int_list[index2]

    return result


def correct_sol_fast(int_list):

    big1 = 0
    big2 = 0
    big1_index = 0

    for i in range(len(int_list)):
        if int_list[i] > big1:
            big1 = int_list[i]
            big1_index = i

    for j in range(len(int_list)):
        if int_list[j] > big2 and j != big1_index:
            big2 = int_list[j]

    return big1 * big2


def generate_random_list(count):

    return [random.randint(*random_digit) for i in range(count)]



if __name__ == '__main__':
    
    list_len = int(input())
    input_list = input().split()
    list_of_int = list(map(int, input_list))

    # # Generate test
    # correct = True
    
    # while correct:

    #     list_len = random.randint(*random_len)
    #     list_of_int = generate_random_list(list_len)

    #     result1 = correct_sol(list_of_int)
    #     result2 = correct_sol_fast(list_of_int)

    #     print(list_of_int)
    #     print(result1, result2)

    #     if result1 != result2:
    #         correct = False
    #         print('Wrong')
    #     else:
    #         print('Ok')
        
    #     print()

    print(correct_sol_fast(list_of_int))