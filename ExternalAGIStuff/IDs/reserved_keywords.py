reserved_keywords = [
    # 语句头
    'assign',  # 0
    'assign_as_reference',  # 1
    'return',  # 2
    'assert',  # 3
    'for',  # 4
    'while',  # 5
    'break',  # 6
    'if',  # 7
    'append',  # 8
    'remove',  # 9
    'request',  # 10
    # 表达式头
    'input',  # 11
    'reg',  # 12
    'iterator',  # 13
    'call',  # 14
    'concept_instance',  # 15
    'size',  # 16
    'get_member',  # 17
    'at',  # 18
    'at_reverse',  # 19
    'find',  # 20
    'exist',  # 21
    'count',
    'target'  # 22
]


def generate_reserved_keywords(keywords):
    reserved = dict()
    for i, j in enumerate(keywords):
        reserved.update({j: i})
    return reserved


r = generate_reserved_keywords(reserved_keywords)

rr = dict([(i, j) for (j, i) in r.items()])
