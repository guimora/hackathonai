import wx
from reqPanel import RequirementsPanel
from resultPanel import ResultsPanel


class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 350), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.panel_requirements = RequirementsPanel(self)
        self.panel_results = ResultsPanel(self)
        self.panel_results.Hide()
        self.test_text = ''

        self.sizer_frame = wx.BoxSizer(wx.VERTICAL)
        self.sizer_frame.Add(self.panel_requirements, 1, wx.EXPAND)
        self.sizer_frame.Add(self.panel_results, 1, wx.EXPAND)

        self.Bind(wx.EVT_BUTTON, self.on_ok, self.panel_requirements.btn_ok)
        self.Bind(wx.EVT_BUTTON, self.on_return, self.panel_results.btn_return)

        self.SetSizer(self.sizer_frame)
        self.SetAutoLayout(1)
        self.Show()

    def on_ok(self, event):
        self.test_text = 'Update here'
        self.panel_requirements.Hide()
        self.panel_results.txt_results.SetValue(self.test_text)
        self.panel_results.Show()
        self.Layout()

    def on_return(self, event):
        self.panel_results.Hide()
        self.panel_requirements.Show()
        self.Layout()

app = wx.App(False)
frame = MainFrame(None, 'Requirements')
app.MainLoop()
