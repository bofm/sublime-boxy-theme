# -*- coding: utf-8 -*-

"""
Boxy Theme Extras
"""

import sublime
import sublime_plugin
from collections import OrderedDict


NO_SELECTION = -1

SUBLIME_LINTER = 'SublimeLinter'

PLAIN_TASKS = 'PlainTasks'

PLAIN_NOTES = 'PlainNotes'

EXTRAS = OrderedDict(
    [
        (
            'PlainNotes',
            {
                'name': 'Plain Notes',
                'settings': 'Note.sublime-settings',
                'desc': 'Choose a color scheme'
            }
        ),
        (
            'PlainTasks',
            {
                'name': 'Plain Tasks',
                'settings': 'PlainTasks.sublime-settings',
                'desc': 'Choose a color scheme'
            }
        ),
        (
            'SublimeLinter',
            {
                'name': 'Sublime Linter',
                'settings': 'SublimeLinter.sublime-settings',
                'desc': 'Activate a gutter theme',
                'revert': 'Revert the gutter theme to the defaults',
                'boxy': 'Packages/Boxy Theme/extras/SublimeLinter/Boxy.gutter-theme',
                'default': 'Packages/SublimeLinter/gutter-themes/Default/Default.gutter-theme'
            }
        )
    ]
)

THEMES = [
    'Boxy Monokai',
    'Boxy Nova',
    'Boxy Ocean',
    'Boxy Solarized Dark',
    'Boxy Solarized Light',
    'Boxy Tomorrow',
    'Boxy Yesterday'
]


def get_settings(pkg):
    return sublime.load_settings(EXTRAS[pkg].get('settings'))


def save_settings(pkg):
    return sublime.save_settings(EXTRAS[pkg].get('settings'))


def get_theme(pkg):
    settings = get_settings(pkg)

    if pkg is SUBLIME_LINTER:
        items = settings.get('user', '')
        if items != '':
            return items.get('gutter_theme', '')

    if pkg in (PLAIN_TASKS, PLAIN_NOTES):
        return settings.get('color_scheme', '')


def set_theme(pkg, path):
    settings = get_settings(pkg)

    if pkg is SUBLIME_LINTER:
        items = settings.get('user', '')
        if items != '':
            items['gutter_theme'] = path
            return settings.set('user', items)

    if pkg in (PLAIN_TASKS, PLAIN_NOTES):
        return settings.set('color_scheme', path)


def activate_theme(pkg, path):
    set_theme(pkg, path)
    return save_settings(pkg)


def revert_theme(pkg, path):
    if path is '':
        get_settings(pkg).erase('color_scheme')
    else:
        set_theme(pkg, path)

    return save_settings(pkg)


class BoxyExtrasCommand(sublime_plugin.WindowCommand):

    def display_list(self, extras):
        self.extras = extras
        self.quick_list = []

        name = ''
        desc = ''

        for extra in self.extras:
            name = self.extras[extra].get('name')
            desc = self.extras[extra].get('desc')
            if extra is SUBLIME_LINTER:
                if get_theme(SUBLIME_LINTER) == self.extras[
                    SUBLIME_LINTER
                ].get('boxy'):
                    desc = self.extras[SUBLIME_LINTER].get('revert')
            self.quick_list.append([name, desc])

        self.window.show_quick_panel(self.quick_list, self.on_done)

    def on_done(self, index):
        if index is NO_SELECTION:
            return

        if index is 0:
            self.window.run_command('boxy_plain_notes')

        if index is 1:
            self.window.run_command('boxy_plain_tasks')

        if index is 2:
            current = get_theme(SUBLIME_LINTER)
            boxy = self.extras[SUBLIME_LINTER].get('boxy')
            default = self.extras[SUBLIME_LINTER].get('default')

            if current == boxy:
                return revert_theme(SUBLIME_LINTER, default)
            else:
                return activate_theme(SUBLIME_LINTER, boxy)

    def run(self):
        self.display_list(EXTRAS)


class BoxyPlainTasksCommand(sublime_plugin.WindowCommand):

    def display_list(self, themes):
        self.themes = themes
        self.initial_theme = get_theme(PLAIN_TASKS)

        quick_list = [theme for theme in self.themes]
        self.quick_list = quick_list

        self.window.show_quick_panel(quick_list, self.on_done,
                                     on_highlight=self.on_highlighted)

    def on_highlighted(self, index):
        set_theme(PLAIN_TASKS, self._quick_list_to_theme(index))

    def on_done(self, index):
        if index is NO_SELECTION:
            revert_theme(PLAIN_TASKS, self.initial_theme)
            return

        activate_theme(PLAIN_TASKS, self._quick_list_to_theme(index))

    def _quick_list_to_theme(self, index):
        return ('Packages/Boxy Theme/extras/PlainTasks/%s.hidden-tmTheme' %
                self.quick_list[index])

    def run(self):
        self.display_list(THEMES)


class BoxyPlainNotesCommand(sublime_plugin.WindowCommand):

    def display_list(self, themes):
        self.themes = themes
        self.initial_theme = get_theme(PLAIN_NOTES)

        quick_list = [theme for theme in self.themes]
        self.quick_list = quick_list

        self.window.show_quick_panel(quick_list, self.on_done,
                                     on_highlight=self.on_highlighted)

    def on_highlighted(self, index):
        set_theme(PLAIN_NOTES, self._quick_list_to_theme(index))

    def on_done(self, index):
        if index is NO_SELECTION:
            revert_theme(PLAIN_NOTES, self.initial_theme)
            return

        activate_theme(PLAIN_NOTES, self._quick_list_to_theme(index))

    def _quick_list_to_theme(self, index):
        return ('Packages/Boxy Theme/schemes/%s.tmTheme' %
                self.quick_list[index])

    def run(self):
        self.display_list(THEMES)
