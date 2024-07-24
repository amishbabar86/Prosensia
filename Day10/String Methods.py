def transform_string(s):
    return {
        "lowercase": s.lower(),
        "uppercase": s.upper(),
        "titlecase": s.title()
    }


print(transform_string("Hello World"))

