Title: 2015 Knight-Mozilla fellowship onboarding
Date: 2015-01-20 13:20
Category: event
Tags: opennews
Slug: onboarding

2015 is starting and as a new Knight-Mozilla fellows I joined the rest of the cohort in the onboarding event in Los Angeles. I am very grateful to Dan, Erika, Ryan and Erin (in spirit) for giving us the opportunity to get to know the rest of the fellows in more depth both personally and professionally.

This fellowship is one of a kind in the sense that each one of us is going to be headed to a different newsroom so this event was a good opportunity to establish relationships that will be kept during 2015 but mainly through remote channels.

In this post I will try to share with you my impressions of the event where we have received tons of information and were able to work together in an open source project started by the [California Civic Data Coalition](http://www.californiacivicdata.org/) that tries to provide a better understanding of campaign finance in the state of California.

***

## Day 1 (Jan 12th)

To start the onboarding event we went to [The Hub LA](http://www.thehubla.com/), Two former fellows [Brian Abelson](https://twitter.com/brianabelson) (2013) and [Aurelia Moser](https://twitter.com/auremoser) (2014) joined us and share their experiences and tips with us. It was really important to listen to their advices since they are the best counsellors that we could have having lived the same situations that we are going to have this year.

Some of their recommendations were:
* Try to stay as organized as possible
* Have a fluent communication about your interests and schedule with your point of contact in the newsroom
* Conferences are great but this fellowship is in no way a one-shot opportunity so try to select the ones that will be more profitable.

We were also fed with a full plate of information from the opennews staff regarding logistics, policies, community and how to work in the open sharing the experience as one of the main goals of the fellowship.

***

## Day 2 (Jan 13th)

![LATimes visit](/images/onboarding/LAtimes.jpg){.post_left width=50%}

We visited the LA Times newsroom guided by [Ben Welsh](https://twitter.com/palewire). We shamelessly interrupted some journalists and got the chance to ask them questions regarding their work and their relationship with the Data Desk that Ben leads at the newsroom. It was really an interesting visit where we got the sense of the work that each of us will be doing at our host newsroom.

Data journalism seems to be a brand new thing but we have learned from people in the LA times that data related investigations have been done since the 80s...of course with different tools but we are not reinventing the wheel, the challenges and workflows of data investigations apply the same now as they did back then.

<div class="clear_float"></div>

***

## Day 3 (Jan 14th)

We went to USC to begin our two hackdays on the [CAL-ACCESS campaign browser](http://django-calaccess-campaign-browser.californiacivicdata.org/en/latest/) project. Ben Welsh and [Aaron Williams](https://twitter.com/aboutaaron) from the CIR gave us an overview of the project goals and the tasks that they had in mind for our contribution to the project.

![USC campaign-browser hackday](/images/onboarding/hackday.jpg){.post_right width=50%}

The campaign browser is an ongoing project that aims at helping journalists and other interested persons in improving their way of extracting meaningful information out of  the [CAL-ACCESS](http://cal-access.ss.ca.gov/default.aspx) data.

We had tasks that were oriented towards frontend as well as backend improvements.

Since I am more comfortable in backend tasks, [Francis](https://twitter.com/frnsys), Ben and I started working on a scraper ran as a custom django-admin command that will complement the information dump that the secretary of state publishes on a daily basis.

We wanted to be able to answer some questions that believe it or not were not possible to answer without that scraping task from the original dump, for example: How much money was spent in campaign finance for each election?

Also we wanted to be able to link each ballot measure with their supporting/opposing committees and we wrote a second scraper to do that.

### Tech tip of the day

If you have not used Django models before there is one nice feature that I will try to point out when building many-to-many relationships in a Django model.

In our example a _propostition/ballot measure_ can have many _committees_ associated with but that works reversely also a _committee_ can support/oppose to many _propositions_. In relational databases this is known as a many-to-many relationship.

Django allows you to model that with a [ManyToManyField](https://docs.djangoproject.com/en/1.7/topics/db/examples/many_to_many/). 

When creating the model using the migrate command, Django under the hood will create a table in the Database for the relationship between _proposition_ and _committee_.

    :::shell
    $ python manage.py migrate

But what if we wanted to characterize that relationship with some attribute as is the case in out example. We don't want just the relationship between a _proposition_ and a _committee_ we want to know also if the _commitee_ is supporting or opposing to the _proposition_. 

We can do that in Django by providing a *through* model to the ManyToManyField (In CAL-ACCESS a committee is identified by a Filer). Now we can explicitly create the relationship model.

    :::python hl_lines="5"
    class Proposition(BaseModel):
        name = models.CharField(max_length=255, null=True)
        filer_id_raw = models.IntegerField(db_index=True) #
        election = models.ForeignKey(Election, null=True, default=None)
        filers = models.ManyToManyField(Filer, through='PropositionFiler')

Take a look at the PropositionFiler class that models the relationship. We need to provide at least the keys that will relate the two models in our case _proposition_ and _filer_ (When not using a through model this would be what django will create under the hood). But now check the position field where we can characterize the relationship with a support or oppose stating whether the committee (filer) opposes/supports the related proposition.

    :::python hl_lines="6 7"
    class PropositionFiler(BaseModel):
        POSITION_CHOICES = (
            ('SUPPORT', 'Support'),
            ('OPPOSE', 'Oppose'),
        )
        proposition = models.ForeignKey(Proposition)
        filer = models.ForeignKey(Filer)
        position = models.CharField(
            choices=POSITION_CHOICES,
            max_length=50
        )

You can use a through model in a many-to-many relationship each time you need to qualify our characterize that relationship with some attributes.

You can read more about the through option in the awesome django documentation [here](https://docs.djangoproject.com/en/1.7/topics/db/models/#intermediary-manytomany)

<div class="clear_float"></div>

***

## Day 4 (Jan 15th)

After a successful scrape we cleaned up the code a little bit, document it and pushed the changes. I have not been involved in large open source projects with more than 3 or 4 developers so this was a good opportunity to grasp important ideas related to documentation and workflows needed to keep a distributed open source project running smoothly.

Ben, shared with us his vision on the _Documentation Driven Development_ which I thought was a nice advise to push open source projects forward instead of what Dan mentioned to be _source available_ projects. I certainly need to progress on this myself and that is one of the challenges I will be facing during this fellowship year.

I switched to some frontend task to help [Tara](https://twitter.com/taraandtheworld) figure out how to handle a visualization that uses [dc.js](http://dc-js.github.io/dc.js/). DC.js is a javascript charting library with native [Crossfilter](http://square.github.io/crossfilter/) support allowing highly efficient exploration on large multi-dimensional dataset. It leverages [D3](http://d3js.org/) engine to render charts in css friendly svg format.

![DC.js library](/images/onboarding/dc.png){.post_full_nb}

If you want to get started with dc.js I found this four part [tutorial](http://www.codeproject.com/Articles/693841/Making-Dashboards-with-Dc-js-Part-Using-Crossfil) easy to follow when I try to figure out how to use that library...Trust me give it a chance...you will love it!!

<div class="clear_float"></div>

***

## Summary

![github activity](/images/onboarding/commits.png){.post_right_nb width=50%}

Overall the onboarding event was a great experience, we got to work together as a cohort and shared our strong and weak points with the rest. I feel now more comfortable to work together, share our knowledge and collaborate in some projects during this amazing year.

To end this post I will like to thank [Dan](https://twitter.com/dansinker), [Erika](https://twitter.com/erika_owens) and [Ryan](https://twitter.com/ryanpitts) for their support and openness...you make everybody feel welcomed and challenged to keep growing the awesome data journalism tech community out there.

<div class="clear_float"></div>

![USC fellows](/images/onboarding/fellows.jpg){.post_full width=70%}










