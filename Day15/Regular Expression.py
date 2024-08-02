import re

def extract_dates(text):
    pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    return re.findall(pattern, text)

def main():
    text = "The dates are 2024-08-07, 2023-12-25, and 2022-02-30."
    print("Extracted dates:", extract_dates(text))

main()
