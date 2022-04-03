from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.IDs.concept_ids import cid_of
concept_attributes_dict = {
    cid_of['natural_number']: (cid_of['content'],),
    cid_of['xq::chessboard']: (cid_of['xq::pieces'], cid_of['xq::whose_turn']),
    cid_of['xq::piece']: (cid_of['xq::piece_owner'], cid_of['xq::piece_name'], cid_of['xq::position']),
    cid_of['list']: (cid_of['content'],),
    cid_of['interface::find_winning_determining_variables_find_variable_changing_code']:
        (cid_of['interface_member::winning_determining_variables'],),
    cid_of['dc::runtime_registers']: (cid_of['content'],),
    cid_of['dc::runtime_iterators']: (cid_of['content'],),

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
