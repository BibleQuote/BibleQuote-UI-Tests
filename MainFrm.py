# -*- coding: utf-8 -*-

from pywinauto.application import Application
import pytest
import time

def BQApp():
    '''Runs an aplication instance'''
    return Application().Start(cmd_line=u'C:\Projects\BibleQuote\Source\Output\BibleQuote.exe')

def MainForm(app):
    '''Sets focus on the main window'''
    tmainform = app.TMainForm
    tmainform.Wait('ready')
    return tmainform

app = BQApp()

mainForm = MainForm(app)

def test_change_app_language():
    """File->Print"""
    menu_item = mainForm.MenuItem(u'View->Interface language->#0', app)
    menu_item.Click()

def test_print_function():
    """File->Print"""
    menu_item = mainForm.MenuItem(u'File->#0', app)
    menu_item.Click()
    window = app.Print
    window.Wait('ready')
    button = window.Cancel
    button.Click()

def test_search_bible_text():
    mainForm.Edit.set_edit_text(u'Mk 1:2')
    tbutton2 = mainForm.OK
    tbutton2.Click()

def test_stop_app():
    app.Kill_()