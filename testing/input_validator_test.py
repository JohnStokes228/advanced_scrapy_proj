import unittest
from spiders.input_validator import InputValidator


class TestInputValidator(unittest.TestCase):
    def test_validate_name(self):
        expected_output = InputValidator.validate_name('wow, very fantastic body!!')
        self.assertEqual(expected_output, 'wow_very_fantastic_body')

    # noinspection PyTypeChecker
    def test_validate_start_urls_negative_case(self):
        with self.assertRaises(TypeError):
            InputValidator.validate_start_urls(12323)  # raises annoying warning if you don't disable type checker here

    def test_validate_start_urls_positive_case(self):
        expected_output = InputValidator.validate_start_urls('adas,ada')
        self.assertEqual(expected_output, ['adas', 'ada'])

    def test_validate_manual_run_positive_case(self):
        test_cases = ['Yes', 'no', 'True', 'FALSE', '1', '0']
        expected_output = [True, False, True, False, True, False]
        realised_output = [InputValidator.validate_manual_run(test_case) for test_case in test_cases]
        self.assertEqual(expected_output, realised_output)

    def test_validate_manual_run_negative_case(self):
        with self.assertRaises(ValueError):
            InputValidator.validate_manual_run('utter garbage that cant be translated to bool 123.456!@?')


if __name__ == '__main__':
    unittest.main()
