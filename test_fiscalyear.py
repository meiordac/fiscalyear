import fiscalyear
import pytest


class TestFiscalYear:

    @pytest.fixture(scope='class')
    def a(self):
        return fiscalyear.FiscalYear(2016)

    @pytest.fixture(scope='class')
    def b(self):
        return fiscalyear.FiscalYear(2017)

    @pytest.fixture(scope='class')
    def c(self):
        return fiscalyear.FiscalYear('2017')

    def test_basic(self, a):
        assert a.fiscal_year == 2016

    def test_repr(self, a):
        assert repr(a) == 'fiscalyear.FiscalYear(2016)'

    def test_str(self, a):
        assert str(a) == 'FY2016'

    def test_less_than(self, a, b):
        assert a < b

    def test_less_than_equals(self, a, b, c):
        assert a <= b <= c

    def test_equals(self, b, c):
        assert b == c

    def test_not_equals(self, a, b):
        assert a != b

    def test_greater_than(self, a, b):
        assert b > a

    def test_greater_than_equals(self, a, b, c):
        assert c >= b >= a

    def test_from_string(self, c):
        assert c.fiscal_year == 2017

    def test_wrong_type(self):
        with pytest.raises(TypeError):
            x = fiscalyear.FiscalYear(2017.5)

        with pytest.raises(TypeError):
            y = fiscalyear.FiscalYear('hello world')

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            x = fiscalyear.FiscalYear(0)

        with pytest.raises(ValueError):
            y = fiscalyear.FiscalYear(-2017)


class TestFiscalQuarter:

    @pytest.fixture(scope='class')
    def a(self):
        return fiscalyear.FiscalQuarter(2016, 4)

    @pytest.fixture(scope='class')
    def b(self):
        return fiscalyear.FiscalQuarter(2017, 1)

    @pytest.fixture(scope='class')
    def c(self):
        return fiscalyear.FiscalQuarter(2017, 2)

    @pytest.fixture(scope='class')
    def d(self):
        return fiscalyear.FiscalQuarter(2017, 3)

    @pytest.fixture(scope='class')
    def e(self):
        return fiscalyear.FiscalQuarter(2017, 4)

    @pytest.fixture(scope='class')
    def f(self):
        return fiscalyear.FiscalQuarter(2018, 1)

    @pytest.fixture(scope='class')
    def g(self):
        return fiscalyear.FiscalQuarter('2018', '1')

    def test_basic(self, a):
        assert a.fiscal_year == 2016
        assert a.quarter == 4

    def test_repr(self, a):
        assert repr(a) == 'fiscalyear.FiscalQuarter(2016, 4)'

    def test_str(self, a):
        assert str(a) == 'FY2016 Q4'

    def test_less_than(self, a, b, c, d, e, f):
        assert a < b < c < d < e < f

    def test_less_than_equals(self, a, b, c, d, e, f, g):
        assert a <= b <= c <= d <= e <= f <= g

    def test_equals(self, f, g):
        assert f == g

    def test_not_equals(self, b, c, g):
        # Same year, different quarter
        assert b != c

        # Same quarter, different year
        assert b != g

    def test_greater_than(self, a, b, c, d, e, f):
        assert f > e > d > c > b > a

    def test_greater_than_equals(self, a, b, c, d, e, f, g):
            assert g >= f >= e >= d >= c >= b >= a

    def test_from_string(self, g):
        assert g.fiscal_year == 2018
        assert g.quarter == 1

    def test_wrong_type(self):
        with pytest.raises(TypeError):
            x = fiscalyear.FiscalQuarter(2017.5, 1.2)

        with pytest.raises(TypeError):
            y = fiscalyear.FiscalQuarter('hello', 'world')

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            x = fiscalyear.FiscalQuarter(2017, 0)

        with pytest.raises(ValueError):
            y = fiscalyear.FiscalQuarter(2017, 5)

        with pytest.raises(ValueError):
            z = fiscalyear.FiscalQuarter(0, 2)