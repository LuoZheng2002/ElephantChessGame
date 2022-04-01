from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
end_game_func_f = [
[r['assign'], [r['reg'], obj(0), []], [r['get_member'], [r['input'], obj(0)], cid_of['xq::pieces']]], 
[r['if'], [r['call'], cid_of['func::math_equal'],
[
[r['count'], [r['reg'], obj(0), []], [r['call'], cid_of['func::compare_concepts'],
[
[r['get_member'], [r['target']], cid_of['xq::piece_name']],
[r['concept_instance'], cid_of['xq::Jiang']]
]
]],
[obj(2)]
]
],
[
[r['return'], [r['concept_instance'], cid_of['False']]]
],
[],
[
[r['return'], [r['concept_instance'], cid_of['True']]]
]
]
]