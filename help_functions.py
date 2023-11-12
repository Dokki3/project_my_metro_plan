from data import lines


def find_number_line(station: str):
    for i in lines:
        if station in lines[i]:
            return i


if __name__ == '__main__':
    print(find_number_line("Сходненская"))