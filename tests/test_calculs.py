"""Tests unitaires pour le module de calculs."""

import pytest

from calculs.core import additionner, diviser, multiplier, soustraire


class TestAdditionner:
    def test_entiers(self):
        assert additionner(2, 3) == 5

    def test_flottants(self):
        assert additionner(0.1, 0.2) == pytest.approx(0.3, rel=1e-7)

    def test_type_incorrect(self):
        with pytest.raises(TypeError):
            additionner("2", 3)


class TestSoustraire:
    def test_resultat(self):
        assert soustraire(10, 4) == 6

    def test_resultat_negatif_interdit(self):
        with pytest.raises(ArithmeticError):
            soustraire(1, 4)


class TestMultiplier:
    def test_entiers(self):
        assert multiplier(3, 4) == 12

    def test_type_incorrect(self):
        with pytest.raises(TypeError):
            multiplier("5", 2)


class TestDiviser:
    def test_resultat(self):
        assert diviser(8, 2) == 4

    def test_division_par_zero(self):
        with pytest.raises(ZeroDivisionError):
            diviser(8, 0)

    def test_type_incorrect(self):
        with pytest.raises(TypeError):
            diviser("8", 2)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
