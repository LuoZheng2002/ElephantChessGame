from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList
from ExternalAGIStuff.IDs.concept_ids import cid_of


def game_object(chessboard: AGIObject,
                rule: AGIObject,
                winning_criteria: AGIObject) -> AGIObject:
    return AGIObject(cid_of['tb_game::game'], {cid_of['tb_game::chessboard']: chessboard,
                                               cid_of['tb_game::rule']: rule,
                                               cid_of['tb_game::winning_criteria']: winning_criteria})


def chessboard_object(elements: AGIList) -> AGIObject:
    return AGIObject(cid_of['tb_game::chessboard'], {cid_of['content']: elements})


def rule_object(teams: AGIList,
                occupations: AGIList,
                who_is_next_func: AGIObject,
                my_team_id: AGIObject) -> AGIObject:
    return AGIObject(cid_of['tb_game::rule'], {cid_of['tb_game::teams']: teams,
                                               cid_of['tb_game::occupations']: occupations,
                                               cid_of['tb_game::who_is_next_func']: who_is_next_func,
                                               cid_of['tb_game::my_team_id']: my_team_id})


def winning_criteria_object(end_game_func: AGIObject, end_game_benefits: AGIList):
    return AGIObject(cid_of['tb_game::winning_criteria'],
                     {cid_of['tb_game::end_game_func']: end_game_func,
                      cid_of['tb_game::end_game_benefits']: end_game_benefits})


def team_object(team_id: int, players: AGIList, end_game_benefit_id: int) -> AGIObject:
    return AGIObject(cid_of['tb_game::team'], {cid_of['id']: team_id,
                                               cid_of['tb_game::players']: players,
                                               cid_of[
                                                   'tb_game::end_game_benefit_id']: end_game_benefit_id})


def occupation_object(occupation_id: AGIObject, operation_func: AGIObject) -> AGIObject:
    return AGIObject(cid_of['tb_game::occupation'],
                     {cid_of['id']: occupation_id,
                      cid_of['tb_game::operation_func']: operation_func})


def executable(lines: AGIList) -> AGIObject:
    return AGIObject(cid_of['code_kw::executable'], {cid_of['content']: lines})


def end_game_benefit(benefit_id: AGIObject, benefit_func: AGIObject) -> AGIObject:
    return AGIObject(cid_of['tb_game::end_game_benefit'],
                     {cid_of['id']: benefit_id,
                      cid_of['tb_game::benefit_func']: benefit_func})


def player_object(player_id: int, occupation_id: int) -> AGIObject:
    return AGIObject(cid_of['tb_game::player'],
                     {cid_of['id']: player_id,
                      cid_of['tb_game::occupation_id']: occupation_id})
