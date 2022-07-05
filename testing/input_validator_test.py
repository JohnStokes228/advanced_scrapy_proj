import unittest
from spider_try_1.input_transformer import InputTransformer


class TestInputValidator(unittest.TestCase):
    def test_validate_name(self):
        expected_output = InputTransformer.transform_name('WOW, very fantastic body!!')
        self.assertEqual(expected_output, 'wow_very_fantastic_body')

    # noinspection PyTypeChecker
    def test_validate_start_urls_negative_case(self):
        with self.assertRaises(TypeError):
            InputTransformer.transform_input_urls_list(12323)  # raises shit warning if you don't disable type checker

    def test_validate_start_urls_positive_case(self):
        expected_output = InputTransformer.transform_input_urls_list('adas,ada')
        self.assertEqual(expected_output, ['adas', 'ada'])

    def test_validate_manual_run_positive_case(self):
        test_cases = ['Yes', 'no', 'True', 'FALSE', '1', '0']
        expected_output = [True, False, True, False, True, False]
        realised_output = [InputTransformer.transform_manual_run(test_case) for test_case in test_cases]
        self.assertEqual(expected_output, realised_output)

    def test_validate_manual_run_negative_case(self):
        with self.assertRaises(ValueError):
            InputTransformer.transform_manual_run('utter garbage that cant be translated to bool 123.456!@?')


if __name__ == '__main__':
    unittest.main()
