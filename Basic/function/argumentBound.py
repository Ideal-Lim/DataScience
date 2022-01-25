import copy

# 함수 인자
def append_element(list, element):
    list.append(element)

def append_element2(list, element):
    list1 = copy.deepcopy(list)
    print(id(list))
    print(id(list1))
    list1.append(element)
    return list1


def test(num):
    num = num + 1 # 지역변수 num

    return num

def test2(num):
    print(id(num))
    num = num + 1
    print(id(num))


if __name__ == "__main__":
    data = [1, 2, 3]
    #1
    print(id(data))
    append_element(data, 4)
    print(data) # [1, 2, 3, 4]
    #2
    print(id(data)) # 1, 2 are same

    num = 0
    print(id(num))
    test(num)
    print(num) # 0
    test2(num)
    print(num) # 0

    data1 = [4, 5, 6]
    append_element2(data1, 7)
    print(data1) # [4, 5, 6]
