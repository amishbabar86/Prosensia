import json

def dict_to_json_and_back(dictionary):
    try:
        json_string = json.dumps(dictionary)
        converted_dict = json.loads(json_string)
        return converted_dict
    except (TypeError, json.JSONDecodeError) as e:
        return dictionary, f"Error: {e}"


result = dict_to_json_and_back({"name": "John", "age": 30})
print(result)  
