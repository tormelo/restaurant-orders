import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        dish_names = []
        ingredients = []
        prices = []
        restrictions = []

        for dish in self.menu_data.dishes:
            dish_names.append(dish.name)
            ingredients.append(dish.get_ingredients())
            prices.append(dish.price)
            restrictions.append(dish.get_restrictions())

        df = pd.DataFrame(
            {
                "dish_name": dish_names,
                "ingredients": ingredients,
                "price": prices,
                "restrictions": restrictions,
            }
        )

        dishes_bool_map = df["restrictions"].map(
            lambda restrictions: False if restriction in restrictions else True
        )

        if not restriction:
            return df
        else:
            return df.loc[dishes_bool_map]
