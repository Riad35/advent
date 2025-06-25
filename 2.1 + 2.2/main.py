def is_safe_report(levels):
    # Prüfen, ob alle Unterschiede zwischen 1 und 3 liegen
    diffs = [abs(levels[i] - levels[i + 1]) for i in range(len(levels) - 1)]
    if not all(1 <= diff <= 3 for diff in diffs):
        return False

    # Prüfen, ob streng monoton steigend oder fallend
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    return increasing or decreasing


def count_safe_reports(file_path):
    safe_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            levels = list(map(int, line.strip().split()))
            if is_safe_report(levels):
                safe_count += 1

    return safe_count


# Beispiel: Pfad zur Datei anpassen
file_path = 'puzzle.txt'
safe_reports = count_safe_reports(file_path)
print(f"Anzahl sicherer Berichte: {safe_reports}")
