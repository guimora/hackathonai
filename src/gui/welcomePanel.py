import wx


class WelcomePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(800, 700),
                          style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        # Properties
        self.font = wx.Font(16, family=wx.FONTFAMILY_DEFAULT, style=0, weight=400, underline=False,
                            faceName="", encoding=wx.FONTENCODING_DEFAULT)
        self.font_text = wx.Font(16, family=wx.FONTFAMILY_SCRIPT, style=0, weight=100, underline=False,
                            faceName="", encoding=wx.FONTENCODING_DEFAULT)

        # Widgets
        self.lbl_welcome = wx.StaticText(self, label='Please enter your text')
        self.btn_continue = wx.Button(self, label='Continue')
        self.lbl_welcome.SetFont(self.font)
        self.btn_continue.SetFont(self.font)

        # Sizers
        self.sizer_frame = wx.BoxSizer(wx.VERTICAL)
        self.sizer_frame.Add(self.lbl_welcome, flag=wx.TOP, border=100)
        self.sizer_frame.Add(self.btn_continue, flag=wx.CENTER)

        self.SetSizer(self.sizer_frame)
        self.SetAutoLayout(1)
        self.Show()
