import unittest


class DummyTestCase(unittest.TestCase):
    def test_dummy(self):
        # Тест всегда проходит
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
