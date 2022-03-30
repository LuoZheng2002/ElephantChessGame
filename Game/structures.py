from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList
from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.IDs.to_object import obj


def game_object(chessboard: AGIObject,
                rule: AGIObject,
                winning_criteria: AGIObject) -> AGIObject:
    return AGIObject(cid_of['tb_game::game'], {cid_of['tb_game::chessboard']: chessboard,
                                               cid_of['tb_game::rule']: rule,
                                               cid_of['tb_game::winning_criteria']: winning_criteria})


def xq_chessboard_object(pieces: AGIList, whose_turn: AGIObject) -> AGIObject:
    return AGIObject(cid_of['xq::chessboard'], {cid_of['xq::pieces']: pieces,
                                                cid_of['xq::whose_turn']: whose_turn})


def rule_object(teams: AGIList,
                occupations: AGIList,
                who_is_next_func: AGIObject or None,
                my_team_id: AGIObject) -> AGIObject:
    return AGIObject(cid_of['tb_game::rule'], {cid_of['tb_game::teams']: teams,
                                               cid_of['tb_game::occupations']: occupations,
                                               cid_of['tb_game::who_is_next_func']: who_is_next_func,
                                               cid_of['tb_game::my_team_id']: my_team_id})


def winning_criteria_object(end_game_func: AGIObject or None, end_game_benefits: AGIList):
    return AGIObject(cid_of['tb_game::winning_criteria'],
                     {cid_of['tb_game::end_game_func']: end_game_func,
                      cid_of['tb_game::end_game_benefits']: end_game_benefits})


def team_object(team_name: str, players: AGIList, end_game_benefit_name: str) -> AGIObject:
    return AGIObject(cid_of['tb_game::team'],
                     {cid_of['name']: obj(team_name),
                      cid_of['tb_game::players']: players,
                      cid_of['tb_game::end_game_benefit_id']: obj(end_game_benefit_name)})


def occupation_object(occupation_name: str, operation_func: AGIObject or None) -> AGIObject:
    return AGIObject(cid_of['tb_game::occupation'],
                     {cid_of['name']: obj(occupation_name),
                      cid_of['tb_game::operation_func']: operation_func})


def end_game_benefit(benefit_name: str, benefit_func: AGIObject or None) -> AGIObject:
    return AGIObject(cid_of['tb_game::end_game_benefit'],
                     {cid_of['name']: obj(benefit_name),
                      cid_of['tb_game::benefit_func']: benefit_func})


def player_object(player_name: str, occupation_name: str) -> AGIObject:
    return AGIObject(cid_of['tb_game::player'],
                     {cid_of['name']: obj(player_name),
                      cid_of['tb_game::occupation_id']: obj(occupation_name)})
