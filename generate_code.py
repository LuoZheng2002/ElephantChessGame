from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
test = [
[r['request'],
[obj(2), obj(3)],
[r['call'], cid_of['func::math_equal'],
[
[r['reg'], obj(4), []],
[obj(5)]
]
],
[
[r['assign'], [r['reg'], obj(4), []], [r['call'], cid_of['func::sum'],
[
[r['reg'], obj(2), []],
[r['reg'], obj(3), []]
]
]]
]
], 
[r['return'], [r['call'], cid_of['func::sum'],
[
[r['reg'], obj(4), []],
[r['reg'], obj(2), []]
]
]]
]