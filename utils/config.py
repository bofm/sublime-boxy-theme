# -*- coding: utf-8 -*-

"""
Boxy Theme Configuration
"""

import sublime
import sublime_plugin
import mdpopups
import os
from collections import OrderedDict


SUB_SECTIONS = OrderedDict(
    [
        (
            'Global',
            [
                'Accent',
                'Background',
                'Font',
                'Icons',
                'Size'
            ]
        ),
        (
            'Bar',
            [
                'Bar Flavors',
                'Bar Margin'
            ]
        ),
        (
            'Tabs',
            [
                'Tab Flavors',
                'Tab Font',
                'Tab Misc',
                'Tab Size'
            ]
        ),
        (
            'Find Panels',
            [
                'Find Panel Font',
                'Find Panel Misc',
                'Find Panel Padding',
                'Find Panel Size'
            ]
        ),
        (
            'Quick Panels',
            [
                'Quick Panel Misc',
                'Quick Panel Size'
            ]
        ),
        (
            'Sidebar',
            [
                'Sidebar Font',
                'Sidebar Icons',
                'Sidebar Indent',
                'Sidebar Misc',
                'Sidebar Size'
            ]
        ),
        (
            'Status Bar',
            [
                'Status Bar Flavors',
                'Status Bar Font',
                'Status Bar Size'
            ]
        )
    ]
)

