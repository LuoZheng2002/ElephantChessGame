from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
test = [
[r['assign'], [r['reg'], obj(0), []], [obj(2)]], 
[r['for'], obj(0), [obj(3)],
[
[r['call_none_return_func'], cid_of['func::increment'],
[
[r['reg'], obj(0), []],
[obj(5)]
]
]
]
], 
[r['return'], [r['reg'], obj(0), []]]
]