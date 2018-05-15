========================================
Django Admin Multiple Choice List Filter
========================================

The SimpleListFilter that ships with Django only allows you to filter on one
option at a time. MultipleChoiceListFilter extends SimpleListFilter to allow you
to filter on multiple options.

Getting started
---------------

Install via pip::

  pip install django-admin-multiple-choice-list-filter

Add to INSTALLED_APPS in settings.py::

  # project/settings.py

  INSTALLED_APPS = [
      ...
      'django_admin_multiple_choice_list_filter',
  ]

As an example, let's say you had a ``shop`` app. In that app you have an ``Order`` model with a ``status`` field that has limited choices::

  # shop/models.py

  from django.db import models


  class Statuses(object):
      RECEIVED, PROCESSING, SHIPPED, CLOSED = range(0, 4)

      CHOICES = (
          (RECEIVED, 'Received'),
          (PROCESSING, 'Processing'),
          (SHIPPED, 'Shipped'),
          (CLOSED, 'Closed'),
      )


  class Order(models.Model):
      status = models.IntegerField(
          choices=Statuses.CHOICES,
          default=Statuses.RECEIVED,
      )

Then, in your app's admin.py::

  # shop/admin.py

  from django.contrib import admin

  from django_admin_multiple_choice_list_filter.list_filters import MultipleChoiceListFilter

  from .models import Order, Statuses


  class StatusListFilter(MultipleChoiceListFilter):
      title = 'Status'
      parameter_name = 'status__in'

      def lookups(self, request, model_admin):
          return Statuses.CHOICES


  class OrderAdmin(admin.ModelAdmin):
      list_display = ('status',)
      list_filter = (StatusListFilter,)

  admin.site.register(Order, OrderAdmin)

Your admin area will now display the MultipleChoiceListFilter. It looks a lot like the
SimpleListFilter, except there is now an additional link next to each choice. Use these
links to include or exclude the choice from the results. You can mix and match any
combination you like.

.. image:: https://raw.githubusercontent.com/ctxis/django-admin-multiple-choice-list-filter/master/django-admin-multiple-choice-list-filter.png

You can override the default template in one of two ways.

1. Override the template: https://docs.djangoproject.com/en/2.0/howto/overriding-templates/.
   The default template location is ``django_admin_multiple_choice_list_filter/filter.html``
2. Set the template name in your subclass of MultipleChoiceListFilter, e.g.::

  # shop/admin.py
  ...

  class StatusListFilter(MultipleChoiceListFilter):
      template = 'path/to/your/template.html'
      ...
