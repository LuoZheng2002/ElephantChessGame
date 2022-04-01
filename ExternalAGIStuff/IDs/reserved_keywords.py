from ExternalAGIStuff.IDs.concept_ids import cid_of


def generate_reserved_keywords():
    reserved = dict()
    for i in cid_of.keys():
        if i.find('dcr::') == 0:
            reserved.update({i[5:]: cid_of[i]})
    return reserved


r = generate_reserved_keywords()

rr = dict([(i, j) for (j, i) in r.items()])
