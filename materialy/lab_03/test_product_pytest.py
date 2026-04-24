# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    return Product("Laptop", 2999.99, 10)


# --- Testy z fixture ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""
    assert product.is_available() == True


def test_is_not_available_when_empty():
    """Sprawdz, czy produkt z quantity=0 nie jest dostepny."""
    empty = Product("Brak towaru", 9.99, 0)
    assert empty.is_available() == False


def test_total_value(product):
    """Sprawdz wartosc calkowita."""
    assert product.total_value() == pytest.approx(2999.99 * 10)


def test_remove_stock(product):
    """Sprawdz, czy usuniecie towaru zmniejsza quantity."""
    product.remove_stock(3)
    assert product.quantity == 7


# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
    (5,   15),   # dodanie 5 do poczatkowych 10 = 15
    (0,   10),   # dodanie 0 = bez zmian
    (100, 110),  # dodanie 100
    (1,   11),   # dodanie 1
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    """Testuje add_stock z roznymi wartosciami."""
    product.add_stock(amount)
    assert product.quantity == expected_quantity


@pytest.mark.parametrize("amount", [-1, -10, -100])
def test_remove_stock_negative_raises(product, amount):
    """Sprawdz, czy ujemna wartosc w remove_stock rzuca ValueError."""
    with pytest.raises(ValueError):
        product.remove_stock(amount)


# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    """Sprawdz, czy proba usuniecia za duzej ilosci rzuca ValueError."""
    with pytest.raises(ValueError):
        product.remove_stock(100)


def test_add_stock_negative_raises(product):
    """Sprawdz, czy ujemna wartosc w add_stock rzuca ValueError."""
    with pytest.raises(ValueError):
        product.add_stock(-5)
