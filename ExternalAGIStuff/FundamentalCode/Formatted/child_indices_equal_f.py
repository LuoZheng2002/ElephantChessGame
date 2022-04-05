from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
child_indices_equal_f = [
[r['if'], [r['call'], cid_of['func::logic_not'], 
[
[r['call'], cid_of['func::math_equal'],
[
[r['size'], [r['input'], obj(0)]],
[r['size'], [r['input'], obj(1)]]
]
]
]
],
[
[r['return'], [r['concept_instance'], cid_of['False']]]
],
[],
[]
], 
[r['for'], obj(0), [r['size'], [r['input'], obj(0)]],
[
[r['if'], [r['call'], cid_of['func::logic_not'], 
[
[r['call'], cid_of['func::math_equal'],
[
[r['at'], [r['input'], obj(0)], [r['iterator'], obj(0)]],
[r['at'], [r['input'], obj(1)], [r['iterator'], obj(0)]]
]
]
]],
[
[r['return'], [r['concept_instance'], cid_of['False']]]
],
[],
[]
]
]
], 
[r['return'], [r['concept_instance'], cid_of['True']]]
]