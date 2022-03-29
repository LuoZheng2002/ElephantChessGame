reserved_keywords = [
    # 语句头
    'assign',
    'assign_as_reference',
    'return',
    'assert',
    'for',
    'while',
    'break',
    'if',
    'append',
    'remove',
    'request',
    # 表达式头
    'input',
    'reg',
    'iterator',
    'call',
    'concept_instance',
    'size',
    'get_member',
    'at',
    'at_reverse',
    'find',
    'exist',
    'target'
]


def generate_reserved_keywords(keywords):
    reserved = dict()
    for i, j in enumerate(keywords):
        reserved.update({j: i})
    return reserved


r = generate_reserved_keywords(reserved_keywords)

rr = dict([(i, j) for (j, i) in r.items()])
