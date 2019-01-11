<p align="center"><img src="https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/3.2.0/name.gif" alt="BOXY"></p>

<p align="center">
  <a href="https://github.com/ihodev/sublime-boxy/releases"><img src="https://img.shields.io/github/release/ihodev/sublime-boxy.svg?maxAge=3600&style=flat-square" alt="Release"></a>
  <a href="https://packagecontrol.io/packages/Boxy%20Theme"><img src="https://img.shields.io/packagecontrol/dt/Boxy%20Theme.svg?maxAge=3600&style=flat-square" alt="Downloads"></a>
  <a href="https://travis-ci.org/ihodev/sublime-boxy"><img src="https://img.shields.io/travis/ihodev/sublime-boxy.svg?maxAge=3600&style=flat-square" alt="Build Status"></a>
  <a href="https://twitter.com/intent/tweet?hashtags=Boxy%2CTheme%2CColorScheme%2CSublimeText&amp;ref_src=twsrc%5Etfw&amp;text=The%20most%20hackable%20theme%20%E2%9D%A4%20Sublime%20Text%203&amp;tw_p=tweetbutton&amp;url=https%3A%2F%2Fpackagecontrol.io%2Fpackages%2FBoxy%2520Theme&amp;via=ihodev" title="Share via Twitter" target="_blank"><img src="https://img.shields.io/badge/share-twitter-1DA1F2.svg?maxAge=2592000&style=flat-square" alt="Twitter"></a>
  <a href="https://www.patreon.com/ihodev" title="Donate with Patreon"><img src="https://img.shields.io/badge/donate-patreon-orange.svg?maxAge=2592000&style=flat-square" alt="Make a donation at patreon.com"></a>
</p>

***

A set of easy customizable interface and syntax themes for **Sublime Text 3 3103+**. Comes in, both, light and dark variations. There are dozens of [**options**][settings] that enable you to personalize your experience with `Boxy Theme`, don't forget to check [them][settings] out.