SUB_SECTION_OPTIONS = OrderedDict(
    [
        (
            'Size',
            [
                'theme_size_xs',
                'theme_size_sm',
                'theme_size_md',
                'theme_size_lg',
                'theme_size_xl'
            ]
        ),
        (
            'Font',
            [
                'theme_font_xs',
                'theme_font_sm',
                'theme_font_md',
                'theme_font_lg',
                'theme_font_xl'
            ]
        ),
        (
            'Accent',
            [
                'theme_accent_blue',
                'theme_accent_cyan',
                'theme_accent_green',
                'theme_accent_lime',
                'theme_accent_mono',
                'theme_accent_numix',
                'theme_accent_orange',
                'theme_accent_pink',
                'theme_accent_purple',
                'theme_accent_sky',
                'theme_accent_tangerine'
            ]
        ),
        (
            'Icons',
            [
                'theme_icons_atomized',
                'theme_icons_flat',
                'theme_icons_materialized'
            ]
        ),
        (
            'Background',
            [
                'theme_unified'
            ]
        ),
        (
            'Bar Flavors',
            [
                'theme_bar',
                'theme_bar_colored',
                'theme_bar_logo_atomized',
                'theme_bar_logo_materialized',
                'theme_bar_shadow_hidden'
            ]
        ),
        (
            'Bar Margin',
            [
                'theme_bar_margin_top_sm',
                'theme_bar_margin_top_md',
                'theme_bar_margin_top_lg'
            ]
        ),
        (
            'Tab Size',
            [
                'theme_tab_size_xs',
                'theme_tab_size_sm',
                'theme_tab_size_md',
                'theme_tab_size_lg',
                'theme_tab_size_xl',
                'theme_tab_size_xxl',
                'theme_tab_width_auto'
            ]
        ),
        (
            'Tab Font',
            [
                'theme_tab_font_xs',
                'theme_tab_font_sm',
                'theme_tab_font_md',
                'theme_tab_font_lg',
                'theme_tab_font_xl',
                'theme_tab_label_bold',
                'theme_tab_selected_label_bold'
            ]
        ),
        (
            'Tab Flavors',
            [
                'theme_tab_line_size_lg',
                'theme_tab_line_size_sm',
                'theme_tab_rounded',
                'theme_tab_selected_filled',
                "theme_tab_selected_overlined",
                'theme_tab_selected_prelined',
                'theme_tab_selected_transparent',
                'theme_tab_selected_underlined'
            ]
        ),
        (
            'Tab Misc',
            [
                'theme_dirty_accent_blue',
                'theme_dirty_accent_cyan',
                'theme_dirty_accent_green',
                'theme_dirty_accent_lime',
                'theme_dirty_accent_numix',
                'theme_dirty_accent_orange',
                'theme_dirty_accent_pink',
                'theme_dirty_accent_purple',
                'theme_dirty_accent_sky',
                'theme_dirty_accent_tangerine',
                'theme_dirty_colored_always',
                'theme_dirty_materialized',
                'theme_dropdown_atomized',
                'theme_dropdown_materialized',
                'theme_tab_arrows_hidden',
                'theme_tab_close_always_visible',
                'theme_tab_highlight_text_only',
                'theme_tab_mouse_wheel_switch',
                'theme_tab_separator',
                'theme_tabset_line_visible'
            ]
        ),
        (
            'Find Panel Size',
            [
                'theme_find_panel_size_xxs',
                'theme_find_panel_size_xs',
                'theme_find_panel_size_sm',
                'theme_find_panel_size_md',
                'theme_find_panel_size_lg',
                'theme_find_panel_size_xl'
            ]
        ),
        (
            'Find Panel Font',
            [
                'theme_find_panel_font_xs',
                'theme_find_panel_font_sm',
                'theme_find_panel_font_md',
                'theme_find_panel_font_lg',
                'theme_find_panel_font_xl'
            ]
        ),
        (
            'Find Panel Padding',
            [
                'theme_find_panel_padding_xs',
                'theme_find_panel_padding_sm',
                'theme_find_panel_padding_md',
                'theme_find_panel_padding_lg',
                'theme_find_panel_padding_xl'
            ]
        ),
        (
            'Find Panel Misc',
            [
                'theme_button_rounded',
                'theme_find_panel_atomized',
                'theme_find_panel_close_hidden',
                'theme_find_panel_materialized',
                'theme_icon_button_highlighted'
            ]
        ),
        (
            'Quick Panel Size',
            [
                'theme_quick_panel_size_xs',
                'theme_quick_panel_size_sm',
                'theme_quick_panel_size_md',
                'theme_quick_panel_size_lg',
                'theme_quick_panel_size_xl'
            ]
        ),
        (
            'Quick Panel Misc',
            [
                'theme_quick_panel_border_visible',
                'theme_quick_panel_item_selected_colored'
            ]
        ),
        (
            'Sidebar Size',
            [
                'theme_sidebar_size_xxs',
                'theme_sidebar_size_xs',
                'theme_sidebar_size_sm',
                'theme_sidebar_size_md',
                'theme_sidebar_size_lg',
                'theme_sidebar_size_xl'
            ]
        ),
        (
            'Sidebar Font',
            [
                'theme_sidebar_font_xs',
                'theme_sidebar_font_sm',
                'theme_sidebar_font_md',
                'theme_sidebar_font_lg',
                'theme_sidebar_font_xl'
            ]
        ),
        (
            'Sidebar Indent',
            [
                'theme_sidebar_indent_xs',
                'theme_sidebar_indent_sm',
                'theme_sidebar_indent_md',
                'theme_sidebar_indent_lg',
                'theme_sidebar_indent_xl'
            ]
        ),
        (
            'Sidebar Icons',
            [
                'theme_sidebar_close_always_visible',
                'theme_sidebar_disclosure',
                'theme_sidebar_file_icons_hidden',
                'theme_sidebar_folder_arrow',
                'theme_sidebar_folder_atomized',
                'theme_sidebar_folder_materialized',
                'theme_sidebar_folder_mono',
                'theme_sidebar_icon_saturation_hg',
                'theme_sidebar_icon_saturation_lw',
                'theme_sidebar_icon_saturation_md',
                'theme_sidebar_icon_saturation_xh'
            ]
        ),
        (
            'Sidebar Misc',
            [
                'theme_sidebar_border',
                'theme_sidebar_heading_bold',
                'theme_sidebar_highlight_selected_text_only',
                'theme_sidebar_highlight_text_only',
                'theme_sidebar_indent_top_level_disabled'
            ]
        ),
        (
            'Status Bar Size',
            [
                'theme_statusbar_size_xs',
                'theme_statusbar_size_sm',
                'theme_statusbar_size_md',
                'theme_statusbar_size_lg',
                'theme_statusbar_size_xl'
            ]
        ),
        (
            'Status Bar Font',
            [
                'theme_statusbar_font_xs',
                'theme_statusbar_font_sm',
                'theme_statusbar_font_md',
                'theme_statusbar_font_lg',
                'theme_statusbar_font_xl',
                'theme_statusbar_label_bold'
            ]
        ),
        (
            'Status Bar Flavors',
            [
                'theme_panel_switcher_atomized',
                'theme_panel_switcher_materialized',
                'theme_statusbar_colored'
            ]
        )
    ]
)

