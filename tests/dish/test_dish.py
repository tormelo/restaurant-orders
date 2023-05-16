from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction
import pytest


# Req 2
def test_dish():
    ingredient = Ingredient("queijo mussarela")

    pizza = Dish("pizza", 35.99)
    pizza.add_ingredient_dependency(ingredient, 10)

    lasagna = Dish("lasagna", 24.99)

    assert pizza.name == "pizza"
    assert hash(pizza) == hash(pizza)
    assert hash(pizza) != hash(lasagna)
    assert pizza == pizza
    assert pizza != lasagna
    assert pizza.__repr__() == "Dish('pizza', R$35.99)"

    with pytest.raises(TypeError):
        Dish("pizza", "35.99")

    with pytest.raises(ValueError):
        Dish("pizza", 0)

    assert pizza.recipe.get(ingredient) == 10
    assert pizza.get_ingredients() == {ingredient}

    assert pizza.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
