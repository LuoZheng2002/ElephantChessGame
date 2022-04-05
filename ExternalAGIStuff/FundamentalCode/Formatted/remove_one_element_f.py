from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
remove_one_element_f = [
[r['for'], obj(0), [r['size'], [r['input'], obj(2)]],
[
[r['if'], [r['call'], cid_of['func::solve_expression'],
[
[r['input'], obj(0)],
[r['input'], obj(1)],
[r['at'], [r['input'], obj(2)], [r['iterator'], obj(0)]]
]
],
[
[r['call_none_return_func'], cid_of['func::remove_element_by_index'],
[
[r['input'], obj(2)],
[r['iterator'], obj(0)]
]
], 
[r['return'], [r['concept_instance'], cid_of['True']]]
],
[],
[]
]
]
], 
[r['return'], [r['concept_instance'], cid_of['False']]]
]