from django.contrib import admin


class MultipleChoiceListFilter(admin.SimpleListFilter):
    template = 'django_admin_multiple_choice_list_filter/filter.html'

    def lookups(self, request, model_admin):
        """
        Must be overridden to return a list of tuples (value, verbose value)
        """
        raise NotImplementedError(
            'The MultipleChoiceListFilter.lookups() method must be overridden to '
            'return a list of tuples (value, verbose value).'
        )

    def queryset(self, request, queryset):
        if request.GET.get(self.parameter_name):
            kwargs = {self.parameter_name: request.GET[self.parameter_name].split(',')}
            queryset = queryset.filter(**kwargs).distinct()
        return queryset

    def value_as_list(self):
        return self.value().split(',') if self.value() else []

    def choices(self, changelist):

        def amend_query_string(include=None, exclude=None):
            selections = self.value_as_list()
            if include and include not in selections:
                selections.append(include)
            if exclude and exclude in selections:
                selections.remove(exclude)
            if selections:
                csv = ','.join(selections)
                return changelist.get_query_string({self.parameter_name: csv})
            else:
                return changelist.get_query_string(remove=[self.parameter_name])

        yield {
            'selected': self.value() is None,
            'query_string': changelist.get_query_string(remove=[self.parameter_name]),
            'display': 'All',
            'reset': True,
        }
        for lookup, title in self.lookup_choices:
            yield {
                'selected': str(lookup) in self.value_as_list(),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}),
                'include_query_string': amend_query_string(include=str(lookup)),
                'exclude_query_string': amend_query_string(exclude=str(lookup)),
                'display': title,
            }
