def match_feature(x):
    match x:
        case a, b:
            print(a)
        case a, b, c:
            print(c)
        case {'name': name, 'age': age, 'register': {'new': _new}}:
            print(name, age, _new)
        case _:
            print('not fit')


def match_types(input_content):
    match input_content:
        case float() | int():
            return input_content, 'is number'
        case str():
            return input_content, 'is string'
        case _:
            return 'not anything'


if __name__ == '__main__':
    print(match_types('hello'))
    print(match_types(10))
    print(match_types(10.0))
