/* Sublime Text 3 Theme Builder
 * -------------------------------------------------------------------------- *
 * Developed with love & patience by Ihor Oleksandrov
 * -------------------------------------------------------------------------- */

'use strict';

/*
 * > Plugins
 */

var gulp = require('gulp');
var del = require('del');
var path = require('path');
var colors = require('colors');
var runSequence = require('run-sequence');
var conventionalChangelog = require('conventional-changelog');
var conventionalGithubReleaser = require('conventional-github-releaser');
var argv = require('yargs').argv;
var fs = require('fs');
var _ = require('lodash');
var $ = require('gulp-load-plugins')();

/*
 * > Settings
 */

var common = require('./sources/settings/common.json');
var envRegExp = new RegExp('([\'|\"]?__version__[\'|\"]?[ ]*[:|=][ ]*[\'|\"]?)(\\d+\\.\\d+\\.\\d+)(-[0-9A-Za-z\.-]+)?([\'|\"]?)', 'i');

/*
 * > Clean
 */

gulp.task('clean:themes', function() {
  return del(['./*.sublime-theme']);
});

gulp.task('clean:schemes', function() {
  return del(['./schemes/*.tmTheme', './schemes/*.YAML-tmTheme']);
});

gulp.task('clean:widgets', function() {
  return del(['./widgets/*.stTheme', './widgets/*.sublime-settings']);
});

gulp.task('clean:extras', function() {
  return del(['./extras/**/*.hidden-tmTheme', './extras/**/*.YAML-tmTheme']);
});

gulp.task('clean:addons', function() {
  return del(['./addons/**/*.addon-theme', './addons/**/*.addon-settings']);
});

/*
 * > Build
 */

gulp.task('build', function(cb) {
  runSequence(
    'build:themes',
    'build:schemes',
    'build:widgets',
    'build:extras',
    'build:addons',
    function (error) {
      if (error) {
        console.log('[build]'.bold.magenta + ' There was an issue building BOXY:\n'.bold.red + error.message);
      } else {
        console.log('[build]'.bold.magenta + ' Finished successfully'.bold.green);
      }

      cb(error);
    }
  );
});

/* >> Themes */

gulp.task('build:themes', ['clean:themes'], function() {
  return gulp.src('./sources/themes/*.json')
    .pipe($.plumber(function(error) {
      console.log('[build:themes]'.bold.magenta + ' There was an issue building themes:\n'.bold.red + error.message);
      this.emit('end');
    }))
    .pipe($.include())
    .pipe($.data(function(file) {
      var specific = require('./sources/settings/specific/' +
          path.basename(file.path));

      return _.merge(common, specific);
    }))
    .pipe($.template())
    .pipe($.rename(function(path) {
      path.basename = 'Boxy ' + _.startCase(path.basename);
      path.extname = '.sublime-theme';
    }))
    .pipe(gulp.dest('./'))
    .on('end', function() {
      console.log('[build:themes]'.bold.magenta + ' Finished successfully'.bold.green);
    });
});

/* >> Schemes */

gulp.task('build:schemes', ['clean:schemes'], function(cb) {
  runSequence(
    'process:schemes',
    'convert:schemes',
    function (error) {
      if (error) {
        console.log('[build:schemes]'.bold.magenta + ' There was an issue building schemes:\n'.bold.red + error.message);
      } else {
        console.log('[build:schemes]'.bold.magenta + ' Finished successfully'.bold.green);
      }

      cb(error);
    }
  );
});

gulp.task('process:schemes', function() {
  return gulp.src('./sources/settings/specific/*.json')
    .pipe($.flatmap(function(stream, file) {
      var basename = 'Boxy ' + _.startCase(path.basename(file.path, path.extname(file.path)));

      return gulp.src('./sources/schemes/scheme.YAML-tmTheme')
        .pipe($.data(function() {
          var specific = require(file.path);

          return _.merge(common, specific);
        }))
        .pipe($.template())
        .pipe($.rename(function(scheme) {
          scheme.basename = basename;
        }))
        .pipe(gulp.dest('./schemes'));
    }));
});

gulp.task('convert:schemes', function() {
  return gulp.src('./schemes/*.YAML-tmTheme')
    .pipe($.flatmap(function(stream) {
      return stream
        .pipe($.plumber(function(error) {
          console.log('[convert:schemes]'.bold.magenta + ' There was an issue converting color schemes:\n'.bold.red + error.message +
                      'To fix this error:\nAdd Sublime Text to the `PATH` and then install "PackageDev" via "Package Control".\nOpen Sublime Text before running the task.'.bold.blue);
          this.emit('end');
        }))
        .pipe($.exec('subl "<%= file.path %>" && subl --command "convert_file"'))
        .pipe($.exec.reporter());
    }));
});

