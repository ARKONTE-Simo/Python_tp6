# livre.py

from dataclasses import dataclass, asdict, replace
import json

@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    # Extension : retourne un nouveau livre avec prix reduit
    def promo(self, prix_reduit: float):
        return replace(self, prix=prix_reduit)

    # Extension : comparaison par prix
    def __lt__(self, autre):
        return self.prix < autre.prix

    # Extension : reconstituer un Livre depuis une chaine JSON
    @staticmethod
    def from_json(chaine_json: str):
        data = json.loads(chaine_json)
        return Livre(**data)

# Exemple d'utilisation
if __name__ == "__main__":
    livre = Livre("1984", "George Orwell", 1949, 9.90)
    print(livre.to_json())

    livre_promo = livre.promo(7.90)
    print(livre_promo.to_json())

    chaine = '{"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupery", "annee": 1943, "prix": 12.5}'
    nouveau_livre = Livre.from_json(chaine)
    print(nouveau_livre.to_json())

    # Comparaison
    print(livre < livre_promo)  # False
