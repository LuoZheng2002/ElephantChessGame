from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
process_line_f = [
[r['if'], [r['call'], cid_of['func::logic_or'],
[
[r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::assign']]
]
],
[r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::assign_as_reference']]
]
]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(0), []], [r['get_member'], [r['input'], obj(0)], cid_of['dc::left_value']]], 
[r['assign_as_reference'], [r['reg'], obj(1), []], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::right_value']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(0), []],
[r['concept_instance'], cid_of['dcr::reg']]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(2), []], [r['get_member'], [r['reg'], obj(0), []], cid_of['dc::index']]], 
[r['assign_as_reference'], [r['reg'], obj(3), []], [r['concept_instance'], cid_of['list']]], 
[r['for'], obj(0), [r['size'], [r['get_member'], [r['reg'], obj(0), []], cid_of['dc::child_indices']]],
[
[r['assign_as_reference'], [r['at'], [r['reg'], obj(3), []], [r['iterator'], obj(0)]], [r['call'], cid_of['func::solve_expression'],
[
[r['at'], [r['get_member'], [r['reg'], obj(0), []], cid_of['dc::child_indices']], [r['iterator'], obj(0)]],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]]
]
], 
[r['if'], [r['call'], cid_of['func::logic_not'], 
[
[r['exist'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_registers']], [r['call'], cid_of['func::logic_and'],
[
[r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['reg'], obj(2), []]
]
],
[r['call'], cid_of['func::child_indices_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::child_indices']],
[r['reg'], obj(3), []]
]
]
]
]]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(4), []], [r['concept_instance'], cid_of['dc::register_container']]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(4), []], cid_of['dc::index']], [r['reg'], obj(2), []]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(4), []], cid_of['dc::child_indices']], [r['reg'], obj(3), []]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::assign']]
]
],
[
[r['assign'], [r['get_member'], [r['reg'], obj(4), []], cid_of['value']], [r['reg'], obj(1), []]]
],
[],
[
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(4), []], cid_of['value']], [r['reg'], obj(1), []]]
]
], 
[r['append'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_registers']], [r['reg'], obj(4), []]]
],
[],
[
[r['assign_as_reference'], [r['reg'], obj(4), []], [r['find'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_registers']], [r['call'], cid_of['func::logic_and'],
[
[r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['reg'], obj(2), []]
]
],
[r['call'], cid_of['func::child_indices_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::child_indices']],
[r['reg'], obj(3), []]
]
]
]
]]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::assign']]
]
],
[
[r['assign'], [r['get_member'], [r['reg'], obj(4), []], cid_of['value']], [r['reg'], obj(1), []]]
],
[],
[
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(4), []], cid_of['value']], [r['reg'], obj(1), []]]
]
]
]
]
],
[[
[r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(0), []],
[r['concept_instance'], cid_of['dcr::get_member']]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(2), []], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['reg'], obj(0), []], cid_of['dc::target_object']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['call_none_return_func'], cid_of['func::set_object_member'],
[
[r['reg'], obj(2), []],
[r['get_member'], [r['reg'], obj(0), []], cid_of['dc::member_name']],
[r['reg'], obj(1), []]
]
]
]
],
[
[r['call'], cid_of['func::logic_or'],
[
[r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(0), []],
[r['concept_instance'], cid_of['dcr::at']]
]
],
[r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(0), []],
[r['concept_instance'], cid_of['dcr::at_reverse']]
]
]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(2), []], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['reg'], obj(0), []], cid_of['dc::target_list']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['assign_as_reference'], [r['reg'], obj(3), []], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['reg'], obj(0), []], cid_of['dc::index']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(0), []],
[r['concept_instance'], cid_of['dcr::at']]
]
],
[
[r['assign_as_reference'], [r['at'], [r['reg'], obj(2), []], [r['reg'], obj(3), []]], [r['reg'], obj(1), []]]
],
[[
[r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(0), []],
[r['concept_instance'], cid_of['dcr::at_reverse']]
]
],
[
[r['assign_as_reference'], [r['at_reverse'], [r['reg'], obj(2), []], [r['reg'], obj(3), []]], [r['reg'], obj(1), []]]
]
]],
[
[r['assert'], [r['concept_instance'], cid_of['False']]]
]
]
]
]],
[
[r['assert'], [r['concept_instance'], cid_of['False']]]
]
], 
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::return']]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(0), []], [r['concept_instance'], cid_of['dc::line_signal_return']]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(0), []], cid_of['dc::line_return_value']], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::return_value']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['return'], [r['reg'], obj(0), []]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::for']]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(0), []], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::end_value']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['if'], [r['call'], cid_of['func::logic_not'], 
[
[r['exist'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_iterators']], [r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['get_member'], [r['input'], obj(0)], cid_of['dc::iterator_index']]
]
]]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(1), []], [r['concept_instance'], cid_of['dc::iterator_container']]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(1), []], cid_of['dc::index']], [r['get_member'], [r['input'], obj(0)], cid_of['dc::iterator_index']]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(1), []], cid_of['value']], [obj(0)]], 
[r['append'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_iterators']], [r['reg'], obj(1), []]]
],
[],
[
[r['assign_as_reference'], [r['reg'], obj(1), []], [r['find'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_iterators']], [r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['get_member'], [r['input'], obj(0)], cid_of['dc::iterator_index']]
]
]]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(1), []], cid_of['value']], [obj(0)]]
]
], 
[r['for'], obj(0), [r['reg'], obj(0), []],
[
[r['for'], obj(1), [r['size'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::for_block']]],
[
[r['assign_as_reference'], [r['reg'], obj(2), [[r['iterator'], obj(0)], [r['iterator'], obj(1)]]], [r['call'], cid_of['func::process_line'],
[
[r['at'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::for_block']], [r['iterator'], obj(1)]],
[r['input'], obj(1)]
]
]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(2), [[r['iterator'], obj(0)], [r['iterator'], obj(1)]]],
[r['concept_instance'], cid_of['dc::line_signal_break']]
]
],
[
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[[
[r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(2), [[r['iterator'], obj(0)], [r['iterator'], obj(1)]]],
[r['concept_instance'], cid_of['dc::line_signal_return']]
]
],
[
[r['return'], [r['reg'], obj(2), [[r['iterator'], obj(0)], [r['iterator'], obj(1)]]]]
]
]],
[]
]
]
], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(1), []], cid_of['value']], [r['call'], cid_of['func::sum'],
[
[r['get_member'], [r['reg'], obj(1), []], cid_of['value']],
[obj(1)]
]
]]
]
], 
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::while']]
]
],
[
[r['while'], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::expression_for_judging']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
],
[
[r['for'], obj(0), [r['size'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::while_block']]],
[
[r['assign_as_reference'], [r['reg'], obj(0), [[r['iterator'], obj(0)]]], [r['call'], cid_of['func::process_line'],
[
[r['at'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::while_block']], [r['iterator'], obj(0)]],
[r['input'], obj(1)]
]
]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(0), [[r['iterator'], obj(0)]]],
[r['concept_instance'], cid_of['dc::line_signal_break']]
]
],
[
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[[
[r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(0), [[r['iterator'], obj(0)]]],
[r['concept_instance'], cid_of['dc::line_signal_return']]
]
],
[
[r['return'], [r['reg'], obj(0), [[r['iterator'], obj(0)]]]]
]
]],
[]
]
]
]
]
], 
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::break']]
]
],
[
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_break']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::if']]
]
],
[
[r['if'], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::expression_for_judging']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
],
[
[r['for'], obj(0), [r['size'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::if_block']]],
[
[r['assign_as_reference'], [r['reg'], obj(0), [[r['iterator'], obj(0)]]], [r['call'], cid_of['func::process_line'],
[
[r['at'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::if_block']], [r['iterator'], obj(0)]],
[r['input'], obj(1)]
]
]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(0), [[r['iterator'], obj(0)]]],
[r['concept_instance'], cid_of['dc::line_signal_break']]
]
],
[
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_break']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(0), [[r['iterator'], obj(0)]]],
[r['concept_instance'], cid_of['dc::line_signal_return']]
]
],
[
[r['return'], [r['reg'], obj(0), [[r['iterator'], obj(0)]]]]
],
[],
[]
]
]
], 
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[],
[
[r['for'], obj(0), [r['size'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::elif_modules']]],
[
[r['if'], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['at'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::elif_modules']], [r['iterator'], obj(0)]], cid_of['dc::expression_for_judging']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(0), [[r['iterator'], obj(0)]]], [r['get_member'], [r['at'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::elif_modules']], [r['iterator'], obj(0)]], cid_of['dc::elif_block']]], 
[r['for'], obj(1), [r['size'], [r['reg'], obj(0), [[r['iterator'], obj(0)]]]],
[
[r['assign_as_reference'], [r['reg'], obj(1), [[r['iterator'], obj(0)], [r['iterator'], obj(1)]]], [r['call'], cid_of['func::process_line'],
[
[r['at'], [r['reg'], obj(0), [[r['iterator'], obj(0)]]], [r['iterator'], obj(1)]],
[r['input'], obj(1)]
]
]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(1), [[r['iterator'], obj(0)], [r['iterator'], obj(1)]]],
[r['concept_instance'], cid_of['dc::line_signal_break']]
]
],
[
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_break']]]
],
[[
[r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(1), [[r['iterator'], obj(0)], [r['iterator'], obj(1)]]],
[r['concept_instance'], cid_of['dc::line_signal_return']]
]
],
[
[r['return'], [r['reg'], obj(1), [[r['iterator'], obj(0)], [r['iterator'], obj(1)]]]]
]
]],
[]
]
]
]
],
[],
[]
]
]
], 
[r['assign_as_reference'], [r['reg'], obj(2), []], [r['get_member'], [r['input'], obj(0)], cid_of['dc::else_block']]], 
[r['for'], obj(2), [r['size'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::else_block']]],
[
[r['assign_as_reference'], [r['reg'], obj(3), [[r['iterator'], obj(2)]]], [r['call'], cid_of['func::process_line'],
[
[r['at'], [r['reg'], obj(2), []], [r['iterator'], obj(2)]],
[r['input'], obj(1)]
]
]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(3), [[r['iterator'], obj(2)]]],
[r['concept_instance'], cid_of['dc::line_signal_break']]
]
],
[
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_break']]]
],
[[
[r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(3), [[r['iterator'], obj(2)]]],
[r['concept_instance'], cid_of['dc::line_signal_return']]
]
],
[
[r['return'], [r['reg'], obj(3), [[r['iterator'], obj(2)]]]]
]
]],
[]
]
]
], 
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
]
]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::assert']]
]
],
[
[r['assert'], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::assert_expression']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::append']]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(0), []], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::target_list']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['assign_as_reference'], [r['reg'], obj(1), []], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::element']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['append'], [r['reg'], obj(0), []], [r['reg'], obj(1), []]], 
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::remove']]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(0), []], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::target_list']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['while'], [r['concept_instance'], cid_of['True']],
[
[r['assign_as_reference'], [r['reg'], obj(1), []], [r['call'], cid_of['func::remove_one_element'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::expression_for_constraint']],
[r['input'], obj(1)],
[r['reg'], obj(0), []]
]
]], 
[r['if'], [r['call'], cid_of['func::logic_not'], 
[
[r['reg'], obj(1), []]
]
],
[
[r['break']]
],
[],
[]
]
]
], 
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::request']]
]
],
[
[r['assert'], [r['call'], cid_of['func::greater_than_or_equal_to'],
[
[r['size'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::requested_registers']]],
[obj(1)]
]
]], 
[r['for'], obj(0), [r['size'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::requested_registers']]],
[
[r['assign_as_reference'], [r['reg'], obj(0), [[r['iterator'], obj(0)]]], [r['at'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::requested_registers']], [r['iterator'], obj(0)]]], 
[r['assert'], [r['call'], cid_of['func::logic_not'], 
[
[r['exist'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_registers']], [r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['reg'], obj(0), [[r['iterator'], obj(0)]]]
]
]]
]
]], 
[r['assign_as_reference'], [r['reg'], obj(1), [[r['iterator'], obj(0)]]], [r['concept_instance'], cid_of['dc::register_container']]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(1), [[r['iterator'], obj(0)]]], cid_of['dc::index']], [r['reg'], obj(0), [[r['iterator'], obj(0)]]]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(1), [[r['iterator'], obj(0)]]], cid_of['dc::child_indices']], [r['concept_instance'], cid_of['list']]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(1), [[r['iterator'], obj(0)]]], cid_of['value']], [r['call'], cid_of['func::get_input_object'],
[

]
]], 
[r['append'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_registers']], [r['reg'], obj(1), [[r['iterator'], obj(0)]]]]
]
], 
[r['assign_as_reference'], [r['reg'], obj(2), []], [r['get_member'], [r['input'], obj(0)], cid_of['dc::provided_block']]], 
[r['for'], obj(1), [r['size'], [r['reg'], obj(2), []]],
[
[r['assign_as_reference'], [r['reg'], obj(3), [[r['iterator'], obj(1)]]], [r['call'], cid_of['func::process_line'],
[
[r['at'], [r['reg'], obj(2), []], [r['iterator'], obj(1)]],
[r['input'], obj(1)]
]
]], 
[r['assert'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(3), [[r['iterator'], obj(1)]]],
[r['concept_instance'], cid_of['dc::line_signal_normal']]
]
]]
]
], 
[r['assert'], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::expression_for_constraint']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::call_none_return_func']]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(0), []], [r['get_member'], [r['input'], obj(0)], cid_of['dc::function_name']]], 
[r['assign_as_reference'], [r['reg'], obj(1), []], [r['get_member'], [r['input'], obj(0)], cid_of['dc::function_params']]], 
[r['assign_as_reference'], [r['reg'], obj(2), []], [r['concept_instance'], cid_of['list']]], 
[r['for'], obj(0), [r['size'], [r['reg'], obj(1), []]],
[
[r['append'], [r['reg'], obj(2), []], [r['call'], cid_of['func::solve_expression'],
[
[r['at'], [r['reg'], obj(1), []], [r['iterator'], obj(0)]],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]]
]
], 
[r['if'], [r['call'], cid_of['func::is_code_dynamic'],
[
[r['reg'], obj(0), []]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(3), []], [r['call'], cid_of['func::run_dynamic_code_object'],
[
[r['call'], cid_of['func::get_dynamic_code_object'],
[
[r['reg'], obj(0), []]
]
],
[r['reg'], obj(2), []]
]
]]
],
[],
[
[r['assign_as_reference'], [r['reg'], obj(3), []], [r['call'], cid_of['func::run_hardcoded_code'],
[
[r['reg'], obj(0), []],
[r['reg'], obj(2), []]
]
]]
]
], 
[r['assert'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(3), []],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['return'], [r['concept_instance'], cid_of['dc::line_signal_normal']]]
],
[],
[]
], 
[r['assert'], [r['concept_instance'], cid_of['False']]]
]