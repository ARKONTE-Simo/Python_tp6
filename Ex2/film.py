# film.py

from dataclasses import dataclass, asdict, replace
import json

@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float  # de 0 a 10

    def __post_init__(self):
        if not (0 <= self.note <= 10):
            raise ValueError("La note doit etre comprise entre 0 et 10")

    # Sérialisation JSON
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    # Retourne True si film avant 2000
    def est_classique(self):
        return self.annee < 2000

    # Comparaison par note
    def __lt__(self, autre):
        return self.note < autre.note

    # Création depuis JSON
    @staticmethod
    def from_json(chaine_json: str):
        data = json.loads(chaine_json)
        return Film(**data)


# Exemple d'utilisation
if __name__ == "__main__":
    f1 = Film("Matrix", "Lilly Wachowski", 1999, 9.0)
    f2 = Film("Inception", "Christopher Nolan", 2010, 8.5)

    print(f1.to_json())
    print(f2.to_json())
    print(f1.est_classique())  # True
    print(f1 < f2)  # False, 9.0 < 8.5 ?
    
    chaine = '{"titre": "Titanic", "realisateur": "James Cameron", "annee": 1997, "note": 8.8}'
    f3 = Film.from_json(chaine)
    print(f3.to_json())
