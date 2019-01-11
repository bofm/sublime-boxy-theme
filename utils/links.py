# -*- coding: utf-8 -*-

"""
Boxy Theme Links
"""

import sublime
import sublime_plugin
import webbrowser


class BoxyDonateCommand(sublime_plugin.WindowCommand):
    def run(self):
        webbrowser.open_new_tab('https://github.com/ihodev/sublime-boxy#share-the-love')


class BoxyForumCommand(sublime_plugin.WindowCommand):
    def run(self):
        webbrowser.open_new_tab('https://forum.sublimetext.com/t/boxy-the-most-hackable-theme-for-sublime-text-3')


class BoxyIssuesCommand(sublime_plugin.WindowCommand):
    def run(self):
        webbrowser.open_new_tab('https://github.com/ihodev/sublime-boxy/issues')


class BoxyPackageControlCommand(sublime_plugin.WindowCommand):
    def run(self):
        webbrowser.open_new_tab('https://packagecontrol.io/packages/Boxy%20Theme')


class BoxyRepoCommand(sublime_plugin.WindowCommand):
    def run(self):
        webbrowser.open_new_tab('https://github.com/ihodev/sublime-boxy')


class BoxyWikiCommand(sublime_plugin.WindowCommand):
    def run(self):
        webbrowser.open_new_tab('https://github.com/ihodev/sublime-boxy/wiki')
