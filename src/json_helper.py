from  flask import jsonify

def jsonify_array(array):
    array_dict = []
    for item in array:
        array_dict.append(item.serialize())

    return jsonify(array_dict)