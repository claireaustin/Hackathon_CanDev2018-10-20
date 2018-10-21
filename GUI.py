#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import wx
import os
import subprocess

wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)
        self.currentDirectory = os.getcwd()
        self.tc2 = ''
        self.path = ''
        self.InitUI()
        self.Centre()


    def InitUI(self):

        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel, label="Automating data fitness")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
            border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('candev.png'))
        sizer.Add(icon, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,
            border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)

        text3 = wx.StaticText(panel, label="            \tDataSet:")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)

        self.tc2 = wx.TextCtrl(panel)
        sizer.Add(self.tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND,
            border=5)

        button1 = wx.Button(panel, label="Browse...")
        button1.Bind(wx.EVT_BUTTON, self.onOpenFile)
        sizer.Add(button1, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)


        sb = wx.StaticBox(panel, label="Optional Modules")

        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer.Add(wx.CheckBox(panel, label="1-a Metadata management"),
            flag=wx.LEFT|wx.TOP, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="1-b Provenance"),
            flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="1-c Multilingualism"),
            flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="1-d Accessibility"),
            flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="2-a Raw data"),
            flag=wx.LEFT, border=5)
        xcb = wx.CheckBox(panel, label="2-b Data format/structure")
        xcb.SetValue(True)
        boxsizer.Add(xcb,
            flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="2-c Data collection"),
            flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="2-d Data preparation"),
            flag=wx.LEFT|wx.BOTTOM, border=5)

        sizer.Add(boxsizer, pos=(5, 0), span=(1, 5),
            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        button3 = wx.Button(panel, label='Help')
        button3.Bind(wx.EVT_BUTTON, self.ShowHelp)
        sizer.Add(button3, pos=(7, 0), flag=wx.LEFT, border=10)

        button4 = wx.Button(panel, label="Apply")
        button4.Bind(wx.EVT_BUTTON, self.OnApply)
        sizer.Add(button4, pos=(7, 3))

        button5 = wx.Button(panel, label="Cancel")
        button5.Bind(wx.EVT_BUTTON, self.OnQuit)

        sizer.Add(button5, pos=(7, 4), span=(1, 1),
            flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)

    def onOpenFile(self, event):
        """
        Create and show the Open FileDialog
        """
        
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory, 
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print("You chose the following file(s):")
            for path in paths:
                print(path)
                self.tc2.SetValue(path)
                self.path = path
        dlg.Destroy()

    def OnApply(self, e):
        s = 'python3 candev.py %s'%(self.path)
        output = subprocess.check_output(s, shell=True)
        print(output)
        if len(output)>200:
            msg = 'Successed!\nFiles save to %s'%(os.getcwd())
        else:
            msg = 'Build Failed'
        self.ShowMsg(msg=msg)
        pass

    def ShowHelp(self, e):
        wx.MessageBox('Powered by Team TM_EC_01   ＞▽＜', '',
            wx.OK | wx.ICON_INFORMATION)

    def ShowMsg(self, msg):
        wx.MessageBox(msg, 'Result',
            wx.OK | wx.ICON_INFORMATION)

    def OnQuit(self, e):
        self.Close()
        

def main():

    app = wx.App()
    ex = Example(None, title="Create Java Class")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()