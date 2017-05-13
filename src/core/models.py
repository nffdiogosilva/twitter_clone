# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Account(User):
    pass


class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tweet = models.CharField(max_length=140, default="What's Happening?")

    user = models.ForeignKey(Account)

    def __unicode__(self):
        "{}".format(self.tweet)


class FavouriteTweet(models.Model):
    tweet = models.ForeignKey(Tweet)
    user = models.ForeignKey(Account)

    class Meta:
        unique_together = ('tweet', 'user')


class Follower(Account):
    # need to exclude self from queryset
    following = models.ForeignKey("self")


class Mention(models.Model):
    tweet = models.ForeignKey(Tweet)
    user = models.ForeignKey(Account)


class Retweet(models.Model):
    tweet = models.ForeignKey(Tweet)
    user = models.ForeignKey(Account)