Want to contribute some code? Excellent! Read up on our [guidelines](https://github.com/ihodev/sublime-boxy/blob/dev/.github/CONTRIBUTING.md).

If you have some problems, first search for a similar issue, and then report with [new one][issues]. Please read the [**Known Issues**][known-issues] section before reporting a new one.

Want to learn more? [**See the wiki &#8594;**][wiki].

***

<div>
<a href="https://github.com/ihodev/sublime-boxy#installation">Installation</a>&nbsp;
▪&nbsp;<a href="https://github.com/ihodev/sublime-boxy#activation">Activation</a>&nbsp;
▪&nbsp;<a href="https://github.com/ihodev/sublime-boxy#icons">Icons</a>&nbsp;
▪&nbsp;<a href="https://github.com/ihodev/sublime-boxy#skins">Skins</a>&nbsp;
▪&nbsp;<a href="https://github.com/ihodev/sublime-boxy/wiki/Settings">Settings</a>&nbsp;
▪&nbsp;<a href="https://github.com/ihodev/sublime-boxy/wiki#references">References</a>&nbsp;
▪&nbsp;<a href="https://forum.sublimetext.com/t/boxy-the-most-hackable-theme-for-sublime-text-3/20564">Forum</a>&nbsp;
▪&nbsp;<a href="https://packagecontrol.io/packages/Boxy%20Theme">Package Control</a>
▪&nbsp;<a href="https://github.com/ihodev/sublime-boxy#share-the-love">Share The Love</a>
</div>

***

<!--
### Getting Started

[![Getting Started with Boxy Theme][img-getting-started]][getting-started]

***
-->

### Installation

The easiest way to install is using [Package Control][pc], where [Boxy][theme] is listed as **`Boxy Theme`**.

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Package Control: Install Package`
3. Find `Boxy Theme` and hit `Enter`
4. Restart Sublime Text
    - **macOS**  : menu item `Sublime Text → Quit Sublime Text`
    - **Windows**: menu item `File → Exit`
    - **Linux**  : menu item `File → Exit`

[**Read more &#8594;**][install]

***

### Activation

Activate the UI theme and color scheme by modifying your user preferences file, which you can find using the menu item `Preferences → Package Settings → Boxy Theme → Preferences`. 

Also you can use commands provided by the theme:

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Boxy Theme: Activation` or `Boxy Theme: Configuration`
3. Hit `Enter`

> **DON'T FORGET TO RESTART SUBLIME TEXT AFTER ACTIVATING THE THEME.**

[**Read more &#8594;**][activation]

***

### Icons

Starting 5.0.0 this theme requires [A File Icon][a-file-icon] package for enhanced support of the file-specific icons. Please install the package and restart Sublime Text.

***

### Skins

You can activate skins by using commands provided by [Skins][skins] package:

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Select Skin` to change the skin
3. Choose `Boxy Theme: Activation` or `Boxy Theme: Configuration` to change the UI theme and color scheme

Or do this manually by modifying your user preferences file, which you can find using the menu item `Preferences → Package Settings → Boxy Theme → Preferences`.

> **DON'T FORGET TO RESTART SUBLIME TEXT AFTER ACTIVATING THE SKIN.**

#### Boxy Monokai ★ Predawn

> **Note**: This skin is heavily inspired by [Predawn Theme][predawn-theme]. Install or support original if it better fits your needs.

[![Boxy Monokai ★ Predawn][img-monokai]][img-monokai]

The screenshot above shows next options in action:

```js
// Activation
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Monokai.tmTheme",
"theme": "Boxy Monokai.sublime-theme",
```

```js
// Settings
"theme_accent_tangerine": true,
"theme_autocomplete_item_selected_colored": true,
"theme_bar_margin_top_sm": true,
"theme_dropdown_atomized": true,
"theme_find_panel_close_hidden": true,
"theme_icon_button_highlighted": true,
"theme_panel_switcher_atomized": true,
"theme_quick_panel_item_selected_colored": true,
"theme_quick_panel_size_md": true,
"theme_scrollbar_colored": true,
"theme_scrollbar_line": true,
"theme_sidebar_close_always_visible": true,
"theme_sidebar_folder_atomized": true,
"theme_statusbar_size_md": true,
"theme_tab_close_always_visible": true,
"theme_tab_selected_overlined": true,
"theme_tab_size_md": true,
```

The operating system is **Windows**. The font used for the code is [**Operator Mono**][operator-mono].

Installed packages:

* [Bracket Highlighter][bracket-highlighter]
* [Sublime Linter][sublime-linter]

#### Boxy Nova ★ Minimal

[![Boxy Nova ★ Minimal][img-nova]][img-nova]

The screenshot above shows next options in action:

```js
// Activation
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Nova.tmTheme",
"theme": "Boxy Nova.sublime-theme",
```

```js
// Settings
"theme_accent_mono": true,
"theme_button_rounded": true,
"theme_find_panel_close_hidden": true,
"theme_find_panel_size_xs": true,
"theme_grid_border_size_sm": true,
"theme_icons_atomized": true,
"theme_minimap_viewport_opacity_xh": true,
"theme_sidebar_folder_arrow": true,
"theme_sidebar_heading_bold": true,
"theme_sidebar_highlight_selected_text_only": true,
"theme_sidebar_highlight_text_only": true,
"theme_sidebar_indent_top_level_disabled": true,
"theme_sidebar_indent_xl": true,
"theme_size_md": true,
"theme_tab_arrows_hidden": true,
"theme_tab_close_always_visible": true,
"theme_unified": true
```

The operating system is **Windows**. The font used for the code is [**Consolas**][consolas]. The UI font is [**Consolas**][consolas] (via [addon][addon-font-face]).

Installed packages:

* [Boxy Theme Addon - Font Face][addon-font-face]
* [Bracket Highlighter][bracket-highlighter]
* [A File Icon][a-file-icon]

#### Boxy Ocean ★ Material

> **Note**: This skin is heavily inspired by [Material Theme][material-theme]. Install or support original if it better fits your needs.

[![Boxy Ocean ★ Material][img-ocean]][img-ocean]

The screenshot above shows next options in action:

```js
// Activation
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Ocean.tmTheme",
"theme": "Boxy Ocean.sublime-theme",
```

```js
// Settings
"theme_accent_cyan": true,
"theme_bar": true,
"theme_bar_logo_atomized": true,
"theme_bar_shadow_hidden": true,
"theme_button_rounded": true,
"theme_dirty_colored_always": true,
"theme_icons_materialized": true,
"theme_scrollbar_rounded": true,
"theme_sidebar_highlight_selected_text_only": true,
"theme_sidebar_highlight_text_only": true,
"theme_sidebar_indent_top_level_disabled": true,
"theme_size_md": true,
"theme_tab_highlight_text_only": true,
"theme_tab_selected_transparent": true,
"theme_tab_selected_underlined": true,
"theme_tab_size_xxl": true,
"theme_unified": true,
```

The operating system is **Ubuntu**. The font used for the code is [**Roboto Mono**][roboto-mono]. The UI font is [**Roboto Medium**][roboto] (via [addon][addon-font-face]).

Installed packages:

* [Boxy Theme Addon - Font Face][addon-font-face]
* [Color Highlighter][color-highlighter]
* [Color ​Helper][color-helper]

#### Boxy Solarized Dark ★ Code

[![Boxy Solarized Dark ★ Code][img-solarized-dark]][img-solarized-dark]

The screenshot above shows next options in action:

```js
// Activation
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Solarized Dark.tmTheme",
"theme": "Boxy Solarized Dark.sublime-theme",
```

```js
// Settings
"theme_accent_purple": true,
"theme_bar": true,
"theme_bar_shadow_hidden": true,
"theme_dropdown_atomized": true,
"theme_find_panel_atomized": true,
"theme_sidebar_disclosure": true,
"theme_sidebar_folder_mono": true,
"theme_sidebar_indent_sm": true,
"theme_statusbar_colored": true,
"theme_statusbar_size_md": true,
"theme_tab_highlight_text_only": true,
"theme_tab_selected_filled": true,
"theme_tab_size_md": true,
"theme_tabset_line_visible": true,
"theme_unified": true,
```

The operating system is **macOS**. The font used for the code is [**SF Mono**][san-francisco]. The UI font is [**SF Mono**][san-francisco] (via [addon][addon-font-face]).

Installed packages:

* [Boxy Theme Addon - Font Face][addon-font-face]
* [Boxy Theme Addon - Mono File Icons][addon-mono-file-icons]
* [Boxy Theme Addon - Widget Font Size][addon-widget-font-size]
* [Bracket Highlighter][bracket-highlighter]

#### Boxy Solarized Light ★ Iowa

[![Boxy Solarized Light ★ Iowa][img-solarized-light]][img-solarized-light]

The screenshot above shows next options in action:

```js
// Activation
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Solarized Light.tmTheme",
"theme": "Boxy Solarized Light.sublime-theme",
```

```js
// Settings
"theme_accent_green": true,
"theme_bar": true,
"theme_bar_colored": true,
"theme_bar_shadow_hidden": true,
"theme_button_rounded": true,
"theme_icons_atomized": true,
"theme_quick_panel_size_md": true,
"theme_scrollbar_rounded": true,
"theme_sidebar_close_always_visible": true,
"theme_sidebar_folder_materialized": true,
"theme_sidebar_highlight_selected_text_only": true,
"theme_sidebar_highlight_text_only": true,
"theme_sidebar_indent_top_level_disabled": true,
"theme_statusbar_size_md": true,
"theme_tab_highlight_text_only": true,
"theme_tab_line_size_lg": true,
"theme_tab_selected_transparent": true,
"theme_tab_selected_underlined": true,
"theme_tab_size_lg": true
```

The operating system is **Windows**. The font used for the code is [**Space Mono**][space-mono].

Installed packages:

* [Bracket Highlighter][bracket-highlighter]
* [Sublime Linter][sublime-linter]

#### Boxy Tomorrow ★ Numix

[![Boxy Tomorrow ★ Numix][img-tomorrow]][img-tomorrow]

The screenshot above shows next options in action:

```js
// Activation
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Tomorrow.tmTheme",
"theme": "Boxy Tomorrow.sublime-theme",
```

```js
// Settings
"theme_accent_numix": true,
"theme_autocomplete_item_selected_colored": true,
"theme_dropdown_atomized": true,
"theme_find_panel_materialized": true,
"theme_grid_border_size_xs": true,
"theme_popup_border_visible": true,
"theme_quick_panel_border_visible": true,
"theme_quick_panel_item_selected_colored": true,
"theme_scrollbar_colored": true,
"theme_scrollbar_line": true,
"theme_sidebar_disclosure": true,
"theme_tab_selected_transparent": true,
"theme_tab_selected_underlined": true,
"theme_tab_size_lg": true,
"theme_unified": true,
```

The operating system is **Ubuntu**. The font used for the code is [**Fira Code**][fira-code]. The UI font is [**Fira Code**][fira-code] (via [addon][addon-font-face])

Installed packages:

* [Boxy Theme Addon - Font Face][addon-font-face]

#### Boxy Yesterday ★ Atom

[![Boxy Yesterday ★ Atom][img-yesterday]][img-yesterday]

The screenshot above shows next options in action:

```js
// Activation
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Yesterday.tmTheme",
"theme": "Boxy Yesterday.sublime-theme",
```

```js
// Settings
"theme_accent_sky": true,
"theme_button_rounded": true,
"theme_find_panel_close_hidden": true,
"theme_find_panel_size_xs": true,
"theme_grid_border_size_lg": true,
"theme_icon_button_highlighted": true,
"theme_icons_atomized": true,
"theme_popup_border_visible": true,
"theme_quick_panel_size_md": true,
"theme_scrollbar_rounded": true,
"theme_sidebar_disclosure": true,
"theme_sidebar_indent_top_level_disabled": true,
"theme_statusbar_size_md": true,
"theme_tab_rounded": true,
"theme_tab_selected_prelined": true,
```

The operating system is **macOS**. The font used for the code is [**Iosevka**][iosevka]. The UI font is [**San Francisco Text**][san-francisco] (via [addon][addon-font-face]).

Installed packages:

* [Boxy Theme Addon - Font Face][addon-font-face]
* [Boxy Theme Addon - Widget Font Size][addon-widget-font-size]
* [PlainNotes][plain-notes]

***

### Share The Love

I've put a lot of time and effort into making `Boxy Theme` awesome. If you love it, you can buy me a coffee. Every cup helps! I promise it will be a good investment 😉

**Donate with:** [Patreon][patreon].

<!-- Links -->

[build-status]: https://travis-ci.org/ihodev/sublime-boxy
[downloads]: https://packagecontrol.io/packages/Boxy%20Theme
[getting-started]: https://youtu.be/d2FZCUDcNxo 'Watch "Getting Started with Boxy Theme" on YouTube'
[issues]: https://github.com/ihodev/sublime-boxy/issues
[known-issues]: https://github.com/ihodev/sublime-boxy/wiki#known-issues
[install]: https://github.com/ihodev/sublime-boxy/wiki/Get-It#installation
[activation]: https://github.com/ihodev/sublime-boxy/wiki/Get-It#activation
[patreon]: https://www.patreon.com/ihodev "Donate with Patreon"
[pc]: https://packagecontrol.io/
[release]: https://github.com/ihodev/sublime-boxy/releases
[settings]: https://github.com/ihodev/sublime-boxy/wiki/Settings
[theme]: https://packagecontrol.io/packages/Boxy%20Theme
[upgrading]: https://github.com/ihodev/sublime-boxy/wiki/Upgrading
[wiki]: https://github.com/ihodev/sublime-boxy/wiki


<!-- Images -->

[img-build-status]: https://img.shields.io/travis/ihodev/sublime-boxy.svg?maxAge=3600&style=flat-square
[img-downloads]: https://img.shields.io/packagecontrol/dt/Boxy%20Theme.svg?maxAge=3600&style=flat-square
[img-getting-started]: https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/3.4.0/getting-started.png
[img-monokai]: https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/3.6.0/skins/monokai.png
[img-name]: https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/name.png
[img-nova]: https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/5.0.0/skins/nova.png
[img-ocean]: https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/3.6.0/skins/ocean.png
[img-patreon]: https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/patreon.png
[img-release]: https://img.shields.io/github/release/ihodev/sublime-boxy.svg?maxAge=3600&style=flat-square
[img-solarized-dark]: https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/3.6.0/skins/solarized-dark.png
[img-solarized-light]: https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/3.6.0/skins/solarized-light.png
[img-tomorrow]: https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/3.6.0/skins/tomorrow.png
[img-yesterday]: https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/readme/3.6.0/skins/yesterday.png

<!-- Fonts -->

[consolas]: https://www.microsoft.com/typography/fonts/family.aspx?FID=300
[fira-code]: https://github.com/tonsky/FiraCode/blob/master/README.md
[iosevka]: https://github.com/be5invis/Iosevka
[operator-mono]: http://www.typography.com/fonts/operator/styles/operatorscreensmartpro
[roboto]: https://fonts.google.com/specimen/Roboto
[roboto-mono]: https://fonts.google.com/specimen/Roboto+Mono?query=Roboto
[san-francisco]: https://developer.apple.com/fonts/
[space-mono]: https://fonts.google.com/specimen/Space+Mono?query=Space+Mono

<!-- Packages -->

[addon-font-face]: https://packagecontrol.io/packages/Boxy%20Theme%20Addon%20-%20Font%20Face
[addon-mono-file-icons]: https://packagecontrol.io/packages/Boxy%20Theme%20Addon%20-%20Mono%20File%20Icons
[addon-widget-font-size]: https://packagecontrol.io/packages/Boxy%20Theme%20Addon%20-%20Widget%20Font%20Size
[bracket-highlighter]: https://packagecontrol.io/packages/BracketHighlighter
[color-helper]: https://packagecontrol.io/packages/ColorHelper
[color-highlighter]: https://packagecontrol.io/packages/Color%20Highlighter
[git-gutter]: https://packagecontrol.io/packages/GitGutter
[a-file-icon]: https://packagecontrol.io/packages/A%20File%20Icon
[plain-notes]: https://packagecontrol.io/packages/PlainNotes
[skins]: https://packagecontrol.io/packages/Skins
[sublime-linter]: https://packagecontrol.io/packages/SublimeLinter
[predawn-theme]: https://packagecontrol.io/packages/Predawn
[material-theme]: https://packagecontrol.io/packages/Material%20Theme
