import wx


class RequirementsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(800, 700),
                          style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        # Properties
        self.font = wx.Font(16, family=wx.FONTFAMILY_DEFAULT, style=0, weight=400, underline=False,
                            faceName="", encoding=wx.FONTENCODING_DEFAULT)
        self.font_text = wx.Font(16, family=wx.FONTFAMILY_SCRIPT, style=0, weight=100, underline=False,
                            faceName="", encoding=wx.FONTENCODING_DEFAULT)

        # Widgets
        self.lbl_insert_reqs = wx.StaticText(self, label='Please enter your text')
        self.txt_reqs = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(650, 166))
        self.btn_ok = wx.Button(self, label='Ok')
        self.lbl_insert_reqs.SetFont(self.font)
        self.txt_reqs.SetFont(self.font_text)
        self.btn_ok.SetFont(self.font)

        # Sizers
        self.sizer_reqs = wx.BoxSizer(wx.VERTICAL)
        self.sizer_reqs.Add(self.lbl_insert_reqs, flag=wx.LEFT, border=75)
        self.sizer_reqs.Add(self.txt_reqs, flag=wx.LEFT, border=75)

        self.sizer_frame = wx.BoxSizer(wx.VERTICAL)
        self.sizer_frame.Add(self.sizer_reqs, flag=wx.TOP | wx.BOTTOM, border=35)
        self.sizer_frame.Add(self.btn_ok, flag=wx.CENTER)

        self.SetSizer(self.sizer_frame)
        self.SetAutoLayout(1)
        self.Show()
