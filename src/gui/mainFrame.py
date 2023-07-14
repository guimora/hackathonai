import wx
from reqPanel import RequirementsPanel
from resultPanel import ResultsPanel
from welcomePanel import WelcomePanel
from src.behaviour_generator import get_response_chatgpt
import src.utils.ticketing_jira as ticketing_jira


class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 350), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.panel_requirements = RequirementsPanel(self)
        self.panel_results = ResultsPanel(self)
        self.panel_welcome = WelcomePanel(self)
        self.panel_requirements.Hide()
        self.panel_results.Hide()
        self.response_text = ''
        self.request_text = ''
        self.response_id = ''

        self.sizer_frame = wx.BoxSizer(wx.VERTICAL)
        self.sizer_frame.Add(self.panel_requirements, 1, wx.EXPAND)
        self.sizer_frame.Add(self.panel_results, 1, wx.EXPAND)
        self.sizer_frame.Add(self.panel_welcome, 1, wx.EXPAND)

        self.Bind(wx.EVT_BUTTON, self.on_ok, self.panel_requirements.btn_ok)
        self.Bind(wx.EVT_BUTTON, self.on_return, self.panel_results.btn_return)
        self.Bind(wx.EVT_BUTTON, self.on_ok_result, self.panel_results.btn_ok)
        self.Bind(wx.EVT_BUTTON, self.on_continue, self.panel_welcome.btn_continue)

        self.SetSizer(self.sizer_frame)
        self.SetAutoLayout(1)
        self.Show()

    def on_ok(self, event):
        self.request_text = self.panel_requirements.txt_reqs.GetValue()
        self.response_text = get_response_chatgpt(self.request_text)
        self.panel_requirements.Hide()
        self.panel_results.txt_results.SetValue(self.response_text)
        self.panel_results.Show()
        self.Layout()

    def on_return(self, event):
        self.panel_results.Hide()
        self.panel_requirements.Show()
        self.Layout()

    def on_ok_result(self, event):
        self.response_id = ticketing_jira.create_issue(self.request_text, self.response_text)
        if self.response_id is not None:
            self.dialog_message = wx.MessageDialog(self, "Jira Issue was created successfully", "Success", wx.OK | wx.CENTER)
        else:
            self.dialog_message = wx.MessageDialog(self, "Jira Issue was not created", "Error",
                                                   wx.OK | wx.CENTER)
        self.dialog_message.ShowModal()

    def on_continue(self, event):
        self.panel_welcome.Hide()
        self.panel_requirements.Show()
        self.Layout()

app = wx.App(False)
frame = MainFrame(None, 'Requirements')
app.MainLoop()
