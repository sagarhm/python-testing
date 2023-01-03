import unittest
from unittest.mock import patch
from gold import Gold


class Test_gold(unittest.TestCase):

    def test_gold(self):



        with patch('gold.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
   

            obj = Gold()
            response = obj.get

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()