SECTION_OPTIONS = OrderedDict(
    [
        (
            'Scrollbars',
            [
                'theme_scrollbar_colored',
                'theme_scrollbar_line',
                'theme_scrollbar_rounded',
                'theme_scrollbar_semi_overlayed'
            ]
        ),
        (
            'Tooltips',
            [
                'theme_tooltips_font_xs',
                'theme_tooltips_font_sm',
                'theme_tooltips_font_md',
                'theme_tooltips_font_lg',
                'theme_tooltips_font_xl'
            ]
        ),
        (
            'Grid',
            [
                'theme_grid_border_size_xs',
                'theme_grid_border_size_sm',
                'theme_grid_border_size_md',
                'theme_grid_border_size_lg',
                'theme_grid_border_size_xl'
            ]
        ),
        (
            'Popups',
            [
                'theme_autocomplete_item_selected_colored',
                'theme_popup_border_visible'
            ]
        ),
        (
            'Minimap',
            [
                'theme_minimap_viewport_opacity_xlw',
                'theme_minimap_viewport_opacity_lw',
                'theme_minimap_viewport_opacity_md',
                'theme_minimap_viewport_opacity_hg',
                'theme_minimap_viewport_opacity_xh',
                'theme_minimap_viewport_opacity_xxh'
            ]
        )
    ]
)

BACK = '[&larr; Back](back-Home){: .boxy-control .boxy-control-back }'

BACK_TO_SUBMENU = ''

SECTIONS = '- [%(section)s](::%(section)s){: .boxy-control }\n'

SECTION_LABEL = '''\n\n# BOXY CONFIG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n\n***\n\n\
## %s\n\n'''

SECTIONS_LABEL = '''\n\n# BOXY CONFIG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n\n***\n\n\
## Main Sections\n\n'''

GENERAL_SETTING = '''- [**%(status)s**{: %(class)s} %(name)s](%(name)s:%\
(set)s:%(section)s){: .boxy-control }\n'''

SCHEME = '''- [**%(status)s**{: %(class)s} %(name)s](color_scheme:%(set)s:%\
(section)s){: .boxy-control }\n'''

THEME_LABEL = '''\n\n# BOXY CONFIG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n\n***\n\n\
## UI Theme\n\n'''

SCHEME_LABEL = '''\n\n# BOXY CONFIG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n\n***\n\n\
## Color Scheme\n\n'''

OTHER_SCHEME = '''- [**%(status)s**{: .boxy-control %(class)s} Other: %(name)s]\
(color_scheme:%(set)s:%(section)s){: .boxy-control }\n'''

THEME = '''- [**%(status)s**{: .boxy-control %(class)s} %(name)s](theme:%(set)s\
:%(section)s){: .boxy-control }\n'''

OTHER_THEME = '''- [**%(status)s**{: .boxy-control %(class)s} Other: %(name)s]\
(theme:%(set)s:%(section)s){: .boxy-control }\n'''

MARKED = '✓'

UNMARKED = '✗'

RADIO_MARKED = '☒'

RADIO_UNMARKED = '☐'

STYLES = '''\
html,
body {
    padding: 0;
}
{% if var.sublime_version < 3119 %}
body {
    padding: 8px;
    {% if var.is_light %}
    {{'.background'|css|brightness(0.98)}}
    padding: 16px;
    {% endif %}
    padding-bottom: 4px;
}
h1,
h2 {
    margin: 0 0 0.5em;
}
h1 {
    font-size: 1.1em;
}
h2 {
    font-size: 1em;
}
hr {
    margin: 0.5em 0;
}
ul,
li {
    margin: 0;
    padding: 0;
    display: block;
}
a {
    display: block;
    padding: 0.125em 0;
}
.boxy-control {
    font-size: 1em;
    text-decoration: none;
}
.boxy-control-back {
    {{'.foreground'|css('color')}}
}
.boxy-control-back {
    display: inline;
}
{% else %}
div.boxy-config {
    padding: 0.8rem;
    padding-bottom: 0.4rem;
}
.boxy-config h1,
.boxy-config h2 {
    margin: 0 0 0.5rem;
}
.boxy-config h1 {
    font-size: 1.1rem;
}
.boxy-config h2 {
    font-size: 1rem;
}
.boxy-config hr {
    margin: 0.5rem 0;
}
.boxy-config ul,
.boxy-config li {
    margin: 0;
    padding: 0;
    display: block;
}
.boxy-config a {
    display: block;
    padding: 0.125rem 0;
}
.boxy-config .boxy-control {
    font-size: 1rem;
    text-decoration: none;
}
.boxy-config .boxy-control-back {
    {{'.foreground'|css('color')}}
}
.boxy-config .boxy-control-back {
    display: inline;
}
{% endif %}
'''


def is_boxy_res(item):
    return item.startswith('Packages/Boxy Theme/')


