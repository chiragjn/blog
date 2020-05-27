ProFit app showcase
###################

:date: 2016-2-29 22:05
:tags: technology,software,fitness,hackathon,android,fitons
:category: Technology
:slug: profit-app-showcase
:summary: The ProFit android app showcase
:status: published


So a lot of people asked me about what my team made that won us the first prize at SportsHack 2016 Hackathon held by `Zone Startups`_,India in Association with `Australia Institute of Sports`_.So here's to ProFit - The PROfessional FITness App.

.. image:: images/profit/ic_launcher.png
   :height: 144
   :width: 144
   :scale: 100%
   :alt: ProFit App Icon
   :align: center

============
About ProFit
============

ProFit is a fitness platform that provides features such as deep Google Now integration, which allows the user to log any activity to ProFit without having to open the app using his/her voice, ProFit aims at minimizing tedious interactions such as data entry by automating it as much as possible. To do the same, ProFit also allows users to create sessions(set of activities) which can be logged together and use data provided by Google Fit.

A major part of ProFit lies in Gamification, ProFit has its own Fitness currency called ‘Fitons’, Users are granted Fitons based on the activities they perform and other personal parameters. Users can earn bragging rights by sharing graphs, ratings and activities on social media to compare  with their peers. ProFit also provides dynamic suggestions to the user based on their history, their goals and safety criteria.

ProFit also lets you set said Goals which your suggestions are based on, such as ‘5k Marathon’. ProFit also shows comprehensive statistics about your activities and goals. ProFit provides a backend admin to monitor and update all users’ data and provide suggestions.

===========
Screenshots
===========

.. container:: text-align-center

	.. image:: images/profit/home0.png
	   :width: 720
	   :height: 1280
	   :scale:  30%
	   :alt: Home Screen
	.. image:: images/profit/home2.png
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: Home Screen
	.. image:: images/profit/homefab.png
	   :width: 720
	   :height: 1280
	   :scale:  30%
	   :alt: Home Screen FAB Menu
	.. image:: images/profit/homeexpanded.png
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: Home Screen Sugeestion Expanded
	.. image:: images/profit/activity.png
	   :width: 720
	   :height: 1280
	   :scale:  30%
	   :alt: Logging Activity
	.. image:: images/profit/sessions.png
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: Adding Sessions
	.. image:: images/profit/gnow.png
	   :width: 720
	   :height: 1280
	   :scale:  30%
	   :alt: Use your voice with Google Now to Log Sessions/Activities/Weight
	.. image:: images/profit/gnowreact.png
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: And Google Now and we will do the Magic
	.. image:: images/profit/stats1.png
	   :width: 720
	   :height: 1280
	   :scale:  30%
	   :alt: Beautiful statistics graphs
	.. image:: images/profit/stats2.png
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: Beautiful statistics graphs
	.. image:: images/profit/stats3.png
	   :width: 720
	   :height: 1280
	   :scale:  30%
	   :alt: Beautiful statistics graphs
	.. image:: images/profit/twittershare.png
	   :width: 720
	   :height: 1280
	   :scale:  30%
	   :alt: Share your graphs on Twitter
	.. image:: images/profit/goals.png
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: Set some goals
	.. image:: images/profit/profile.png
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: Profile Screen

===========================
Screencast clips
===========================

.. container:: text-align-center

	.. image:: images/profit/tabs_scr.gif
	   :width: 720
	   :height: 1280
	   :scale:  30%
	   :alt: All the tabs
	.. image:: images/profit/homedeco.gif
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: Home Screen DecoView Animation
	.. image:: images/profit/fab.gif
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: Floating Action Button To Toolbar Animation
	.. image:: images/profit/homeexpand.gif
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: Home Screen Expanding ListView Suggestions
	.. image:: images/profit/profile.gif
	   :width: 720
	   :height: 1280
	   :scale: 30%
	   :alt: Profile Screen DecoViews

===============
The Fitons team
===============

.. image:: images/profit/fitons.jpeg
   :alt: Profile Screen DecoViews
   :align: center

.. raw:: html

	<div style="font-size:0.95rem;text-align:center;">From left to right: Chirag Jain, <a href="https://www.facebook.com/s4shyam95">Shyam Mehta</a> and <a href="https://www.facebook.com/paren200">Paren Desai</a></div>

=============
For the Geeks
=============

The source code for this Android app is available here_.But it is no where near production level code and it contains deliberate 'hacks' to make things work.Also we used Apache ANT build system(will never again,we hit the 65K dex methods limit :P ) instead of Gradle so checkout project.properties files for all the awesome libraries we used.

Also, will update this article with the minor problems we faced during development.


=======
Credits
=======

`Shyam Mehta`_ for the summary on ProFit

Vitaly Rubstov for his inspiring `Workout Book UI and UX concept`_ 


.. _`Australia Institute of Sports`: http://www.ausport.gov.au/ais
.. _`Zone Startups`: http://india.zonestartups.com/
.. _here: https://github.com/chiragjn/ProFit-Android
.. _`Shyam Mehta`: https://www.facebook.com/s4shyam95
.. _`Workout Book UI and UX concept`: http://works.yalantis.com/workout-book/
