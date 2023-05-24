import lesson_phonebook
import unittest
import json

class TestPhonebook(unittest.TestCase):

    def setUp(self):
        # create a temporary phonebook.json file with some initial data
        data = [
            {'telephone': '111-111-1111', 'name': 'John', 'last name': 'Doe', 'full name': 'John Doe',
             'city': 'New York'},
            {'telephone': '222-222-2222', 'name': 'Jane', 'last name': 'Doe', 'full name': 'Jane Doe',
             'city': 'Los Angeles'}
        ]
        with open('phonebook.json', 'w') as file:
            json.dump(data, file)

    def test_add_entry(self):
        # simulate user input for adding a new entry
        user_input = ['1', '333-333-3333', 'Mike', 'Smith', 'New York', '8']
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            phonebook()1

    with open('phonebook.json', 'r') as file:
        data = json.load(file)
        self.assertIn({'telephone': '333-333-3333', 'name': 'Mike', 'last name': 'Smith', 'full name': 'Mike Smith',
                       'city': 'New York'}, data)

if __name__ == "__main__":
 unittest.main()

# import unittest
# import json
# from unittest.mock import mock_open, patch
# from lesson_phonebook import phonebook
#
# class TestLoadPhonebook(unittest.TestCase):
#
#     def test_load_phonebook(self):
#         book_name = "test_book"
#         phonebook = {"1234567890": {"name": "John", "surname": "Doe", "phone": "1234567890", "city": "New York"}}
#         json_data = json.dumps(phonebook)
#
#         with patch("builtins.open", mock_open(read_data=json_data)):
#             result = load_phonebook(book_name)
#         self.assertEqual(result, phonebook)
# if __name__ == "__main__":
#  unittest.main()
