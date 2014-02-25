module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    sass: {
      dist: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          '../static/css/app.min.css': 'sass/app.scss'
        }
      }
    },
    imageEmbed: {
      dist: {
        src: ['../static/css/app.min.css'],
        dest: '../static/css/app.min.css',
        options: {
          deleteAfterEncoding : false
        }
      }
    },
    concat: {
      dist: {
        src: ['js/jquery.js', 'js/plugins.js', 'js/app.js'],
        dest: '../static/js/app.all.js'
      }
    },
    uglify: {
      scripts: {
        files: {
          '../static/js/app.min.js': ['../static/js/app.all.js']
        }
      }
    },
    watch: {
      sass: {
        files: ['sass/**/*.scss'],
        tasks: ['sass']
      },
      concat: {
        files: ['js/**/*.js'],
        tasks: ['concat']
      },
      uglify: {
        files: ['../static/js/app.all.js'],
        tasks: ['uglify']
      }
    }
  });
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.loadNpmTasks("grunt-image-embed");
  grunt.registerTask('default', ['sass', 'imageEmbed', 'concat']);
  grunt.registerTask('deploy', ['sass', 'imageEmbed', 'concat', 'uglify']);
};