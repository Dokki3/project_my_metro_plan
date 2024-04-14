from functools import cache

import time

from data import five2, trans, lines


# алгоритм построения маршрута

def plotting_a_route(station1: str, line1: int or str, station2: str, line2: int or str, lines) -> list:
    line_fixed_1 = line1
    line_fixed_2 = line2
    line_result = []
    # маршрут для одной линии
    try:
        line = lines[line1]
        if line1 == 5:
            match line[line.index(station1):line.index(station2):]:
                case []:
                    line = line[::-1]
                    line_result.append(line[line.index(station1):line.index(station2) + 1:])
                case _:
                    line_result.append(line[line.index(station1):line.index(station2) + 1:])
            line = five2
            match line[line.index(station1):line.index(station2):]:
                case []:
                    line = line[::-1]
                    line_result.append(line[line.index(station1):line.index(station2) + 1:])
                case _:
                    line_result.append(line[line.index(station1):line.index(station2) + 1:])
        else:
            match line[line.index(station1):line.index(station2):]:
                case []:
                    line = line[::-1]
                    line_result.append(line[line.index(station1):line.index(station2) + 1:])
                case _:
                    line_result.append(line[line.index(station1):line.index(station2) + 1:])
    except ValueError:
        pass
    '''
    # маршрут для 4 линии
    if line1 == 4 and line2 == '4A':
        line = lines[line1]
        if line[line.index(station1):8:] == []:
            line = line[::-1]
            line = line[line.index(station1):4:]
            for i in lines[line2]:
                    line.append(i)
        else:
            line = lines[line1][line.index(station1):8:]
            for i in lines[line2]:
                    line.append(i)
        line_result.append(line[:line.index(station2) + 1:])
    elif line1 == '4A' and line2 == 4:
        line = lines[line1]
        if line[line.index(station1):1:] == []:
            line = line[::-1]
            line = line[line.index(station1):3:]
            if 7 > lines[line2].index(station2):
                for i in lines[line2][:8:][::-1]:
                        line.append(i)
            else:
                for i in lines[line2][7:lines[line2].index(station2) + 1:]:
                        line.append(i)
        else:
            line = lines[line1][line.index(station1):1:]
            if 7 > lines[line2].index(station2):
                for i in lines[line2][:8:][::-1]:
                    line.append(i)
            else:
                for i in lines[line2][7:lines[line2].index(station2) + 1:]:
                    line.append(i)
        line_result.append(line[:line.index(station2) + 1:])'''
    # маршруты двух вариантов (больше одной линии)
    # находим маршрут с одной пересадкой
    try:
        tr_ = trans[line_fixed_1][line_fixed_2]
        for j in tr_:
            tr = [j]
            # находим массив станций для 1-ой линии
            if line1 == 5:
                for line in [lines[line1], five2]:
                    try:
                        match line[line.index(station1):line.index(tr[0][0]) + 1:]:
                            case []:
                                line = line[line.index(station1):line.index(tr[0][0]):-1]
                                line.append(tr[0][0])
                            case _:
                                line = line[line.index(station1):line.index(tr[0][0]) + 1:]
                        # находим массив станций для 2-ой линии
                        line_ = lines[line2]
                        match line_[line_.index(tr[0][1]):line_.index(station2) + 1:]:
                            case []:
                                line_ = line_[line_.index(tr[0][1]):line_.index(station2):-1]
                                line_.append(station2)
                            case _:
                                line_ = line_[line_.index(tr[0][1]):line_.index(station2) + 1:]
                        result = line + line_
                        for r1 in result:
                            if result.count(r1) > 1:
                                break
                        else:
                            line_result.append(result)
                    except ValueError:
                        continue
            if line2 == 5:
                for line_ in [lines[line1], five2]:
                    try:
                        line = lines[line1]
                        match line[line.index(station1):line.index(tr[0][0]) + 1:]:
                            case []:
                                line = line[line.index(station1):line.index(tr[0][0]):-1]
                                line.append(tr[0][0])
                            case _:
                                line = line[line.index(station1):line.index(tr[0][0]) + 1:]
                        # находим массив станций для 2-ой линии
                        match line_[line_.index(tr[0][1]):line_.index(station2) + 1:]:
                            case []:
                                line_ = line_[line_.index(tr[0][1]):line_.index(station2):-1]
                                line_.append(station2)
                            case _:
                                line_ = line_[line_.index(tr[0][1]):line_.index(station2) + 1:]
                        result = line + line_
                        for r1 in result:
                            if result.count(r1) > 1:
                                break
                        else:
                            line_result.append(result)
                    except ValueError:
                        continue
            else:
                line = lines[line1]
                match line[line.index(station1):line.index(tr[0][0]) + 1:]:
                    case []:
                        line = line[line.index(station1):line.index(tr[0][0]):-1]
                        line.append(tr[0][0])
                    case _:
                        line = line[line.index(station1):line.index(tr[0][0]) + 1:]
                # находим массив станций для 2-ой линии
                line_ = lines[line2]
                match line_[line_.index(tr[0][1]):line_.index(station2) + 1:]:
                    case []:
                        line_ = line_[line_.index(tr[0][1]):line_.index(station2):-1]
                        line_.append(station2)
                    case _:
                        line_ = line_[line_.index(tr[0][1]):line_.index(station2) + 1:]
                result = line + line_
                for r1 in result:
                    if result.count(r1) > 1:
                        break
                else:
                    line_result.append(result)
    except KeyError:
        pass
    # находим все маршруты с двумя пересадками
    try:
        tr1 = []
        tr2 = []
        #
        for i in trans[line1].keys():
            try:
                tr1 = trans[line_fixed_1][i]
                tr2 = trans[i][line_fixed_2]
                line2, line3 = i, line_fixed_2
                line = lines[line1]
                if len(tr1) != 1:
                    size = []
                    for j in tr1:
                        try:
                            if line_fixed_1 == 5:
                                for line in [lines[line1], five2]:
                                    match line[line.index(station1):line.index(j[0]) + 1:]:
                                        case []:
                                            l = line[line.index(station1):line.index(j[0]):-1]
                                            l.append(j[0])
                                            size.append(len(l))
                                        case None:
                                            size.append(1)
                                        case _:
                                            size.append(len(line[line.index(station1):line.index(j[0]) + 1:]))
                            else:
                                match line[line.index(station1):line.index(j[0]) + 1:]:
                                    case []:
                                        l = line[line.index(station1):line.index(j[0]):-1]
                                        l.append(j[0])
                                        size.append(len(l))
                                    case None:
                                        size.append(1)
                                    case _:
                                        size.append(len(line[line.index(station1):line.index(j[0]) + 1:]))
                        except ValueError:
                            continue
                    min_tr = size.index(min(size))
                    tr1 = [tr1[min_tr]]
                else:
                    if tr1[0][0] == tr2[0][1]:
                        continue
                line_ = lines[line2]
                if len(tr2) != 1:
                    size = []
                    for j in tr2:
                        try:
                            if j[1] != tr1[0][0]:
                                if line2 == 5:
                                    for line_ in [lines[line2], five2]:
                                        match line_[line_.index(tr1[0][1]):line_.index(j[0]) + 1:]:
                                            case []:
                                                l = line_[line_.index(tr1[0][1]):line_.index(j[0]):-1]
                                                l.append(j[0])
                                                size.append(len(l))
                                            case None:
                                                size.append(1)
                                            case _:
                                                size.append(len(line_[line_.index(tr1[0][1]):line_.index(j[0]) + 1:]))
                                else:
                                    match line_[line_.index(tr1[0][1]):line_.index(j[0]) + 1:]:
                                        case []:
                                            l = line_[line_.index(tr1[0][1]):line_.index(j[0]):-1]
                                            l.append(j[0])
                                            size.append(len(l))
                                        case None:
                                            size.append(1)
                                        case _:
                                            size.append(len(line_[line_.index(tr1[0][1]):line_.index(j[0]) + 1:]))
                            else:
                                size.append(300)
                        except ValueError:
                            continue
                    if len(size) == 2:
                        min_tr = size.index(min(size))
                        tr2 = [tr2[min_tr]]
                    else:
                        min_tr = size.index(min(size))
                        if min_tr == (0 | 2):
                            line_ = lines[line2]
                        else:
                            line_ = five2
                        tr2 = [tr2[min_tr]]
                # находим массив станций для 1-ой линии
                if line1 == 5:
                    for line in [lines[line1], five2]:
                        try:
                            match line[line.index(station1):line.index(tr1[0][0]) + 1:]:
                                case []:
                                    line = line[line.index(station1):line.index(tr1[0][0]):-1]
                                    line.append(tr1[0][0])
                                case _:
                                    line = line[line.index(station1):line.index(tr1[0][0]) + 1:]
                            # находим массив станций для 2-ой линии
                            match line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]:
                                case []:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]):-1]
                                    line_.append(tr2[0][0])
                                case _:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]
                            # находим массив станций для 3-ой линии
                            line_1 = lines[line3]
                            match line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]:
                                case []:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2):-1]
                                    line_1.append(station2)
                                case _:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]
                            result = line + line_ + line_1
                            for r1 in result:
                                if result.count(r1) > 1:
                                    break
                            else:
                                line_result.append(result)
                        except ValueError:
                            continue
                if line2 == 5:
                    for line_ in [lines[line2], five2]:
                        try:
                            line = lines[line1]
                            match line[line.index(station1):line.index(tr1[0][0]) + 1:]:
                                case []:
                                    line = line[line.index(station1):line.index(tr1[0][0]):-1]
                                    line.append(tr1[0][0])
                                case _:
                                    line = line[line.index(station1):line.index(tr1[0][0]) + 1:]
                            # находим массив станций для 2-ой линии
                            match line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]:
                                case []:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]):-1]
                                    line_.append(tr2[0][0])
                                case _:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]
                            # находим массив станций для 3-ой линии
                            line_1 = lines[line3]
                            match line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]:
                                case []:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2):-1]
                                    line_1.append(station2)
                                case _:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]
                            result = line + line_ + line_1
                            for r1 in result:
                                if result.count(r1) > 1:
                                    break
                            else:
                                line_result.append(result)
                        except ValueError:
                            continue
                if line3 == 5:
                    for line_1 in [lines[line3], five2]:
                        try:
                            line = lines[line1]
                            match line[line.index(station1):line.index(tr1[0][0]) + 1:]:
                                case []:
                                    line = line[line.index(station1):line.index(tr1[0][0]):-1]
                                    line.append(tr1[0][0])
                                case _:
                                    line = line[line.index(station1):line.index(tr1[0][0]) + 1:]
                            # находим массив станций для 2-ой линии
                            match line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]:
                                case []:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]):-1]
                                    line_.append(tr2[0][0])
                                case _:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]
                            # находим массив станций для 3-ой линии
                            match line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]:
                                case []:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2):-1]
                                    line_1.append(station2)
                                case _:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]
                            result = line + line_ + line_1
                            for r1 in result:
                                if result.count(r1) > 1:
                                    break
                            else:
                                line_result.append(result)
                        except ValueError:
                            continue
                else:
                    line = lines[line1]
                    match line[line.index(station1):line.index(tr1[0][0]) + 1:]:
                        case []:
                            line = line[line.index(station1):line.index(tr1[0][0]):-1]
                            line.append(tr1[0][0])
                        case _:
                            line = line[line.index(station1):line.index(tr1[0][0]) + 1:]
                    # находим массив станций для 2-ой линии
                    line_ = lines[line2]
                    match line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]:
                        case []:
                            line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]):-1]
                            line_.append(tr2[0][0])
                        case _:
                            line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]
                    # находим массив станций для 3-ой линии
                    line_1 = lines[line3]
                    match line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]:
                        case []:
                            line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2):-1]
                            line_1.append(station2)
                        case _:
                            line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]
                    result = line + line_ + line_1
                    for r1 in result:
                        if result.count(r1) > 1:
                            break
                    else:
                        line_result.append(result)
            except KeyError:
                continue
    except:
        pass
    # находим все маршруты с тремя пересадками
    try:
        tr1 = []
        tr2 = []
        tr3 = []
        #
        for i in trans[line1].keys():
            try:
                for p in trans[i].keys():
                    try:
                        tr1 = trans[line_fixed_1][i]
                        tr2 = trans[i][p]
                        tr3 = trans[p][line_fixed_2]
                        line2, line3, line4 = i, p, line_fixed_2
                        line = lines[line1]
                        if len(tr1) != 1:
                            size = []
                            for j in tr1:
                                try:
                                    match line[line.index(station1):line.index(j[0]) + 1:]:
                                        case []:
                                            l = line[line.index(station1):line.index(j[0]):-1]
                                            l.append(j[0])
                                            size.append(len(l))
                                        case None:
                                            size.append(1)
                                        case _:
                                            size.append(len(line[line.index(station1):line.index(j[0]) + 1:]))
                                except ValueError:
                                    continue
                            min_tr = size.index(min(size))
                            tr1 = [tr1[min_tr]]
                        else:
                            if tr1[0][0] == tr2[0][1]:
                                continue
                        line_2 = lines[line2]
                        if len(tr2) != 1:
                            size = []
                            for j in tr2:
                                try:
                                    if j[1] != tr1[0][0]:
                                        match line_2[line_2.index(tr1[0][1]):line_2.index(j[0]) + 1:]:
                                            case []:
                                                l = line_2[line_2.index(tr1[0][1]):line_2.index(j[0]) - 1:-1]
                                                l.append(j[0])
                                                size.append(len(l))
                                            case None:
                                                size.append(1)
                                            case _:
                                                size.append(len(line_2[line_2.index(tr1[0][1]):line_2.index(j[0]) + 1:]))
                                    else:
                                        size.append(300)
                                except ValueError:
                                    continue
                            min_tr = size.index(min(size))
                            tr2 = [tr2[min_tr]]
                        line_3 = lines[line3]
                        if len(tr3) != 1:
                            size = []
                            for j in tr3:
                                try:
                                    if j[1] != tr2[0][0]:
                                        match line_3[line_3.index(tr2[0][1]):line_3.index(j[0]) + 1:]:
                                            case []:
                                                l = line_3[line_3.index(tr2[0][1]):line_3.index(j[0]) - 1:-1]
                                                l.append(j[0])
                                                size.append(len(l))
                                            case None:
                                                size.append(1)
                                            case _:
                                                size.append(len(line_3[line_3.index(tr2[0][1]):line_3.index(j[0]) + 1:]))
                                    else:
                                        size.append(100)
                                except ValueError:
                                    continue
                            min_tr = size.index(min(size))
                            tr3 = [tr3[min_tr]]
                        # находим массив станций для 1-ой линии
                        line_1 = lines[line1]
                        match line_1[line_1.index(station1):line_1.index(tr1[0][0]) + 1:]:
                            case []:
                                line_1 = line_1[line_1.index(station1):line_1.index(tr1[0][0]):-1]
                                line_1.append(tr1[0][0])
                            case _:
                                line_1 = line_1[line_1.index(station1):line_1.index(tr1[0][0]) + 1:]
                        # находим массив станций для 2-ой линии
                        line_2 = lines[line2]
                        match line_2[line_2.index(tr1[0][1]):line_2.index(tr2[0][0]) + 1:]:
                            case []:
                                line_2 = line_2[line_2.index(tr1[0][1]):line_2.index(tr2[0][0]):-1]
                                line_2.append(tr2[0][0])
                            case _:
                                line_2 = line_2[line_2.index(tr1[0][1]):line_2.index(tr2[0][0]) + 1:]
                        # находим массив станций для 3-ой линии
                        line_3 = lines[line3]
                        match line_3[line_3.index(tr2[0][1]):line_3.index(tr3[0][0]) + 1:]:
                            case []:
                                line_3 = line_3[line_3.index(tr2[0][1]):line_3.index(tr3[0][0]):-1]
                                line_3.append(tr3[0][0])
                            case _:
                                line_3 = line_3[line_3.index(tr2[0][1]):line_3.index(tr3[0][0]) + 1:]
                        # находим массив станций для 3-ой линии
                        line_4 = lines[line4]
                        match line_4[line_4.index(tr3[0][1]):line_4.index(station2) + 1:]:
                            case []:
                                line_4 = line_4[line_4.index(tr3[0][1]):line_4.index(station2):-1]
                                line_4.append(station2)
                            case _:
                                line_4 = line_4[line_4.index(tr3[0][1]):line_4.index(station2) + 1:]

                        result = line_1 + line_2 + line_3 + line_4
                        for r1 in result:
                            if result.count(r1) > 1:
                                break
                        else:
                            line_result.append(result)
                    except KeyError:
                        continue
            except KeyError:
                continue
    except:
        pass
    print(len(line_result))
    # возвращаем все вариации маршрутов
    for r in line_result:
        if line_result.count(r) > 1:
            line_result.remove(r)
        else:
            for r1 in r:
                if r.count(r1) > 1:
                    print(False)
    return line_result


if __name__ == '__main__':
    for i in plotting_a_route('Деловой центр8A', '8A', 'Деловой центр8A', '8A', lines):
        print(i)
    '''w = []
    t = 0
    f = 0
    e = 0
    for i in lines:
        for j in lines[i]:
            w.append(j)
    for i in w:
        st1 = [s for s in [1, 2, 3, 4, '4A', 5, 6, 7, 8, '8A', 9, 10, 11, '11A', 12, 15] if i in lines[s]]
        st1 = st1[0]
        for j in w:
            if j != i:
                st2 = [s for s in [1, 2, 3, 4, '4A', 5, 6, 7, 8, '8A', 9, 10, 11, '11A', 12, 15] if j in lines[s]]
                st2 = st2[0]
                try:
                    if plotting_a_route(i, st1, j, st2, lines) is []:
                        e += 1
                    plotting_a_route(i, st1, j, st2, lines)
                    print(True, i, j)
                    t += 1
                except Exception:
                    print(False, i, j)
                    f += 1
    print(len(w), e)
    print(f'True: {t}, False: {f}')'''