/* >> Widgets */

gulp.task('build:widgets', ['clean:widgets'], function(cb) {
  runSequence(
    'build:widget-themes',
    'build:widget-settings',
    function (error) {
      if (error) {
        console.log('[build:widgets]'.bold.magenta + ' There was an issue building widgets:\n'.bold.red + error.message);
      } else {
        console.log('[build:widgets]'.bold.magenta + ' Finished successfully'.bold.green);
      }

      cb(error);
    }
  );
});

gulp.task('build:widget-themes', function() {
  return gulp.src('./sources/settings/specific/*.json')
    .pipe($.flatmap(function(stream, file) {
      var basename = 'Boxy ' + _.startCase(path.basename(file.path, path.extname(file.path)));

      return gulp.src('./sources/widgets/widget.stTheme')
        .pipe($.data(function() {
          var specific = require(file.path);

          return _.merge(common, specific);
        }))
        .pipe($.template())
        .pipe($.rename(function(widget) {
          widget.basename = 'Widget - ' + basename;
        }))
        .pipe(gulp.dest('./widgets'));
    }));
});

gulp.task('build:widget-settings', function() {
  return gulp.src('./sources/settings/specific/*.json')
    .pipe($.flatmap(function(stream, file) {
      var basename = 'Boxy ' + _.startCase(path.basename(file.path, path.extname(file.path)));

      return gulp.src('./sources/widgets/widget.sublime-settings')
        .pipe($.data(function() {
          var specific = require(file.path);

          return _.merge(common, specific);
        }))
        .pipe($.template())
        .pipe($.rename(function(widget) {
          widget.basename = 'Widget - ' + basename;
        }))
        .pipe(gulp.dest('./widgets'));
    }));
});

/* >> Extras */

gulp.task('build:extras', ['clean:extras'], function(cb) {
  runSequence(
    'process:extras',
    'convert:extras',
    function (error) {
      if (error) {
        console.log('[build:extras]'.bold.magenta + ' There was an issue building extras:\n'.bold.red + error.message);
      } else {
        console.log('[build:extras]'.bold.magenta + ' Finished successfully'.bold.green);
      }

      cb(error);
    }
  );
});

gulp.task('process:extras', function() {
  return gulp.src('./sources/settings/specific/*.json')
    .pipe($.flatmap(function(stream, file) {
      var basename = 'Boxy ' + _.startCase(path.basename(file.path, path.extname(file.path)));

      return gulp.src('./sources/extras/**/*.YAML-tmTheme')
        .pipe($.data(function() {
          var specific = require(file.path);

          return _.merge(common, specific);
        }))
        .pipe($.template())
        .pipe($.rename(function(scheme) {
          scheme.basename = basename;
        }))
        .pipe(gulp.dest('./extras'));
    }));
});

gulp.task('convert:extras', function() {
  return gulp.src('./extras/**/*.YAML-tmTheme')
    .pipe($.flatmap(function(stream) {
      return stream
        .pipe($.plumber(function(error) {
          console.log('[convert:extras]'.bold.magenta + ' There was an issue converting color extras:\n'.bold.red + error.message +
                      'To fix this error:\nAdd Sublime Text to the `PATH` and then install "PackageDev" via "Package Control".\nOpen Sublime Text before running the task.'.bold.blue);
          this.emit('end');
        }))
        .pipe($.exec('subl "<%= file.path %>" && subl --command "convert_file"'))
        .pipe($.exec.reporter());
    }));
});

/* >> Add-ons */

gulp.task('build:addons', ['clean:addons'], function(cb) {
  runSequence(
    'build:addon-themes',
    'build:addon-settings',
    function (error) {
      if (error) {
        console.log('[build:addons]'.bold.magenta + ' There was an issue building addons:\n'.bold.red + error.message);
      } else {
        console.log('[build:addons]'.bold.magenta + ' Finished successfully'.bold.green);
      }

      cb(error);
    }
  );
});

gulp.task('build:addon-themes', function() {
  return gulp.src('./sources/settings/specific/*.json')
    .pipe($.flatmap(function(stream, file) {
      var basename = 'Boxy ' + _.startCase(path.basename(file.path, path.extname(file.path)));

      return gulp.src('./sources/addons/**/*.addon-theme')
        .pipe($.data(function() {
          var specific = require(file.path);

          return _.merge(common, specific);
        }))
        .pipe($.template())
        .pipe($.rename(function(widget) {
          widget.basename = 'Widget - ' + basename;
        }))
        .pipe(gulp.dest('./addons'));
    }));
});

