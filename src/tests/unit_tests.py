import unittest
from unittest.mock import patch
from src.gui.mainFrame import MainFrame


class TestMainFrame(unittest.TestCase):

    def setUp(self):
        self.frame = MainFrame(None, 'Requirements')

    @patch('src.behaviour_generator.get_response_chatgpt')
    def test_on_ok(self, mock_get_response):
        self.frame.panel_welcome.Hide()
        self.frame.panel_requirements.Show()
        mock_get_response.return_value = 'test'
        self.frame.panel_requirements.txt_reqs.SetValue('test')
        self.frame.on_ok(None)
        self.assertEqual(self.frame.panel_requirements._visible, False)
        self.assertEqual(self.frame.panel_results._visible, True)
        self.assertEqual(self.frame.panel_results._txtResultsValue, 'test')

    def testOnReturn(self):  # Test on return method of main frame class
        self._visible = False  # Set visibility to false
        self._txtResultsValue = ''  # Set text value to empty string
        self.assertEqual(self._visible, True)   # Visibility should be true after calling on return method
