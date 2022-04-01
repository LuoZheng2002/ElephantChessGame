from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
end_game_benefit_f = [
[r['if'], [r['exist'], [r['get_member'], [r['input'], obj(0)], cid_of['xq::pieces']], [r['call'], cid_of['func::logic_and'],
[
[r['call'], cid_of['func::logic_not'], 
[
[r['call'], cid_of['func::compare_concepts'],
[
[r['get_member'], [r['target']], cid_of['xq::piece_owner']],
[r['input'], obj(1)]
]
]
]],
[r['call'], cid_of['func::compare_concepts'],
[
[r['get_member'], [r['target']], cid_of['xq::piece_name']],
[r['concept_instance'], cid_of['xq::Jiang']]
]
]
]
]],
[
[r['return'], [obj(0)]]
],
[],
[]
], 
[r['return'], [obj(1)]]
]