from dataclasses import dataclass


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


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    start: Point
    end: Point


def walrus_patterns(test_input):
    match test_input:
        case Point(x, y):
            print('it is a point')
        case Line(Point(x, y) as start, Point(z, k) as end) if start == end:
            print(start)
        case _:
            print('not is a point')


if __name__ == '__main__':
    print(match_types('hello'))
    print(match_types(10))
    print(match_types(10.0))

    walrus_patterns(Point(10, 11))
    walrus_patterns(Line(Point(10, 11), Point(10, 11)))

    if a := len('some word') > 5:
        print('it is too long')


