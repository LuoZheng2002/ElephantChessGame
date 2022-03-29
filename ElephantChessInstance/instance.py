from Game.structures import *


def natural_number_object(number: int):
    value = list()
    str_number = str(number)
    for digit in str_number:
        value.append(AGIObject(int(digit)+100, dict()))
    return AGIObject(cid_of['natural_number'], {cid_of['value']: AGIList(value)})


def vector_object(numbers):
    value = list()
    for number in numbers:
        value.append(natural_number_object(number))
    return AGIObject(cid_of['vector'], {cid_of['value']: AGIList(value)})


def piece_object(owner: str, name: str, position: list) -> AGIObject:
    return AGIObject(cid_of['piece'], {cid_of['piece_owner']: cid_of[owner],
                                       cid_of['piece_name']: cid_of[name],
                                       cid_of['position']: vector_object(position)})


pieces_list = [
    piece_object('red_team', '车', [0, 0]),
    piece_object('red_team', '马', [1, 0])
]
elements = [
    AGIObject(cid_of['pieces'], {cid_of['value']: AGIList(pieces_list)}),
    AGIObject(cid_of['whose_turn'], {cid_of['value']: cid_of['reds_turn']})
]
chessboard = chessboard_object(AGIList(elements))
teams = [
    team_object(cid_of['red_team'],
                AGIList([player_object(cid_of['red_player'], cid_of['elephant_chess_player_occupation'])]),
                cid_of['elephant_chess_player_benefit']),
    team_object(cid_of['red_team'],
                AGIList([player_object(cid_of['red_player'], cid_of['elephant_chess_player_occupation'])]),
                cid_of['elephant_chess_player_benefit'])
]
# to do: operation_func
operation_func = executable(AGIList())
occupations = [occupation_object(cid_of['elephant_chess_player_occupation'], operation_func)]
who_is_next_func = executable(AGIList())
rule = rule_object(AGIList(teams), AGIList(occupations), who_is_next_func, cid_of['red_team'])
end_game_func = executable(AGIList())
benefit_func = executable(AGIList())
end_game_benefits = [end_game_benefit(cid_of['elephant_chess_player_benefit'], benefit_func)]
winning_criteria = winning_criteria_object(end_game_func, AGIList(end_game_benefits))
elephant_chess = game_object(chessboard, rule, winning_criteria)
