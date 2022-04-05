from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
run_dynamic_code_object_f = [
[r['assign'], [r['reg'], obj(0), []], [r['concept_instance'], cid_of['dc::runtime_inputs']]], 
[r['for'], obj(0), [r['size'], [r['input'], obj(1)]],
[
[r['assign'], [r['reg'], obj(1), [[r['iterator'], obj(0)]]], [r['concept_instance'], cid_of['dc::input_container']]], 
[r['assign'], [r['get_member'], [r['reg'], obj(1), [[r['iterator'], obj(0)]]], cid_of['dc::index']], [r['iterator'], obj(0)]], 
[r['assign'], [r['get_member'], [r['reg'], obj(1), [[r['iterator'], obj(0)]]], cid_of['value']], [r['at'], [r['input'], obj(1)], [r['iterator'], obj(0)]]], 
[r['append'], [r['reg'], obj(0), []], [r['reg'], obj(1), [[r['iterator'], obj(0)]]]]
]
], 
[r['assign'], [r['reg'], obj(2), []], [r['concept_instance'], cid_of['dc::runtime_registers']]], 
[r['assign'], [r['reg'], obj(3), []], [r['concept_instance'], cid_of['dc::runtime_iterators']]], 
[r['assign'], [r['reg'], obj(4), []], [r['concept_instance'], cid_of['dc::runtime_memory']]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(4), []], cid_of['dc::runtime_inputs']], [r['reg'], obj(0), []]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(4), []], cid_of['dc::runtime_registers']], [r['reg'], obj(2), []]], 
[r['assign_as_reference'], [r['get_member'], [r['reg'], obj(4), []], cid_of['dc::runtime_iterators']], [r['reg'], obj(3), []]], 
[r['for'], obj(1), [r['size'], [r['input'], obj(0)]],
[
[r['assign'], [r['reg'], obj(5), [[r['iterator'], obj(1)]]], [r['call'], cid_of['func::process_line'],
[
[r['at'], [r['input'], obj(0)], [r['iterator'], obj(1)]],
[r['reg'], obj(4), []]
]
]], 
[r['assert'], [r['call'], cid_of['func::logic_not'], 
[
[r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(5), [[r['iterator'], obj(1)]]],
[r['concept_instance'], cid_of['dc::line_signal_break']]
]
]
]]], 
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['reg'], obj(5), [[r['iterator'], obj(1)]]],
[r['concept_instance'], cid_of['dc::line_signal_return']]
]
],
[
[r['return'], [r['get_member'], [r['reg'], obj(5), [[r['iterator'], obj(1)]]], cid_of['dc::line_return_value']]]
],
[],
[]
]
]
], 
[r['return'], [r['concept_instance'], cid_of['None']]]
]