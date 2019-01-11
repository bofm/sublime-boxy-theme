## Found an Issue?

If you have some problems, first search for a similar issue, and then report with [new one](https://github.com/ihodev/sublime-boxy/issues) (don't forget to **follow the issue template**). Please read the [**Known Issues**](https://github.com/ihodev/sublime-boxy/wiki#known-issues) section before reporting a new one.

Don't forget to provide your environment details:

[![Environment](https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/wiki/env.gif)](https://raw.githubusercontent.com/ihodev/sublime-boxy-assets/master/assets/wiki/env.gif)

## Git Commit Guidelines

We have very precise rules over how our git commit messages can be formatted. This leads to more readable messages that are easy to follow when looking through the project history. But also, we use the git commit messages to generate the **Boxy** change log. 

We use [**Angular JS commit guidelines**](https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#-git-commit-guidelines) (except the scope notes, we don't need them).

## Building

These themes use a custom Gulp builder. If you want to edit them you must install it first:

```bash
$ npm install
```

then run watcher by:

```bash
$ gulp watch
```

You can now edit the source files under `sources` folder that will be compiled (don't edit compiled files, all sources are inside `sources`).

If you'd like to add some rules and styles to the template of the color schemes, please, do it inside `sources\schemes\scheme.YAML-tmTheme`. Run `gulp build:schemes` and then generate `*.tmTheme` files in `schemes` folder with such tool as [PackageDev](https://github.com/SublimeText/PackageDev).

All colors can be found in `sources\settings` folder.
