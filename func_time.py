from data import data


def determining_the_time(route_: list) -> int:
    summ = 0
    try:
        for j in route_:
            try:
                if j != route_[-1]:
                    summ += data[(j, route_[route_.index(j) + 1])]
            except KeyError:
                if j != route_[-1]:
                    summ += data[(route_[route_.index(j) + 1], j)]
        return summ
    except KeyError:
        return 500


if __name__ == '__main__':
    route = [['Красносельская', ]]
    print(determining_the_time(['Сокольники', 'Красносельская']))
    route.sort(key=determining_the_time)
    print(route)
