from data import lines


def find_number_line(station: str):
    for i in lines:
        if station in lines[i]:
            return i


def find_repeats(lst: list) -> bool:
    for i in lst:
        if lst.count(i) != 1:
            return True
    return False


def find_line_to_line(lst: list) -> bool:
    for i in lst:
        if len(i) != 1 and find_repeats(i):
            return True


if __name__ == '__main__':
    list_line_result = [[1, 2, 3], [9, 10, 9, 12], [3, 2, 3]]
    integer = 0
    while find_line_to_line(list_line_result):
        if find_repeats(list_line_result[integer]):
            list_line_result.pop(integer)
        else:
            integer += 1
    print(list_line_result)
