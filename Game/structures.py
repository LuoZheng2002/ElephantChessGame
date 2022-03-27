from ExternalAGIStuff.concept_instance_struct import AGIObject, AGIList
from ExternalAGIStuff.concept_ids import cid_of


def game_object(chessboard: AGIObject,
                rule: AGIObject,
                winning_criteria: AGIObject) -> AGIObject:
    return AGIObject(cid_of['game'], {cid_of['game::chessboard']: chessboard,
                                      cid_of['game::rule']: rule,
                                      cid_of['game::winning_criteria']: winning_criteria})


def chessboard_object(elements: AGIList) -> AGIObject:
    return AGIObject(cid_of['game::chessboard'], {cid_of['value']: elements})


def rule_object(teams: AGIList,
                occupations: AGIList,
                who_is_next_func: AGIObject,
                my_team_id: AGIObject) -> AGIObject:
    return AGIObject(cid_of['game::rule'], {cid_of['game::rule::teams']: teams,
                                            cid_of['game::rule::occupations']: occupations,
                                            cid_of['game::rule::who_is_next_func']: who_is_next_func,
                                            cid_of['game::rule::my_team_id']: my_team_id})


def winning_criteria_object(end_game_func: AGIObject, end_game_benefits: AGIList):
    return AGIObject(cid_of['game::winning_criteria'],
                     {cid_of['game::winning_criteria::end_game_func']: end_game_func,
                      cid_of['game::winning_criteria::end_game_benefits']: end_game_benefits})


def team_object(team_id: int, players: AGIList, end_game_benefit_id: int) -> AGIObject:
    return AGIObject(cid_of['game::rule::team'], {cid_of['game::rule::team::id']: team_id,
                                                  cid_of['game::rule::team::players']: players,
                                                  cid_of['game::rule::team::end_game_benefit_id']: end_game_benefit_id})


def occupation_object(occupation_id: AGIObject, operation_func: AGIObject) -> AGIObject:
    return AGIObject(cid_of['game::rule::occupation'],
                     {cid_of['game::rule::occupation::id']: occupation_id,
                      cid_of['game::rule::occupation::operation_func']: operation_func})


def executable(lines: AGIList) -> AGIObject:
    return AGIObject(cid_of['executable'], {cid_of['value']: lines})


def end_game_benefit(benefit_id: AGIObject, benefit_func: AGIObject) -> AGIObject:
    return AGIObject(cid_of['game::winning_criteria::end_game_benefit'],
                     {cid_of['game::winning_criteria::end_game_benefit::id']: benefit_id,
                      cid_of['game::winning_criteria::end_game_benefit::benefit_func']: benefit_func})


def player_object(player_id: int, occupation_id: int) -> AGIObject:
    return AGIObject(cid_of['game::rule::team::player'],
                     {cid_of['game::rule::team::player::id']: player_id,
                      cid_of['game::rule::team::player::occupation_id']: occupation_id})
