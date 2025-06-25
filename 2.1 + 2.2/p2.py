def is_safe(report):
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing


def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified = report[:i] + report[i + 1:]
        if is_safe(modified):
            return True
    return False


def count_safe_reports(file_path):
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            report = list(map(int, line.strip().split()))
            if is_safe_with_dampener(report):
                safe_count += 1
    return safe_count


# Anwendung
file_path = 'puzzle.txt'
print(f"Anzahl sicherer Berichte: {count_safe_reports(file_path)}")
