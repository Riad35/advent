# Path ist eine Klasse aus Pathlib- Module. bietet einfache arbeit mit Dateipfaden
from pathlib import Path
# Defines a function named
def read_numbers_from_file(filename: Path) -> tuple[list[int], list[int]]:
    # Liest zahlen aus einer Datei und gibt 2 Listen aus
    left_list, right_list = [], []
    # Opens the file in read mode
    with filename.open("r", encoding="utf-8") as file:
        # Loops through each line
        for line in file:
            try:
                l, r = map(int, line.split())
                # Adds the first number (l) to left_list and the second number (r) to right_list
                left_list.append(l)
                right_list.append(r)
            except ValueError:
                print(f"Überspringe ungültige Zeile: {line.strip()}")
    # Returns beide listen
    return left_list, right_list


# Defines a function, which calculates the sum of absolute differences
def total_distance(left_list: list[int], right_list: list[int]) -> int:
    # Sort function .sort()
    left_list.sort()
    right_list.sort()
    return sum(abs(l - r) for l, r in zip(left_list, right_list))


if __name__ == "__main__":
    filename = Path(r"numbers.txt")
    if filename.exists():
        left, right = read_numbers_from_file(filename)
        result = total_distance(left, right)
        print(f"Gesamtdistanz: {result}")
    else:
        print(f"Datei {filename} nicht gefunden.")
