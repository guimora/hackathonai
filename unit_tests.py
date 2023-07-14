

import unittest
import wx
from src.gui.reqPanel import RequirementsPanel
from src.gui.resultPanel import ResultsPanel
from src.gui.welcomePanel import WelcomePanel
from src.behaviour_generator import get_response_chatgpt
import src.utils.ticketing_jira as ticketing_jira


class TestMainFrame(unittest.TestCase):

    def setUp(self):
        self.app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
        self.frame = MainFrame(None, 'Requirements')  # A Frame is a top-level window

    def tearDown(self):
        self.frame = None  # Close the frame

    def test_on_ok(self):
        self.frame._on_ok()  # Call the method to be tested

        self.assertEqual(self.frame._request_text, self.frame._panel_requirements._txt_reqs)  # Verify if the request text is equal to the value of the text box in the requirements panel 
        self.assertEqual(self.frame._response_text, get_response_chatgpt(self._request_text))  # Verify if the response text is equal to the value returned by get response chatgpt function  

    def test_on_return(self):
        self._onReturn()  # Call the method to be tested

        self.assertFalse(self._panelResults._isShown())  # Verify if results panel is hidden after return button is clicked  
        self.assertTrue(self._panelRequirements._isShown())  # Verify if requirements panel is shown after return button is clicked  

    def testOnOkResult(self):
        self._onOkResult()  # Call the method to be tested

        self