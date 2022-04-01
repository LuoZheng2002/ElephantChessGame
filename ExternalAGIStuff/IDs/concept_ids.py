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
    'dynamic_code',
    'dc::lines',
    'dc::sub_block',
    # 语句头
    'dcr::assign',  #
    'dcr::assign_as_reference',  #
    'dcr::return',  #
    'dcr::assert',  #
    'dcr::for',  #
    'dcr::while',  #
    'dcr::break',  #
    'dcr::if',  #
    'dcr::append',  #
    'dcr::remove',  #
    'dcr::request',  #
    # 表达式头
    'dcr::input',  #
    'dcr::reg',  #
    'dcr::iterator',  #
    'dcr::call',  #
    'dcr::concept_instance',  #
    'dcr::size',
    'dcr::get_member',
    'dcr::at',
    'dcr::at_reverse',
    'dcr::find',
    'dcr::exist',
    'dcr::count',
    'dcr::target',
    'dcr::constexpr',
    # 参数名称
    'dc::left_value',
    'dc::right_value',
    'dc::return_value',
    'dc::assert_expression',
    'dc::index',
    'dc::child_indices',
    'dc::function_name',
    'dc::function_params',
    'dc::concept_name',
    'dc::target_list',
    'dc::target_object',
    'dc::member_name',
    'dc::expression_for_constraint',
    'dc::expression_for_judging',
    'dc::iterator_index',
    'dc::end_value',
    'dc::for_block',
    'dc::while_block',
    'dc::if_block',
    'dc::elif_modules',
    'dc::elif_module',
    'dc::elif_block',
    'dc::else_block',
    'dc::element',
    'dc::requested_registers',
    'dc::provided_block',
    # 可执行代码
    # 硬编码代码
    'func::compare_concepts',
    'func::logic_and',
    'func::logic_or',
    'func::logic_not',
    'func::is_natural_number_single_digit',
    'func::compare_single_digit_natural_numbers',
    'func::sum',
    'func::difference',
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

