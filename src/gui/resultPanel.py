import wx


class ResultsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(800, 700), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        # Properties
        self.font = wx.Font(16, family=wx.FONTFAMILY_DEFAULT, style=0, weight=400, underline=False,
                            faceName="", encoding=wx.FONTENCODING_DEFAULT)
        # self.SetBackgroundColour((237, 231, 230))

        # Widgets
        self.lbl_insert_reqs = wx.StaticText(self, label='Validate results, edit if necessary')
        self.txt_results = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(650, 166))
        self.btn_ok = wx.Button(self, label='Ok')
        self.btn_return = wx.Button(self, label='Return')
        self.lbl_insert_reqs.SetFont(self.font)
        self.txt_results.SetFont(self.font)
        self.btn_ok.SetFont(self.font)
        self.btn_return.SetFont(self.font)

        # Sizers
        self.sizer_results = wx.BoxSizer(wx.VERTICAL)
        self.sizer_results.Add(self.lbl_insert_reqs, flag=wx.LEFT, border=75)
        self.sizer_results.Add(self.txt_results, flag=wx.LEFT, border=75)

        self.sizer_button = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_button.Add(self.btn_ok)
        self.sizer_button.Add(self.btn_return, flag=wx.LEFT, border=15)

        self.sizer_frame = wx.BoxSizer(wx.VERTICAL)
        self.sizer_frame.Add(self.sizer_results, flag=wx.TOP | wx.BOTTOM, border=25)
        self.sizer_frame.Add(self.sizer_button, flag=wx.CENTER)

        self.SetSizer(self.sizer_frame)
        self.SetAutoLayout(1)
        self.Show()