gulp.task('build:addon-settings', function() {
  return gulp.src('./sources/settings/specific/*.json')
    .pipe($.flatmap(function(stream, file) {
      var basename = 'Boxy ' + _.startCase(path.basename(file.path, path.extname(file.path)));

      return gulp.src('./sources/addons/**/*.addon-settings')
        .pipe($.data(function() {
          var specific = require(file.path);

          return _.merge(common, specific);
        }))
        .pipe($.template())
        .pipe($.rename(function(widget) {
          widget.basename = 'Widget - ' + basename;
        }))
        .pipe(gulp.dest('./addons'));
    }));
});

/*
 * > Images
 */

gulp.task('optimize', function(cb) {
  runSequence(
    'optimize:assets',
    'optimize:icons',
    function (error) {
      if (error) {
        console.log('[optimize]'.bold.magenta + ' There was an issue optimizing images:\n'.bold.red + error.message);
      } else {
        console.log('[optimize]'.bold.magenta + ' Finished successfully'.bold.green);
      }

      cb(error);
    }
  );
});

gulp.task('optimize:assets', function() {
  return gulp.src('./assets/**/*.png')
    .pipe($.imagemin([$.imagemin.optipng({
      bitDepthReduction: false,
      colorTypeReduction: false,
      paletteReduction: false
    })], {verbose: true}))
    .pipe(gulp.dest('./assets'));
});

gulp.task('optimize:icons', function() {
  return gulp.src('./icons/*.png')
    .pipe($.imagemin([$.imagemin.optipng({
      bitDepthReduction: false,
      colorTypeReduction: false,
      paletteReduction: false
    })], {verbose: true}))
    .pipe(gulp.dest('./icons'));
});

/*
 * > Release
 */

gulp.task('changelog', function() {
  return conventionalChangelog({
    preset: 'angular',
    releaseCount: 0
  })
  .pipe(fs.createWriteStream('CHANGELOG.md'));
});

gulp.task('bump', function(cb) {
  runSequence(
    'bump-pkg-version',
    'bump-env-version',
    function (error) {
      if (error) {
        console.log('[bump]'.bold.magenta + ' There was an issue bumping version:\n'.bold.red + error.message);
      } else {
        console.log('[bump]'.bold.magenta + ' Finished successfully'.bold.green);
      }
      cb(error);
    }
  );
});

gulp.task('bump-pkg-version', function() {
  return gulp.src('./package.json')
    .pipe($.if((Object.keys(argv).length === 2), $.bump()))
    .pipe($.if(argv.patch, $.bump()))
    .pipe($.if(argv.minor, $.bump({ type: 'minor' })))
    .pipe($.if(argv.major, $.bump({ type: 'major' })))
    .pipe(gulp.dest('./'));
});

gulp.task('bump-env-version', function() {
  return gulp.src('./utils/environment.py')
    .pipe($.if((Object.keys(argv).length === 2), $.bump({ regex: envRegExp })))
    .pipe($.if(argv.patch, $.bump({ regex: envRegExp })))
    .pipe($.if(argv.minor, $.bump({ type: 'minor', regex: envRegExp })))
    .pipe($.if(argv.major, $.bump({ type: 'major', regex: envRegExp })))
    .pipe(gulp.dest('./utils'));
});

gulp.task('github-release', function(done) {
  conventionalGithubReleaser({
    type: 'oauth',
    token: process.env.CONVENTIONAL_GITHUB_RELEASER_TOKEN
  }, {
    preset: 'angular'
  }, done);
});


/*
 * > Watch
 */

gulp.task('watch', function() {
  gulp.watch('./sources/themes/**/*.json', ['build:themes']);
  gulp.watch('./sources/schemes/scheme.YAML-tmTheme', ['build:schemes']);
  gulp.watch('./sources/extras/**/*.YAML-tmTheme', ['build:extras']);
  gulp.watch('./sources/addons/**/*.*', ['build:addons']);
  gulp.watch('./sources/widgets/widget.*', ['build:widgets']);
  gulp.watch('./sources/settings/**/*.json', ['build:schemes', 'build:extras', 'build:widgets', 'build:themes']);
});


/*
 * > Default
 */

gulp.task('default', ['build']);
