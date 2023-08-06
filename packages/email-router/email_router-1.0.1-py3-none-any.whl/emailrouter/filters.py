import re

from emailrouter.utils import ArgumentMixin, Base as Filter, Registry, load_module_from_file


FilterRegistry = Registry()
register_filter = FilterRegistry.register_class


@register_filter('python')
class PythonFilter(ArgumentMixin, Filter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.call_func = load_module_from_file(self.data['file']).check

    def __call__(self, email):
        return self.call_func(email, *self.args, **self.kwargs)


class NonLeafFilter(Filter):
    pass


class MultipleFilter(NonLeafFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subfilters = [self.registry.create_object(f) for f in self.data['conditions']]


class SingleFilter(NonLeafFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subfilter = self.registry.create_object(self.data['condition'])


class LeafFilter(Filter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field = self.process_field(self.data['field'])
        self.value = self.process_value(self.data['value'])

    def field_data(self, data):
        if self.field is None:
            return data
        return getattr(data, self.field)

    @classmethod
    def process_value(cls, value):
        return value

    @classmethod
    def process_field(cls, field):
        assert field in (
            None,
            'message_id',
            'bcc',
            'bcc_names',
            'body',
            'cc',
            'cc_names',
            'recipient_names',
            'recipients',
            'reply_to',
            'reply_to_names',
            'sender_names',
            'senders',
            'subject',
        )
        return field


class CaseInsensitiveMixin:
    @classmethod
    def process_value(cls, value):
        return super().process_value(value).lower()

    def field_data(self, email):
        return super().field_data(email).lower()


@register_filter('true', default=True)
class TrueFilter(Filter):
    def __call__(self, email):
        return True


@register_filter('false')
class FalseFilter(Filter):
    def __call__(self, email):
        return False


@register_filter('any')
class AnyFilter(MultipleFilter):
    def __call__(self, email):
        return any(f(email) for f in self.subfilters)


@register_filter('all')
class AllFilter(MultipleFilter):
    def __call__(self, email):
        return all(f(email) for f in self.subfilters)


@register_filter('not')
class NotFilter(SingleFilter):
    def __call__(self, email):
        return not self.subfilter(email)


@register_filter('equal')
class EqualFilter(LeafFilter):
    def __call__(self, email):
        return self.field_data(email) == self.value


@register_filter('iequal')
class IEqualFilter(CaseInsensitiveMixin, EqualFilter):
    pass


@register_filter('regex')
class RegexFilter(LeafFilter):
    flags = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.re_expr = re.compile(self.value, flags=self.flags)

    def __call__(self, email):
        return self.re_expr.match(self.field_data(email)) is not None


@register_filter('iregex')
class IRegexFilter(RegexFilter):
    flags = re.IGNORECASE


@register_filter('substring')
class SubstringFilter(LeafFilter):
    def __call__(self, email):
        return self.value in self.field_data(email)


@register_filter('isubstring')
class ISubstringFilter(CaseInsensitiveMixin, SubstringFilter):
    pass


@register_filter('startswith')
class StartsWithFilter(LeafFilter):
    def __call__(self, email):
        return self.field_data(email).startswith(self.value)


@register_filter('istartswith')
class IStartsWithFilter(CaseInsensitiveMixin, StartsWithFilter):
    pass


@register_filter('endswith')
class EndsWithFilter(LeafFilter):
    def __call__(self, email):
        return self.field_data(email).endswith(self.value)


@register_filter('iendswith')
class IEndsWithFilter(CaseInsensitiveMixin, EndsWithFilter):
    pass


@register_filter('length')
class LengthFilter(LeafFilter):
    def __call__(self, email):
        return len(self.field_data(email)) == self.value


@register_filter('listany')
class ListAnyFilter(LeafFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subfilter = self.registry.create_object({
            'type': self.data['condition'],
            'field': None,
            'value': self.data['value'],
        })

    def __call__(self, email):
        return any(self.subfilter(data) for data in self.field_data(email))


@register_filter('listall')
class ListAllFilter(LeafFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subfilter = self.registry.create_object({
            'type': self.data['condition'],
            'field': None,
            'value': self.data['value'],
        })

    def __call__(self, email):
        return all(self.subfilter(data) for data in self.field_data(email))
