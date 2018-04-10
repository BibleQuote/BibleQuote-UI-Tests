# -*- coding: utf-8 -*-

from pywinauto.application import Application
import time

app = Application().Start(cmd_line=u'C:\Projects\BibleQuote\Source\Output\BibleQuote.exe')
tmainform = app.TMainForm
tmainform.Wait('ready')

time.sleep(3)

tedit = tmainform[u'5']
tedit.ClickInput()

tmainform.Edit.set_edit_text(u'Mk 1:2')

tbutton2 = tmainform.OK
tbutton2.Click()

time.sleep(3)

"""File->Print"""
menu_item = tmainform.MenuItem(u'File->#0', app)
menu_item.Click()

window = app.Print
window.Wait('ready')
button = window.Cancel
button.Click()

time.sleep(3)

app.Kill_()