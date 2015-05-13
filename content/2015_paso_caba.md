Title: 2015 PASO CABA Elections
Date: 2015-05-10 13:20
Category: fellowship
Tags: opennews, elections
Slug: 2015pasocaba

On April 26th Buenos Aires has held its first PASO elections. PASO stands for Simultaneous and Obligatory Open Primary elections. In this election two main things are decided:

* Which candidate will pass as the official candidate for each political party for the final elections
* Each political party has to achieve at least 1.5% of the total votes to be able to continue on the election race.

These were my first elections inside a newsroom and it was thrilling!! It was like being inside a movie surrounded by journalists waiting for the initial results to rush to their computers to write articles and analysis... but we needed data and I can tell you it was not easy.

This 2015 will be a year full of elections: Regional PASO elections, Regional final elections and the mother of all... Presidential elections.

![Calendar](/images/2015_paso_caba/calendar.jpg){.post_left width=48%}In Argentina voting is a compulsory right, so Argentinians will be voting many times during this year. One of the first things that stroke me as a foreigner is that PASO elections are not withheld inside the political party affiliates but rather extended to the whole census. In Spain Primary elections only affect the affiliates and thus are rather overlooked by the overall population. 

I have had some interesting discussions on whether extending Primary elections to the overall population is a good democratic procedure... on one hand it always seems a good idea to let people decide the candidate that they want for their party of choice...but on the other hand having such a low barrier for making the cut for the next round would theoretically allow "big" parties to try to tweak the results of their other contestants by asking their loyal voters to vote for the other party weak candidate...kind of convoluted but possible.

The local government decided to switch technological providers for this and upcoming elections and as usual there is some adjustment time to get things working smoothly. 

At La Nación, we wanted to make a news app that would allow readers to perform realtime analysis of the results of the elections showing as many details as possible, therefore we wanted to show the results by polling station.

## Frontend isolation
Due to the mentioned technical change the local government was running late in providing newsrooms with details on how the results were going to be made available during the realtime vote counting process.

So we decided that we needed to _blackbox_ the frontend needs and specify a data format that was required by the frontend leaving the transformation tasks to the backend and assuming that it was going to be doable after all.

That way we could move forward in defining the final visualizations and the different reader interaction capabilities and drilldown analysis.

<div class="clear_float"></div>

***

## Backend nightmare
![API](/images/2015_paso_caba/API.jpg){.post_right width=48%} After being really persuasive with government officials, we ended up having some documentation on the 21st of April... we were going to have an API to query but not many details yet.

We started defining the backend structure out of thin air, trying to be modular so that we could be efficient when changes were necessary.

