from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
solve_expression_f = [
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::constexpr']]
]
],
[
[r['return'], [r['get_member'], [r['input'], obj(0)], cid_of['content']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::input']]
]
],
[
[r['assert'], [r['exist'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_inputs']], [r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['get_member'], [r['input'], obj(0)], cid_of['dc::index']]
]
]]], 
[r['return'], [r['get_member'], [r['find'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_inputs']], [r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['get_member'], [r['input'], obj(0)], cid_of['dc::index']]
]
]], cid_of['value']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::reg']]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(0), []], [r['get_member'], [r['input'], obj(0)], cid_of['dc::index']]], 
[r['assign_as_reference'], [r['reg'], obj(1), []], [r['concept_instance'], cid_of['list']]], 
[r['for'], obj(0), [r['size'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::child_indices']]],
[
[r['assign_as_reference'], [r['at'], [r['reg'], obj(1), []], [r['iterator'], obj(0)]], [r['call'], cid_of['func::solve_expression'],
[
[r['at'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::child_indices']], [r['iterator'], obj(0)]],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]]
]
], 
[r['assert'], [r['exist'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_registers']], [r['call'], cid_of['func::logic_and'],
[
[r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['reg'], obj(0), []]
]
],
[r['call'], cid_of['func::child_indices_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::child_indices']],
[r['reg'], obj(1), []]
]
]
]
]]], 
[r['return'], [r['get_member'], [r['find'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_registers']], [r['call'], cid_of['func::logic_and'],
[
[r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['reg'], obj(0), []]
]
],
[r['call'], cid_of['func::child_indices_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::child_indices']],
[r['reg'], obj(1), []]
]
]
]
]], cid_of['value']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::iterator']]
]
],
[
[r['assert'], [r['exist'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_iterators']], [r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['get_member'], [r['input'], obj(0)], cid_of['dc::index']]
]
]]], 
[r['return'], [r['get_member'], [r['find'], [r['get_member'], [r['input'], obj(1)], cid_of['dc::runtime_iterators']], [r['call'], cid_of['func::math_equal'],
[
[r['get_member'], [r['target']], cid_of['dc::index']],
[r['get_member'], [r['input'], obj(0)], cid_of['dc::index']]
]
]], cid_of['value']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::call']]
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
[r['return'], [r['call'], cid_of['func::run_dynamic_code_object'],
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
[]
], 
[r['return'], [r['call'], cid_of['func::run_hardcoded_code'],
[
[r['reg'], obj(0), []],
[r['reg'], obj(2), []]
]
]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::concept_instance']]
]
],
[
[r['return'], [r['get_member'], [r['input'], obj(0)], cid_of['dc::concept_name']]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::size']]
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
[r['return'], [r['size'], [r['reg'], obj(0), []]]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::logic_or'],
[
[r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::at']]
]
],
[r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::at_reverse']]
]
]
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
[r['get_member'], [r['input'], obj(0)], cid_of['dc::index']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::at']]
]
],
[
[r['return'], [r['at'], [r['reg'], obj(0), []], [r['reg'], obj(1), []]]]
],
[],
[]
], 
[r['return'], [r['at_reverse'], [r['reg'], obj(0), []], [r['reg'], obj(1), []]]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::get_member']]
]
],
[
[r['assign_as_reference'], [r['reg'], obj(0), []], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::target_object']],
[r['input'], obj(1)],
[r['concept_instance'], cid_of['None']]
]
]], 
[r['return'], [r['call'], cid_of['func::get_object_member'],
[
[r['reg'], obj(0), []],
[r['get_member'], [r['input'], obj(0)], cid_of['dc::member_name']]
]
]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::target']]
]
],
[
[r['assert'], [r['call'], cid_of['func::logic_not'], 
[
[r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(2)],
[r['concept_instance'], cid_of['None']]
]
]
]]], 
[r['return'], [r['input'], obj(2)]]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::logic_or'],
[
[r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::find']]
]
],
[r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::exist']]
]
]
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
[r['for'], obj(0), [r['size'], [r['reg'], obj(0), []]],
[
[r['if'], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::expression_for_constraint']],
[r['input'], obj(1)],
[r['at'], [r['reg'], obj(0), []], [r['iterator'], obj(0)]]
]
],
[
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::find']]
]
],
[
[r['return'], [r['at'], [r['reg'], obj(0), []], [r['iterator'], obj(0)]]]
],
[],
[
[r['return'], [r['concept_instance'], cid_of['True']]]
]
]
],
[],
[]
]
]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::find']]
]
],
[
[r['return'], [r['concept_instance'], cid_of['Fail']]]
],
[],
[
[r['return'], [r['concept_instance'], cid_of['False']]]
]
]
],
[],
[]
], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['dcr::count']]
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
[r['assign_as_reference'], [r['reg'], obj(1), []], [obj(0)]], 
[r['for'], obj(0), [r['size'], [r['reg'], obj(0), []]],
[
[r['if'], [r['call'], cid_of['func::solve_expression'],
[
[r['get_member'], [r['input'], obj(0)], cid_of['dc::expression_for_constraint']],
[r['input'], obj(1)],
[r['at'], [r['reg'], obj(0), []], [r['iterator'], obj(0)]]
]
],
[
[r['call_none_return_func'], cid_of['func::increment'],
[
[r['reg'], obj(1), []],
[obj(1)]
]
]
],
[],
[]
]
]
], 
[r['return'], [r['reg'], obj(1), []]]
],
[],
[]
], 
[r['assert'], [r['concept_instance'], cid_of['False']]]
]