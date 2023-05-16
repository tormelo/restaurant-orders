from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    meat = Ingredient("carne")
    bacon = Ingredient("bacon")

    assert meat == meat
    assert hash(meat) == hash(meat)
    assert hash(meat) != hash(bacon)
    assert meat.name == "carne"
    assert meat.__repr__() == "Ingredient('carne')"

    assert meat.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
