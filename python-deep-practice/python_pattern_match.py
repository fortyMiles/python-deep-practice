def match_feature(x):
    match x:
        case a, b:
            print(a)
        case a, b, c:
            print(c)
        case _:
            print('not fit')


if __name__ == '__main__':
    match_feature((1, 2))
