def split_and_join_conditionally(input_str, delimiter1, delimiter2, condition_fn):
    parts = input_str.split(delimiter1)
    filtered_parts = [part for part in parts if condition_fn(part)]
    return delimiter2.join(filtered_parts)


input_str = "this,is,a,test,string"
print(split_and_join_conditionally(input_str, ",", "-", lambda s: len(s) > 3))  
