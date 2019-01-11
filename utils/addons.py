# -*- coding: utf-8 -*-

"""
Boxy Theme Add-ons
"""

import sublime
import os
import zipfile
import shutil


PREFERENCES = 'Preferences.sublime-settings'

PARENT = 'Boxy Theme'

UNIFIED_SETTINGS = {
    'source': 'addons/UnifiedMode',
    'target': 'Boxy Theme Addon - Unified Mode',
    'package': 'Boxy Theme.sublime-package'
}

ID = '48c3cc08-b280-4048-a9bd-a948a83319df'


def get_settings():
    return sublime.load_settings(PREFERENCES)


def copy_dir(source_dir, target_dir):
    if os.path.exists(source_dir):
        files = os.listdir(source_dir)
        for f in files:
            name = os.path.basename(f)
            pre, ext = os.path.splitext(name)

            if ext == '.addon-settings':
                name = pre + '.sublime-settings'

            if ext == '.addon-theme':
                name = pre + '.stTheme'

            source = os.path.join(source_dir, f)
            target = os.path.join(target_dir, name)
            shutil.copy(source, target)


def extract_dir(path_to_zip, source_dir, extract_dir=None):
    if extract_dir is None:
        return

    if os.path.exists(path_to_zip):
        with zipfile.ZipFile(path_to_zip) as z:
            for f in z.namelist():
                if f.startswith(source_dir):
                    name = os.path.basename(f)

                    if not name:
                        continue

                    pre, ext = os.path.splitext(name)

                    if ext == '.addon-settings':
                        name = pre + '.sublime-settings'

                    if ext == '.addon-theme':
                        name = pre + '.stTheme'

                    source = z.open(f)
                    target = open(os.path.join(extract_dir, name), 'wb')
                    with source, target:
                        shutil.copyfileobj(source, target)
            z.close()


def unified_mode():
    source = UNIFIED_SETTINGS['source']
    target = os.path.join(sublime.packages_path(), UNIFIED_SETTINGS['target'])
    package = os.path.join(sublime.installed_packages_path(),
                           UNIFIED_SETTINGS['package'])
    is_unified = get_settings().get('theme_unified', False)
    main = os.path.join(sublime.packages_path(), PARENT, source)

    if is_unified:
        if not os.path.exists(target):
            os.mkdir(target)

            if os.path.exists(main):
                copy_dir(main, target)
            else:
                extract_dir(package, source, target)

    elif os.path.exists(target):
        shutil.rmtree(target)


def plugin_loaded():
    unified_mode()
    get_settings().add_on_change(ID, unified_mode)


def plugin_unloaded():
    target = os.path.join(sublime.packages_path(), UNIFIED_SETTINGS['target'])

    if os.path.exists(target):
        shutil.rmtree(target)
