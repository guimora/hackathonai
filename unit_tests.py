

import unittest
from unittest.mock import patch
from src.behaviour_generator import get_response_chatgpt
from reqPanel import RequirementsPanel
from resultPanel import ResultsPanel
from MainFrame import MainFrame


class TestMainFrame(unittest.TestCase):

    def setUp(self):
        self.frame = MainFrame(None, 'Requirements')

    @patch('src.behaviour_generator.get_response_chatgpt')
    def test_on_ok(self, mock_get_response):
        mock_get_response.return_value = 'test'

        self.frame.panel_requirements.txt_reqs.SetValue('test')

        self.frame.on_ok(None)

        self.assertEqual(self.frame.panel_requirements._visible, False)
        self.assertEqual(self.frame.panel_results._visible, True)
        self.assertEqual(self.frame.panel_results._txtResultsValue, 'test')

    def testOnReturn(self):  # Test on return method of main frame class 

        self._visible = False  # Set visibility to false 

        self._txtResultsValue = ''  # Set text value to empty string 

        self._onReturn()  # Call on return method 

        # Verify if the tests passed or not: 
        self.assertEqual(self._visible, True)   # Visibility should be true after calling on return method  
        self