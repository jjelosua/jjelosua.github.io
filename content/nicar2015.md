Title: 2015 Nicar conference
Date: 2015-03-17 13:20
Category: event
Tags: opennews
Slug: nicar2015



This year's NICAR conference in Atlanta was overall a great experience, It has helped me focus my fellowship year on machine learning. I think this technique will become more and more adopted by newsrooms in the following years.

I have met many people with my same interests (is always good not to feel alone...). I also had the opportunity to get to know more the 2015 knight-mozilla fellows cohort and spend time with other fellows from past years.

![Atlanta](/images/nicar2015/Atlanta.jpg){.post_left width=48%} ![Nicar](/images/nicar2015/NicarEvolution.jpg){.post_right width=48%} 

This year's NICAR conference in Atlanta was overall a great experience, It has helped me focus my fellowship year on machine learning. I think this technique will become more and more adopted by newsrooms in the following years.

I have met many people with my same interests (is always good not to feel alone...). I also had the opportunity to get to know more the 2015 knight-mozilla fellows cohort and spend time with other fellows from past years.

I can divide the sessions that had more impact on me in two subgroups: technical and management oriented.

<div class="clear_float"></div> 

***

## Management oriented sessions

### Do it once and only once

![Do It Once](/images/nicar2015/DoItOnce.png){.post_right width=50%} 

Speakers: _[Derek Willis](https://twitter.com/derekwillis)_ & _[David Eaves](https://twitter.com/eads)_

Derek and David warned us about the time wasting perils of data processing without automation and audit trails.

One of the highlights of the talk to me was finding out about [Ben Balter change agent](https://github.com/benbalter/change_agent): A Git-backed key-value store, for tracking changes to documents and other files over time as defined by ben in the repo.

I always thought that version control will be applied to other industries outside technology soon and that is going to be a changemaker in that industry.

Slides: _[Derek Slides](http://dwillis.github.io/do-it-once-nicar-2015/)_ & _[David Slides](http://recoveredfactory.net/cleaner-data-nicar15/)_

### Processes, standards and documentation for data-driven projects

![Christopher Groskopf](/images/nicar2015/ChristopherTip.png){.post_right width=50%} 

Speakers: _[Christopher Groskopf](https://twitter.com/onyxfish)_ & _[Paul Overberg](https://twitter.com/poverberg)_

In this session Paul and Christopher walked us through the importance of creating team standards, project vocabularies and consistent procedures to produce high quality projects in a sustainable way. This is especially crucial when working under a deadline something that happens naturally in newsrooms.

In particular I found Christopher's part full of wisdom. Coming from someone that has worked in newsrooms and remotely for a while and that has taken the time to share his experience in this invaluable [tips](http://recoveredfactory.net/cleaner-data-nicar15/).

<div class="clear_float"></div>

***

## Technical sessions

### From text to pictures

![Text Visualization inspiration](/images/nicar2015/TextVizInspiration.png){.post_full width=70%}

### Plot.ly

![Plotly](/images/nicar2015/plotly.png){.post_right width=50%} 

Speakers: _[Matthew Sundquist](https://www.linkedin.com/pub/matt-sundquist/30/800/752)_

Until NICAR I had not heard about plot.ly (yeah I know...shame on me!!) and I think that it has a lot of potential in the data journalism field and ranging from journalists that want to create graphs without coding to developers through their [API](https://plot.ly/api/).

It generates D3.js visualizations under the hood but it exposes many ways to perform an integration with the platform.

To find out more just check their [tutorials](https://plot.ly/learn/) and [API documentation](https://plot.ly/api/)

### Using machine learning to deal with dirty data: a Dedupe demonstration

![Dedupe](/images/nicar2015/Dedupe.png){.post_right width=50%}

Speakers: _[Jeff Ernsthausen](https://twitter.com/jeffernsthausen)_, _[Derek Eder](https://twitter.com/derekeder)_, _[Eric van Zanten](https://twitter.com/evanzanten)_ & [Forest Gregg](https://github.com/fgregg)

If I had to pick my favorite session from this year's conference I would have to choose the demo on a tool developed by datamade called [Dedupe](https://github.com/datamade/dedupe).

It is a machine learning based python library for accurate and scalable data deduplication and entity-resolution. I have fought many times with trying to combine different datasets that do not have a clear identifier to join by. OpenRefine can help with small datasets but the process of clustering is not repeatable and even more important it is not scalable.

Having a machine learning process for that kind of task is probably the best way to go. I got so inspired by that demo that I think a big part of my fellowship is going to be focused on machine learning and how to apply it to journalistic problems. 

![Dedupe OpenSource](/images/nicar2015/Dedupe_OSS.png){.post_full width=70%}

As a starter I am going to use dedupe to try to match two different datasets for the upcoming argentinian elections, in next posts I will tell you how it went and what have I learned in the process.

<div class="clear_float"></div>

***

## Technical tip of the day

Let's dig a little bit deeper on how to install numpy with parallel processing support on a Mac OS X (tested on 10.9 and 10.10) you can read more about the convoluted issue [here](http://mail.scipy.org/pipermail/numpy-discussion/2012-August/063589.html). Since it took me a while to get things working for me I thought maybe sharing my pains can help someone in the future.

I will walk you through the installation process that has worked for me, if you think it can be improved don't hesitate to contact me.

1. If you have not installed homebrew, the first step is to do so:
    
        :::shell
        $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

2. Set up some compilation flags on your environment of choice
    
        :::shell
        export CFLAGS=-Qunused-arguments 
        export CPPFLAGS=-Qunused-arguments  

3. Brew tap the homebrew python repo
    
        :::shell
        $ brew tap homebrew/python

4. Install numpy with OpenBlas support

        :::shell
        $ brew install numpy --with-openblas

5. Check if numpy is linked against OpenBlas

        :::python
        >>> import numpy as np
        >>> np.__config__.show()

6. You should see an output like this

        :::python
        lapack_opt_info:
            libraries = ['openblas', 'openblas']
            library_dirs = ['/usr/local/opt/openblas/lib']
            language = f77
        blas_opt_info:
            libraries = ['openblas', 'openblas']
            library_dirs = ['/usr/local/opt/openblas/lib']
            language = f77
        openblas_info:
            libraries = ['openblas', 'openblas']
            library_dirs = ['/usr/local/opt/openblas/lib']
            language = f77
        openblas_lapack_info:
            libraries = ['openblas', 'openblas']
            library_dirs = ['/usr/local/opt/openblas/lib']
            language = f77
        blas_mkl_info:
          NOT AVAILABLE

7. Now you can continue with the normal installation process for dedupe, just remember to include system packages if you are going to use a virtualenv so that are compiled OpenBlas numpy will be used inside the virtual environment

        :::shell
        $ virtualenv venv --system-site-packages

<div class="clear_float"></div>

***

## Wrap up

This year's NICAR conference in Atlanta was overall a great experience, It has guided me towards machine learning as a focus for my fellowship year. I think this technique will become more and more adopted by newsrooms in the following years.

I have met many people with my same interests (is always good not to feel alone... ;-)). I also had the opportunity to get to chat more with the 2015 knight-mozilla fellows cohort and also spend sometime with other fellows from past years.

I would recommend anyone interested in the data journalism field to at least attend once to this conference organized by [Investigative Reporters & Editors](http://ire.org/about/) you will not regret it.

<div class="clear_float"></div>








