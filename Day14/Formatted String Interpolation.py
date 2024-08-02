def interpolate_string(template, values):
    for key, value in values.items():
        template = template.replace(f"{{{key}}}", str(value))
    return template


template = "Hello, {name}. You are {age} years old."
values = {"name": "Amish", "age": 20}
result = interpolate_string(template, values)
print(result)  
