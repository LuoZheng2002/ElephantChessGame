from Game.structures import *
from ExternalAGIStuff.IDs.to_object import obj


def natural_number_object(number: int):
    return obj(number)


def vector_object(numbers):
    value = list()
    for number in numbers:
        value.append(natural_number_object(number))
    return AGIObject(cid_of['vector'], {cid_of['content']: AGIList(value)})


def piece_object(owner: str, name: str, position: list) -> AGIObject:
    return AGIObject(cid_of['xq::piece'], {cid_of['xq::piece_owner']: AGIObject(cid_of[owner], dict()),
                                           cid_of['xq::piece_name']: AGIObject(cid_of[name], dict()),
                                           cid_of['xq::position']: vector_object(position)})


pieces_list = [
    piece_object('xq::red_team', 'xq::Che', [0, 0]),
    piece_object('xq::red_team', 'xq::Ma', [1, 0]),
    piece_object('xq::red_team', 'xq::Xiang', [2, 0]),
    piece_object('xq::red_team', 'xq::Shi', [3, 0]),
    piece_object('xq::red_team', 'xq::Jiang', [4, 0]),
    piece_object('xq::red_team', 'xq::Shi', [5, 0]),
    piece_object('xq::red_team', 'xq::Xiang', [6, 0]),
    piece_object('xq::red_team', 'xq::Ma', [7, 0]),
    piece_object('xq::red_team', 'xq::Che', [8, 0]),
    piece_object('xq::red_team', 'xq::Pao', [1, 2]),
    piece_object('xq::red_team', 'xq::Pao', [7, 2]),
    piece_object('xq::red_team', 'xq::Bing', [0, 3]),
    piece_object('xq::red_team', 'xq::Bing', [2, 3]),
    piece_object('xq::red_team', 'xq::Bing', [4, 3]),
    piece_object('xq::red_team', 'xq::Bing', [6, 3]),
    piece_object('xq::red_team', 'xq::Bing', [8, 3]),
    piece_object('xq::black_team', 'xq::Che', [0, 9]),
    piece_object('xq::black_team', 'xq::Ma', [1, 9]),
    piece_object('xq::black_team', 'xq::Xiang', [2, 9]),
    piece_object('xq::black_team', 'xq::Shi', [3, 9]),
    piece_object('xq::black_team', 'xq::Jiang', [4, 9]),
    piece_object('xq::black_team', 'xq::Shi', [5, 9]),
    piece_object('xq::black_team', 'xq::Xiang', [6, 9]),
    piece_object('xq::black_team', 'xq::Ma', [7, 9]),
    piece_object('xq::black_team', 'xq::Che', [8, 9]),
    piece_object('xq::black_team', 'xq::Pao', [1, 7]),
    piece_object('xq::black_team', 'xq::Pao', [7, 7]),
    piece_object('xq::black_team', 'xq::Bing', [0, 6]),
    piece_object('xq::black_team', 'xq::Bing', [2, 6]),
    piece_object('xq::black_team', 'xq::Bing', [4, 6]),
    piece_object('xq::black_team', 'xq::Bing', [6, 6]),
    piece_object('xq::black_team', 'xq::Bing', [8, 6]),
]
pieces = AGIList(pieces_list)
whose_turn = AGIObject(cid_of['xq::red_team'], dict())
xq_chessboard = xq_chessboard_object(pieces, whose_turn)
teams = [
    team_object('xq::red_team',
                AGIList([player_object('xq::red_player', 'xq::player_occupation')]),
                'xq::player_benefit'),
    team_object('xq::black_team',
                AGIList([player_object('xq::black_player', 'xq::player_occupation')]),
                'xq::player_benefit')
]
# to do: operation_func
operation_func = None
occupations = [occupation_object('xq::player_occupation', operation_func)]
who_is_next_func = None
rule = rule_object(AGIList(teams), AGIList(occupations), who_is_next_func, obj('xq::red_team'))
end_game_func = None
benefit_func = None
end_game_benefits = [end_game_benefit('xq::player_benefit', benefit_func)]
winning_criteria = winning_criteria_object(end_game_func, AGIList(end_game_benefits))
elephant_chess = game_object(xq_chessboard, rule, winning_criteria)
