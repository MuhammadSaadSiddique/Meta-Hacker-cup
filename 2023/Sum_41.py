import itertools


def chkproduct(combination, P):
    product = 1
    for num in combination:
        product *= num
    if product == P:
        return combination
    else:
        return -1

def backtrack(
    candidates: list, path: list, answer: list, target: int, previous_index: int
) -> None:
    """
    A recursive function that searches for possible combinations. Backtracks in case
    of a bigger current combination value than the target value.

    Parameters
    ----------
    previous_index: Last index from the previous search
    target: The value we need to obtain by summing our integers in the path list.
    answer: A list of possible combinations
    path: Current combination
    candidates: A list of integers we can use.
    """
    if target == 0:
        s=chkproduct(path, P)
        if s!=-1:
            answer.append(path.copy())
    else:
        for index in range(previous_index, len(candidates)):
            if target >= candidates[index]:
                path.append(candidates[index])
                backtrack(candidates, path, answer,
                          target - candidates[index], index)
                path.pop(len(path) - 1)


def combination_sum(candidates: list, target: int) -> list:
    """
    >>> combination_sum([2, 3, 5], 8)
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    >>> combination_sum([2, 3, 6, 7], 7)
    [[2, 2, 3], [7]]
    >>> combination_sum([-8, 2.3, 0], 1)
    Traceback (most recent call last):
        ...
    RecursionError: maximum recursion depth exceeded in comparison
    """
    path = []  # type: list[int]
    answer = []  # type: list[int]
    backtrack(candidates, path, answer, target, 0)
    return answer
import math
def divisorGenerator(n):
    large_divisors = []
    large_divisors = []
    if n==1:
        s=2
    elif (n < 42):
        s = n
    else:
        s = 42
    for i in range(1, int(s)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        if divisor < 42:
            yield int(divisor)
def find_array(P):
    res = list(divisorGenerator(P))
    
    combinations = combination_sum(res, 41)
    # print(combinations)
    if combinations == []:
        return -1
    else:
        combinations.sort(key=len) # for lesest combination
        return combinations[0] 
    return -1


def write(res):
    with open("2sum_41_chapter_1_input_output.txt", "a") as b:
        b.write(res+"\n")


with open("2sum_41_chapter_1_input.txt", "r") as f:
    T = int(f.readline().strip())
    for i in range(T):
        P = int(f.readline().strip())
        
        array = find_array(P)
        if array == -1:
            print("Case #{}: -1".format(i+1))
            write("Case #{}: -1".format(i+1))
        else:
            N = len(array)
            print("Case #{}: {} {}".format(i+1, N, " ".join(str(x) for x in array)))
            write("Case #{}: {} {}".format(i+1, N, " ".join(str(x) for x in array)))


