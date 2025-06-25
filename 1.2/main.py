from pathlib import Path


def read_numbers_from_file(filename: Path) -> tuple[list[int], dict[int, int]]:
    """Liest Zahlen aus einer Datei und gibt eine Liste und ein Häufigkeits-Dictionary zurück."""
    left_list = []
    haeufigkeit = {}

    try:
        with filename.open("r", encoding="utf-8") as file:
            for line in file:
                try:
                    l, r = map(int, line.split())
                    left_list.append(l)

                    # Häufigkeit direkt aktualisieren
                    haeufigkeit[r] = haeufigkeit.get(r, 0) + 1
                except ValueError:
                    print(f"Überspringe ungültige Zeile: {line.strip()}")
    except FileNotFoundError:
        print(f"Datei {filename} nicht gefunden.")

    return left_list, haeufigkeit


def calculate_similarity_score(left_list: list[int], haeufigkeit: dict[int, int]) -> int:
    """Berechnet die Ähnlichkeitsbewertung basierend auf den Häufigkeiten."""
    return sum(num * haeufigkeit.get(num, 0) for num in left_list)


# Hauptprogramm
if __name__ == "__main__":
    filename = Path("numbers.txt")

    if filename.exists():
        left_list, haeufigkeit = read_numbers_from_file(filename)

        # Ergebnisse ausgeben
        similarity_score = calculate_similarity_score(left_list, haeufigkeit)
        print(f"Ähnlichkeitsbewertung: {similarity_score}")
    else:
        print(f"Datei {filename} nicht gefunden.")