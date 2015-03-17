Juan Elosua personal blog
=========================

Source content for the [pelican](http://blog.getpelican.com) project that
I am using to create my personal blog

Huge thanks to _pelican team_, _[DandyDev](https://github.com/DandyDev/pelican-bootstrap3)_ and _[davisp](https://github.com/davisp/ghp-import)_ for their great work that makes this blog so straight forward to build.

## pelican-bootsrap3 Theme

I have change the base pelican-bootsrap3 theme to use a glyphicon as the site logo and removed the author header on the sidebar.

To do the same just clone my modified repo
    $ git clone https://github.com/jjelosua/pelican-bootstrap3

Then install the theme with the command line tool provided by pelican
    $ pelican-themes -vi path/to/cloned_repo


## Plugins repo

The configuration file asumes that you have cloned the [pelican plugins repo](https://github.com/getpelican/pelican-plugins) in a folder that lives next to this repo folder. 
    $ cd .. # move one level down from your pelican blog repo
    $ git clone git@github.com:getpelican/pelican-plugins.git




