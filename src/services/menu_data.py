import pandas as pd
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        df = pd.read_csv(source_path)

        dishes_dict = {}

        for dish, price, ingredient_name, ingredient_amount in df.itertuples(
            index=False
        ):
            if dish not in dishes_dict:
                dishes_dict[dish] = Dish(dish, price)

            ingredient = Ingredient(ingredient_name)

            dishes_dict[dish].add_ingredient_dependency(
                ingredient, ingredient_amount
            )

        self.dishes = set(dishes_dict.values())
