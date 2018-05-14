# -*- coding: utf-8 -*-

from pywinauto.application import Application
import pytest
import time

class TestBibleQuoteApp:
    
    def setup_class(self):
        '''Run an aplication instance'''
        app = Application()
        self.app = app.start('D:\\Projects\\BibleQuote\\Output\\BibleQuote.exe')
        self.dlg = self.app.TMainForm
        menu_item = self.dlg.MenuItem(u'#1->#2->#1')
        menu_item.click()

    def teardown_class(self):
        '''Close the application after tests'''
        self.app.kill_()

    ''' ========== Test dialog windows ========== '''

    def test_print_function(self):
        '''File->Print'''
        menu_item = self.dlg.MenuItem(u'File->#0', self.app)
        menu_item.click()
        window = self.app.PrintDialog
        window.wait('visible')
        assert self.dlg.IsEnabled() == False
        assert window.Texts()[0] == u'Print'
        assert window.Printer.Texts()[0] == u'Printer'
        window.Cancel.click()

    def test_about_popup_window(self):
        '''Help->About this programm'''
        menu_item = self.dlg.MenuItem(u'Help->#3', self.app)
        menu_item.click()
        window = self.app.About
        window.wait('visible')
        assert self.dlg.IsEnabled() == False
        assert window.Texts()[0] == u'About'
        assert '6.0.20120312 (12.03.2012) BETA' in window.Edit.Texts()[0]
        window.OK.click()

    def test_settings(self):
        '''File->Options'''
        menu_item = self.dlg.MenuItem(u'File->#5', self.app)
        menu_item.click()
        window = self.app.Parameters
        window.wait('visible')
        time.sleep(3)
        window.OK.click()

    ''' ========== Test main window ========== '''

    def test_search_bible_text(self):
        self.dlg.Edit.set_edit_text(u'Mk 1:2')
        tbutton2 = self.dlg.OK
        tbutton2.click()

    def test_change_view(self):
        '''Togle left Panel'''
        assert self.dlg.TPageControl.IsEnabled() == True
        assert self.dlg.TPageControl.IsVisible() == True
        self.dlg.TToolBar2.click()
        time.sleep(3)
        assert self.dlg.TPageControl.IsEnabled() == True
        assert self.dlg.TPageControl.IsVisible() == True
        self.dlg.TToolBar2.click()
