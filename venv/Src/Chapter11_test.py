from Chapter8_function import name
import unittest
from Chapter11_testClass import AnonymousSurvey


class NameTestCase(unittest.TestCase):
    """测试name_function"""

    def setUp(self):  # 创建对象，可被其他测试用例使用，避免多次创建，程序首先运行setUp
        question = "Who is your favorite actor"
        self.responses = ['Enlish', 'Russian', 'German']
        self.my_servey = AnonymousSurvey(question)

    def test_first_last_name(self):  # 测试函数，函数必须以test开头
        format_name = name('janis', 'joplin')
        self.assertEqual(format_name, 'Janis Joplin')
        format_name1 = name('J', 'K', 'L')
        self.assertEqual(format_name1, 'J L K')

    def test_store_single_response(self):  # 测试类，函数必须以test开头
        question = "What language did you learn to speak?"
        my_survey = AnonymousSurvey(question)  # 创建实例
        my_survey.store_answer('English')
        self.assertIn('English', my_survey.answers)

    def test_setUp(self):
        for answer in self.responses:
            self.my_servey.store_answer(answer)
        for answer in self.my_servey.answers:
            self.assertIn(answer, self.responses)


unittest.main  # main后不能加括号，否则检测不到test
