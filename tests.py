import pytest

from main import rewrite_letter

GOOD_LOWERED_INPUTS = [
    ("Hola Mundo", "El Mundo es un lugar especial, hola!"),
    ("Hola Mundo", "ElMundoesunlugarespecial,hola!"),
]

GOOD_NOT_LOWERED_INPUTS = [
    ("Hola Mundo", "El Mundo es un lugar especial, Hola!"),
    ("Hola Mundo", "ElMundoesunlugarespecial,Hola!"),
]

BAD_INPUTS = [
    ("Hola Mundo", "El es un lugar especial, hola!"),
    ("Hola Mundo", "Elesunlugarespecial,hola!"),
    ("Hola Mundo", ""),
]


@pytest.mark.parametrize("letter,article", GOOD_LOWERED_INPUTS)
def test_rewrite_letter_with_good_article_lowered_should_succeed(
    letter, article
):
    rewrited = rewrite_letter(letter, article)

    assert rewrited == "hola mundo"


@pytest.mark.parametrize("letter,article", GOOD_NOT_LOWERED_INPUTS)
def test_rewrite_letter_with_good_article_not_lowered_should_succeed(
    letter, article
):
    rewrited = rewrite_letter(letter, article, lowered=False)

    assert rewrited == "Hola Mundo"


@pytest.mark.parametrize("letter,article", GOOD_LOWERED_INPUTS)
def test_rewrite_letter_with_good_article_not_lowered_should_fail(
    letter, article
):
    rewrited = rewrite_letter(letter, article, lowered=False)

    assert rewrited is None


@pytest.mark.parametrize("letter,article", BAD_INPUTS)
def test_rewrite_letter_with_bad_article(letter, article):
    rewrited = rewrite_letter(letter, article)

    assert rewrited is None
