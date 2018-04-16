# -*- coding: utf-8 -*-

from pywinauto.application import Application
import pytest
import time

def BQApp():
    '''Run an aplication instance'''
    return Application().Start(cmd_line=u'D:\\Projects\\BibleQuote\\Output\\BibleQuote.exe')

def MainForm(app):
    '''Set focus on the main window'''
    tmainform = app.TMainForm
    tmainform.Wait('ready')
    return tmainform

def change_app_language():
    '''Change app language to English
    File->Interface language->English'''
    menu_item = tmainform.MenuItem(u'#1->#2->#1', app)
    menu_item.Click()

''' ========== Run app ========== '''

app = BQApp()
tmainform = MainForm(app)
change_app_language()


''' ========== Test dialog windows ========== '''

def test_print_function():
    '''File->Print'''
    menu_item = tmainform.MenuItem(u'File->#0')
    menu_item.Click()
    window = app.PrintDialog
    window.Wait('ready')
    assert tmainform.IsEnabled() == False
    assert window.Texts()[0] == u'Print'
    assert window.Printer.Texts()[0] == u'Printer'
    window.Cancel.Click()

def test_about_popup_window():
    '''Help->About this programm'''
    menu_item = tmainform.MenuItem(u'Help->#3')
    menu_item.Click()
    window = app.About
    window.Wait('ready')
    assert tmainform.IsEnabled() == False
    assert window.Texts()[0] == u'About'
    assert '6.0.20120312 (12.03.2012) BETA' in window.Edit.Texts()[0]
    window.OK.Click()


''' ========== Test main window ========== '''

def test_search_bible_text():
    tmainform.Edit.set_edit_text(u'Mk 1:2')
    tbutton2 = tmainform.OK
    tbutton2.Click()

def test_change_view():
    '''Togle left Panel'''
    assert tmainform.TPageControl.IsEnabled() == True
    assert tmainform.TPageControl.IsVisible() == True
    tmainform[u'3'].Click()
    time.sleep(3)
    assert tmainform.TPageControl.IsEnabled() == True
    assert tmainform.TPageControl.IsVisible() == True
    tmainform[u'3'].Click()


''' ========== Close app window ========== '''

def test_stop_app():
    app.Kill_()
