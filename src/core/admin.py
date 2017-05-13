# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Account, Tweet, FavouriteTweet, Follower, Mention, Retweet


admin.site.register(Account)
admin.site.register(Tweet)
admin.site.register(FavouriteTweet)
admin.site.register(Follower)
admin.site.register(Mention)
admin.site.register(Retweet)
