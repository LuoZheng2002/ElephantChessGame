concepts = [
    # 基本概念
    'True',
    'False',
    'Fail',
    'id',
    'name',
    'content',
    # 普通概念
    'list',
    'digit',
    'natural_number',
    'vector',
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'greater_than',
    'less_than',
    'math_equal',
    # 可执行代码相关概念
    'dynamic_code_object',
    'dc::line',
    'dc::expression',
    # 语句头
    'head_kw::assign',
    'head_kw::assign_as_reference',
    'head_kw::return',
    'head_kw::assert',
    'head_kw::for',
    'head_kw::while',
    'head_kw::break',
    'head_kw::if',
    'head_kw::append',
    'head_kw::remove',
    'head_kw::request',
    # 表达式头
    'expr_kw::input',
    'expr_kw::reg',
    'expr_kw::iterator',
    'expr_kw::call',
    'expr_kw::concept_instance',
    'expr_kw::size',
    'expr_kw::get_member',
    'expr_kw::get_concept_id',
    'expr_kw::at',
    'expr_kw::at_reverse',
    'expr_kw::find',
    'expr_kw::exist',
    'expr_kw::target',
    # 可执行代码
    # 硬编码代码
    'func::compare_concepts',
    'func::logic_and',
    'func::logic_or',
    'func::logic_not',
    'func::is_natural_number_single_digit',
    'func::compare_single_digit_natural_numbers',
    'func::sum',
    # 动态代码
    'func::digit_to_natural_number',
    'func::compare_natural_numbers',
    'func::math_equal',
    'func::greater_than',
    'func::less_than',
    'func::greater_than_or_equal_to',
    'func::less_than_or_equal_to',
    'func::test_code',
    'func::batch_logic_and',
    'func::batch_logic_or',
    'func::max',
    'func::min',
    # 回合制博弈问题相关概念
    'tb_game::game',
    'tb_game::chessboard',
    'tb_game::rule',
    'tb_game::winning_criteria',
    'tb_game::teams',
    'tb_game::occupations',
    'tb_game::who_is_next_func',
    'tb_game::my_team_id',
    'tb_game::end_game_func',
    'tb_game::end_game_benefits',
    'tb_game::team',
    'tb_game::players',
    'tb_game::end_game_benefit_id',
    'tb_game::occupation',
    'tb_game::operation_func',
    'tb_game::end_game_benefit',
    'tb_game::benefit_func',
    'tb_game::player',
    'tb_game::occupation_id',
    # 下面是在解决博弈问题时临时生成的概念id
    'xq::chessboard',
    'xq::pieces',
    'xq::piece',
    'xq::piece_owner',
    'xq::piece_name',
    'xq::position',
    'xq::Che',
    'xq::Ma',
    'xq::Xiang',
    'xq::Shi',
    'xq::Jiang',
    'xq::Pao',
    'xq::Bing',
    'xq::whose_turn',
    'xq::red_team',
    'xq::black_team',
    'xq::red_player',
    'xq::black_player',
    'xq::player_occupation',
    'xq::player_benefit',
]


def generate_concept_ids(concept_names):
    concept_ids = dict()
    for i, j in enumerate(concept_names):
        concept_ids.update({j: i})
    return concept_ids


cid_of = generate_concept_ids(concepts)

cid_reverse = dict([(i, j) for (j, i) in cid_of.items()])

