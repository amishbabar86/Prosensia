import re

def validate_data(data_entries):
    report = []
    for entry in data_entries:
        entry_report = {"entry": entry}
        entry_report["length"] = len(entry)
        entry_report["is_alpha"] = entry.isalpha()
        entry_report["is_numeric"] = entry.isnumeric()
        entry_report["is_alphanumeric"] = entry.isalnum()
        entry_report["is_email"] = bool(re.match(r"[^@]+@[^@]+\.[^@]+", entry))
        entry_report["is_date"] = bool(re.match(r"\d{4}-\d{2}-\d{2}", entry))
        report.append(entry_report)
    return report

def main():
    data_entries = ["hello", "12345", "hello123", "test@example.com", "2024-08-07", "invalid-date"]
    report = validate_data(data_entries)
    for entry_report in report:
        print(entry_report)

main()