Trying to divide the functionality in modules helps when you find an error, because you can easily go directly to the module that is causing the error and correct it. But on the other hand, it results in more difficulties in keeping the state of the overall process simple enough. We relied on [User-Defined Exceptions](https://docs.python.org/2/tutorial/errors.html#user-defined-exceptions){:target="_blank"} to keep track of the overall process while executing code in a module deep down the execution stack.

We did not have data yet to test the process so we developed an adhoc simulation script that would randomly produce voting results distributions. My wife to the rescue... [Marta](https://twitter.com/marta_alonso_f) helped us develop the results simulation and I believe that was a key decision in the overall success of the project since it allowed us to start testing the backend well ahead of the API availability.

Finally we were given an endpoint to test the government API by friday 24th at 18h... fun weekend ahead. 

<div class="clear_float"></div>

***

## Logging: What the h...  is going on!!! 
![Postman](/images/2015_paso_caba/log.jpg){.post_right width=48%}As a realtime application (running on EC2 machines) we knew that it was almost as important to have an easy way to keep track of what was going on in the backend on realtime to be able to act quickly in case something unexpected happened.

We developed a logging strategy that was published each time the process was run (each minute), making it accessible through HTTP.

For monitoring purposes we used [Postman](https://chrome.google.com/webstore/detail/postman-rest-client-packa/fhbjgbiflinjbdggehcddcbncdddomop?hl=en){:target="_blank"}, a chrome app that lets you define and save collections of HTTP requests:

* One collection for the government API endpoints
* One collection for the backend monitoring 

<div class="clear_float"></div>

***

## Concurrency >100.000 simultaneous visitors
Being a freelance developer that used to work with NGOs in Spain to increase transparency and the use of Open Data I had not being exposed to the traffic that the homepage of La Nación receives on an election day. So It was really interesting for me to learn from the infrastructure and architecture team the tips & tricks that we needed to take into account in order to be successful: HTTP caches, Content Delivery Networks configuration and static files versioning... All of that was new to me, but really important in terms of performance and bug fixing on the fly.

To be able to handle that, we decided that we needed an "almost" automatic way of deployment that would decrease the probabilities of human errors while going through a somewhat stressful situation. We used [_gulp_](http://gulpjs.com/){:target="_blank"} to automate the deployment process, letting it handle the minification, uglyfying and versioning for us. Extract of the gulp deployment process:

    :::js
    gulp.task('minify-css', function () {
    gulp.src(['css/reset.css', 'css/fonts.css', 
              'css/select2.css', 'css/style.css'], { cwd: '../webapp' })
    .pipe(minifyCSS())
    .pipe(concat(css_file_min))
    .pipe(gulp.dest('../build/css'));
    });

    gulp.task('test_js', function(){
        return gulp.src(['js/permanentlinkjs.js', 'js/handlebars_helpers.js',
                         'js/elecciones_app.js', 'js/scripts.js'], { cwd: '../webapp' })
            .pipe(jshint())
            .pipe(jshint.reporter('default'))
            .pipe(jshint.reporter(stylish));
    });

    gulp.task('js', ['test_js'], function () {
        var all = gulp.src(['js/permanentlinkjs.js', 'js/handlebars_helpers.js',
                           'js/elecciones_app.js', 'js/scripts.js'] , { cwd: '../webapp' })
            .pipe(sourcemaps.init())
            .pipe(uglify())
            .pipe(concat(js_all))
            .pipe(sourcemaps.write('./'))
            .pipe(gulp.dest('../build/js'));
        
        var vendor = gulp.src([
            'libs/jquery/dist/jquery.min.js', 
            'libs/select2/select2.min.js', 
            'libs/handlebars/handlebars.min.js', 
            'libs/jquery.nicescroll/jquery.nicescroll.min.js', 
            ], { cwd: '../webapp' })
            .pipe(sourcemaps.init())
              .pipe(uglify())
              .pipe(concat(js_vendor))
            .pipe(sourcemaps.write('./'))
              .pipe(gulp.dest('../build/libs'));

        return merge(all,vendor);
        
    });

    gulp.task('copy', function () {
        var opts = {
            conditionals: true,
            spare:true
        };
        var html = gulp.src('*.html', { cwd: '../webapp' })
            .pipe(htmlreplace({
                js:['libs/'+js_vendor, 'js/'+js_all],
                css: ['css/'+css_file_min]
            }))
            .pipe(minifyHTML(opts))
            .pipe(gulp.dest('../build'));

        
        var fonts = gulp.src('css/fonts/*', { cwd: '../webapp' })
            .pipe(gulp.dest('../build/css/fonts'));

        var img = gulp.src('img/*', { cwd: '../webapp' })
            .pipe(gulp.dest('../build/img'));

        var css_img = gulp.src(['css/images/*'], { cwd: '../webapp' })
            .pipe(gulp.dest('../build/css/images'));

        var data = gulp.src('data/*', { cwd: '../webapp' })
            .pipe(gulp.dest('../build/data'));

        return merge(html, fonts, img, css_img, data);
    });

    gulp.task('build', ['minify-css', 'js', 'copy']);
   

## Realtime news app
At the end, on the election day, we were "anxious" to check if the kind of creative way of connecting the dots was going to work out... and it did!!

After sometime while the API was not responding we were able to get a full response to our backend and transform it to the frontend expected format... that was at 22:30 Sunday night... we even published the initial results before the official government page that was suffering from availability issues.

We have cleaned up after ourselves and have released the code of the project on github [here](https://github.com/lanacioncom/elecciones_2015_caba)

[![Realtime map](/images/2015_paso_caba/realtime.jpg){.post_left_together width=48%}](http://www.lanacion.com.ar/1787651-elecciones-2015-resultados-de-las-paso-portenas-en-un-mapa-interactivo){:target="_blank"} [![Realtime ranking](/images/2015_paso_caba/quienesquien.jpg){.post_right_together width=48%}](http://www.lanacion.com.ar/1787653-en-vivo-como-se-perfilan-los-ganadores-y-perdedores-de-las-paso-portenas){:target="_blank"}

<div class="clear_float"></div>

***

## Calm after the storm... Nope!!

After the adrenaline came down a bit we realized that had not completed our task since we wanted to let the readers go deep into their local details... we needed the results by polling station.

Luckily [Manuel Aristarán](http://jazzido.com/) had worked on a similar project for the 2013 elections and we had worked in advance to obtain the geolocation of each polling station. 

Thanks to that we could delivered a map that showed the results for each polling station the same day we got the official results from the Buenos Aires Government.

[![polling station results](/images/2015_paso_caba/polling_station.jpg){.post_full width=90%}](http://www.lanacion.com.ar/1788681-como-fueron-los-resultados-de-las-paso-en-la-escuela-donde-votaste){:target="_blank"}

We used [_cartodb.js_ API](http://docs.cartodb.com/cartodb-platform/cartodb-js.html){:target="_blank"} [_require.js_](http://requirejs.org/){:target="_blank"} in order to keep the javascript development modular. 

To avoid having too many HTTP requests we finally integrated the requirejs optimizer into the gulp deployment pipeline so that we have the benefit of modularity in development but with a nice performance on production.

[Here](https://github.com/lanacioncom/2015_paso_caba_map){:target="_blank"} is the open sourced code for that map.

<div class="clear_float"></div>

***

## Wrap up

![Team](/images/2015_paso_caba/team.jpg){.post_right width=48%}I am really grateful for being able to have lived the election experience inside a newsroom. We have worked hard as a team and the overall results were really positive... really proud of the team and the effort.

Thanks to the rest of the team [Cristian Bertelegni](https://twitter.com/cbertelegni), [Gaston de la Llana](https://twitter.com/gasgas83) and [Pablo Loscri](https://twitter.com/ploscri) for keeping such a nice working atmosphere. I would also like to send special thanks to Flor Fernández and Mariana Trigo for their support.

It is worth mentioning that all this work and analysis was not only used in the online edition at La Nación. The results from the developed _News Apps_ were also used to enrich the reader experience on the paper edition. That means a double win for the newsroom: creating an interactive application that will also generate value on the printed version.

![paper edition](/images/2015_paso_caba/paper.jpg){.post_full width=100%}

<div class="clear_float"></div>



