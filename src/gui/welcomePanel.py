import wx


class WelcomePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(800, 700),
                          style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        # Properties
        self.font = wx.Font(12, family=wx.FONTFAMILY_DEFAULT, style=0, weight=700, underline=False,
                            faceName="", encoding=wx.FONTENCODING_DEFAULT)

        # Widgets
        self.lbl_welcome = wx.StaticText(self, label='A new way to establish and fortify requirements')
        self.btn_continue = wx.Button(self, label='Continue')
        self.lbl_welcome.SetFont(self.font)
        self.btn_continue.SetFont(self.font)

        # Creating Image
        self.image = wx.Image("/Users/grissell.esquivel/Documents/OpenAiHack/hackathonai/src/utils/logo.png", wx.BITMAP_TYPE_ANY)
        self.image = self.image.Scale(350, 100, wx.IMAGE_QUALITY_HIGH)
        self.bitmap = wx.Bitmap(self.image)
        self.static_bitmap = wx.StaticBitmap(self, wx.ID_ANY, self.bitmap)

        # Sizers
        self.sizer_frame = wx.BoxSizer(wx.VERTICAL)
        self.sizer_frame.Add(self.static_bitmap, flag=wx.CENTER| wx.TOP, border=80)
        self.sizer_frame.Add(self.lbl_welcome, flag=wx.CENTER| wx.TOP, border=15)
        self.sizer_frame.Add(self.btn_continue, flag=wx.CENTER| wx.TOP, border=30)

        self.SetSizer(self.sizer_frame)
        self.SetAutoLayout(1)
        self.Show()