class BoxyConfigCommand(sublime_plugin.TextCommand):

    def on_navigate(self, href):
        if href.startswith('back'):
            self.show_popup(href[5:])
        else:
            settings = sublime.load_settings('Preferences.sublime-settings')
            name, value, section = href.split(':')
            if name:
                if name not in ('theme', 'color_scheme'):
                    boolean = True if value == 'True' else False
                    if boolean:
                        settings.set(name, boolean)
                    else:
                        settings.erase(name)
                else:
                    settings.set(name, value)
                sublime.save_settings('Preferences.sublime-settings')

            self.show_popup(section)

    def show_popup(self, menu):
        global BACK
        global BACK_TO_SUBMENU

        settings = sublime.load_settings('Preferences.sublime-settings')
        popup = []

        marked = settings.get('theme_config_marked', False)
        unmarked = settings.get('theme_config_unmarked', False)
        radio_marked = settings.get('theme_config_radio_marked', False)
        radio_unmarked = settings.get('theme_config_radio_unmarked', False)

        if marked is False:
            marked = MARKED

        if unmarked is False:
            unmarked = UNMARKED

        if radio_marked is False:
            radio_marked = RADIO_MARKED

        if radio_unmarked is False:
            radio_unmarked = RADIO_UNMARKED

        if menu == 'Home':
            popup.append(SECTIONS_LABEL)
            for k in (['UI Theme', 'Color Scheme'] +
                      list(SUB_SECTIONS.keys()) +
                      list(SECTION_OPTIONS.keys())):
                popup.append(SECTIONS % {'section': k})
        elif menu == 'UI Theme':
            theme = settings.get('theme', '')
            boxy_themes = [
                os.path.basename(bt) for bt in sorted(
                    sublime.find_resources('Boxy*.sublime-theme')
                ) if is_boxy_res(bt)
            ]
            popup.append(THEME_LABEL)
            for option in boxy_themes:
                option_value = theme == option
                popup.append(
                    THEME % {
                        'name': option,
                        'status': radio_marked if option_value else radio_unmarked,
                        'set': option,
                        'class': '.success' if option_value else '.error',
                        'section': 'UI Theme'
                    }
                )
            if theme is not None and theme not in boxy_themes:
                popup.append(
                    OTHER_THEME % {
                        'name': theme,
                        'status': radio_marked,
                        'set': option,
                        'class': '.success' if option_value else '.error',
                        'section': 'UI Theme'
                    }
                )
        elif menu == 'Color Scheme':
            scheme = settings.get('color_scheme', '')
            boxy_schemes = [
                bs for bs in sorted(
                    sublime.find_resources('Boxy*.tmTheme')
                ) if is_boxy_res(bs)
            ]
            popup.append(SCHEME_LABEL)
            for option in boxy_schemes:
                option_value = scheme == option
                popup.append(
                    SCHEME % {
                        'name': option,
                        'status': radio_marked if option_value else radio_unmarked,
                        'set': option,
                        'class': '.success' if option_value else '.error',
                        'section': 'Color Scheme'
                    }
                )
            if scheme is not None and scheme not in boxy_schemes:
                popup.append(
                    OTHER_SCHEME % {
                        'name': scheme,
                        'status': radio_marked,
                        'set': option,
                        'class': '.success',
                        'section': 'Color Scheme'
                    }
                )
        elif menu in SUB_SECTIONS.keys():
            popup.append(SECTION_LABEL % menu)
            for k in SUB_SECTIONS[menu]:
                popup.append(SECTIONS % {'section': k})
            BACK = '[← Back](back-Home){: .boxy-control .boxy-control-back }'
            BACK_TO_SUBMENU = '''[← Back](back-%s){: .boxy-control\
             .boxy-control-back }''' % (menu)
        elif menu in SECTION_OPTIONS.keys():
            popup.append(SECTION_LABEL % menu)
            for option in SECTION_OPTIONS[menu]:
                option_value = bool(settings.get(option, False))
                popup.append(
                    GENERAL_SETTING % {
                        'name': option,
                        'status': marked if option_value else unmarked,
                        'set': str(not option_value),
                        'class': '.success' if option_value else '.error',
                        'section': menu
                    }
                )
            BACK = '[← Back](back-Home){: .boxy-control .boxy-control-back }'
        else:
            popup.append(SECTION_LABEL % menu)
            for option in SUB_SECTION_OPTIONS[menu]:
                option_value = bool(settings.get(option, False))
                popup.append(
                    GENERAL_SETTING % {
                        'name': option,
                        'status': marked if option_value else unmarked,
                        'set': str(not option_value),
                        'class': '.success' if option_value else '.error',
                        'section': menu
                    }
                )
            BACK = BACK_TO_SUBMENU

        if menu != 'Home':
            popup.append(BACK)

        mdpopups.hide_popup(self.view)
        mdpopups.show_popup(
            self.view,
            ''.join(popup),
            css=STYLES,
            wrapper_class='boxy-config',
            on_navigate=self.on_navigate,
            max_width=1024,
            max_height=1024
        )

    def run(self, edit):
        self.show_popup('Home')
