from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.IDs.concept_ids import cid_of
concept_attributes_dict = {
    cid_of['natural_number']: (cid_of['content'],),
    cid_of['xq::chessboard']: (cid_of['xq::pieces'], cid_of['xq::whose_turn']),
    cid_of['xq::piece']: (cid_of['xq::piece_owner'], cid_of['xq::piece_name'], cid_of['xq::position']),
    cid_of['list']: (cid_of['content'],),
    cid_of['interface::find_winning_determining_variables_find_variable_changing_code']:
        (cid_of['interface_member::winning_determining_variables'],),
    cid_of['dc::runtime_inputs']: (cid_of['content'],),
    cid_of['dc::runtime_registers']: (cid_of['content'],),
    cid_of['dc::runtime_iterators']: (cid_of['content'],),
    cid_of['dc::runtime_memory']: (cid_of['dc::runtime_inputs'],
                                   cid_of['dc::runtime_registers'],
                                   cid_of['dc::runtime_iterators']),
    cid_of['dc::line_signal_return']: (cid_of['dc::line_return_value'],),
    cid_of['dc::input_container']: (cid_of['dc::index'], cid_of['value']),
    cid_of['dc::register_container']: (cid_of['dc::index'], cid_of['dc::child_indices'], cid_of['value']),
    cid_of['dc::iterator_container']: (cid_of['dc::index'], cid_of['value']),
}


def create_concept_instance(concept_id) -> AGIObject:
    if concept_id not in concept_attributes_dict.keys():
        return AGIObject(concept_id, dict())
    else:
        attributes = dict()
        for i in concept_attributes_dict[concept_id]:
            attributes.update({i: None})
        return AGIObject(concept_id, attributes)
