# content of test_class.py
class Dummy:
    def check(self):
        return True

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = Dummy()
        assert hasattr(x, "check")