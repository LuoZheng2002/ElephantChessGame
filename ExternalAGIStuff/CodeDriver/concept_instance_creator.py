from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.IDs.concept_ids import cid_of
concept_attributes_dict = {
    cid_of['natural_number']: (cid_of['content'],)
}


def create_concept_instance(concept_id) -> AGIObject:
    global concept_attributes_dict
    if concept_id not in concept_attributes_dict.keys():
        return AGIObject(concept_id, dict())
    else:
        attributes = dict()
        for i in concept_attributes_dict[concept_id]:
            attributes.update({i: None})
        return AGIObject(concept_id, attributes)
