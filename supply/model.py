from .database import *
class Model:
    """
    Modellen:   Klassen innehåller datastrukturen.
                -- Kontrollern kan skicka meddelanden till Modellen
                   och Modellen kan besvara dem.
                -- Modellen använder delegater för att sända meddelanden
                   till Kontrollern vid förändring.
                -- Modellen kommunicerar ALDRIG med Vyn.
                -- Modellen har getters och setters för att kommunicera
                   med Kontrollern.
    """
    def __init__(self, vc):
        self.vc = vc
        self.db = Database()

    def data_changed_delegate(self):
        self.vc.data_changed_delegate()

    def get_recipes_var(self):
        return [list(i) for i in self.db.get_recipes()]

    def set_recipes_var(self, product, ingredient, amount, unit):
        self.db.set_recipes(product, ingredient, amount, unit)
        self.data_changed_delegate()

    def get_products_var(self):
        return [list(i) for i in self.db.get_products()]

    def set_products_var(self, product_name):
        self.db.set_product(product_name)
        self.data_changed_delegate()

    def del_products_var(self, product_id):
        self.db.del_product(product_id)
        self.data_changed_delegate()

    def get_ingredients_var(self):
        return [list(i) for i in self.db.get_ingredients()]

    def set_ingredients_var(self, ingredients_name):
        self.db.set_ingredients(ingredients_name)
        self.data_changed_delegate()

    def del_ingredients_var(self, ingredients_id):
        self.db.del_ingredients(ingredients_id)
        self.data_changed_delegate()

    def get_units_var(self):
        """
        Returnerar en lista på samtliga enheter och dess namn.
        Returns: Lista på enheter och dess namn.
        """
        return [list(i) for i in self.db.get_units()]
