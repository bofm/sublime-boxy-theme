# -*- coding: utf-8 -*-

"""
Boxy Theme Environment
"""

import sublime
import sublime_plugin
import textwrap


__version__ = '5.2.0'
__pc_name__ = 'Boxy Theme'


def list2string(obj):
    return '.'.join([str(x) for x in obj])


def format_version(module, attr, call=False):
    try:
        if call:
            version = getattr(module, attr)()
        else:
            version = getattr(module, attr)
    except Exception as e:
        print(e)
        version = 'Version could not be acquired!'

    if not isinstance(version, str):
        version = list2string(version)
    return version


def is_installed_by_package_control():
    settings = sublime.load_settings('Package Control.sublime-settings')
    return str(__pc_name__ in set(settings.get('installed_packages', [])))


class BoxyEnvironmentCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        info = {}

        info['platform'] = sublime.platform()
        info['version'] = sublime.version()
        info['arch'] = sublime.arch()
        info['boxy_version'] = __version__
        info['pc_install'] = is_installed_by_package_control()

        try:
            import mdpopups
            info['mdpopups_version'] = format_version(mdpopups, 'version',
                                                      call=True)
        except Exception:
            info['mdpopups_version'] = 'Version could not be acquired!'

        try:
            import markdown
            info['markdown_version'] = format_version(markdown, 'version')
        except Exception:
            info['markdown_version'] = 'Version could not be acquired!'

        try:
            import jinja2
            info['jinja_version'] = format_version(jinja2, '__version__')
        except Exception:
            info['jinja_version'] = 'Version could not be acquired!'

        try:
            import pygments
            info['pygments_version'] = format_version(pygments, '__version__')
        except Exception:
            info['pygments_version'] = 'Version could not be acquired!'

        msg = textwrap.dedent(
            '''\
            - Boxy Theme: %(boxy_version)s
            - Sublime Text: %(version)s
            - Platform: %(platform)s
            - Package Control: %(pc_install)s
            - Dependencies:
                * mdpopups: %(mdpopups_version)s
                * markdown: %(markdown_version)s
                * pygments: %(pygments_version)s
                * jinja2: %(jinja_version)s
            ''' % info
        )

        view = sublime.active_window().active_view()
        def copy_and_hide(msg):
            sublime.set_clipboard(msg)
            view.hide_popup()
        view.show_popup(msg.replace('\n', '<br>') +
                        '<br><a href="' + msg + '">Copy</a>',
                        on_navigate=copy_and_hide)
