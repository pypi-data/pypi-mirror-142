import unittest

from emailrouter import FilterRegistry, InvalidConfigException


class TestFilters(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = FilterRegistry()

    def test_true(self):
        f = self.registry.create_object({
            'type': 'true',
        })
        self.assertTrue(f(' '))

        f = self.registry.create_object(None)
        self.assertTrue(f(''))

    def test_false(self):
        f = self.registry.create_object({
            'type': 'false',
        })
        self.assertFalse(f(' '))

    def test_equal(self):
        f = self.registry.create_object({
            'type': 'equal',
            'field': None,
            'value': 'value',
        })
        self.assertTrue(f('value'))
        self.assertFalse(f('VALUe'))
        self.assertFalse(f('value2'))

    def test_iequal(self):
        f = self.registry.create_object({
            'type': 'iequal',
            'field': None,
            'value': 'value',
        })
        self.assertTrue(f('value'))
        self.assertTrue(f('ValuE'))
        self.assertFalse(f('vvalue'))

    def test_regex(self):
        f = self.registry.create_object({
            'type': 'regex',
            'field': None,
            'value': r'a.*@gmail\.com',
        })
        self.assertTrue(f('a.@gmail.com'))
        self.assertTrue(f('abbbb@gmail.com'))
        self.assertTrue(f('aBBB@gmail.com'))
        self.assertFalse(f('aBBB@GMAIL.com'))
        self.assertFalse(f('ba@gmail.com'))
        self.assertFalse(f('a@gmail\\.com'))

    def test_iregex(self):
        f = self.registry.create_object({
            'type': 'iregex',
            'field': None,
            'value': r'a.*@gmail\.com',
        })
        self.assertTrue(f('abbbb@gmail.com'))
        self.assertTrue(f('aBBB@gmail.com'))
        self.assertTrue(f('aBBB@GMAIL.com'))
        self.assertFalse(f('ba@gmail.com'))

    def test_substring(self):
        f = self.registry.create_object({
            'type': 'substring',
            'field': None,
            'value': 'abcdef',
        })
        self.assertTrue(f('abcdef'))
        self.assertTrue(f('wwabcdefgg'))
        self.assertTrue(f('aaaabcdeffff'))
        self.assertFalse(f('aaaabcdeFfff'))
        self.assertFalse(f('wwabcdegg'))

    def test_isubstring(self):
        f = self.registry.create_object({
            'type': 'isubstring',
            'field': None,
            'value': 'abcdEF',
        })
        self.assertTrue(f('abcdef'))
        self.assertTrue(f('aaaabcdeffff'))
        self.assertTrue(f('aaaabcdeFfff'))
        self.assertFalse(f('wwabcdegg'))

    def test_startswith(self):
        f = self.registry.create_object({
            'type': 'startswith',
            'field': None,
            'value': 'ab',
        })
        self.assertTrue(f('abcd'))
        self.assertFalse(f('aBab'))

    def test_istartswith(self):
        f = self.registry.create_object({
            'type': 'istartswith',
            'field': None,
            'value': 'ab',
        })
        self.assertTrue(f('abcd'))
        self.assertTrue(f('aBab'))
        self.assertFalse(f('aab'))

    def test_endswith(self):
        f = self.registry.create_object({
            'type': 'endswith',
            'field': None,
            'value': 'cd',
        })
        self.assertTrue(f('abcd'))
        self.assertFalse(f('cdcD'))

    def test_iendswith(self):
        f = self.registry.create_object({
            'type': 'iendswith',
            'field': None,
            'value': 'cd',
        })
        self.assertTrue(f('abcd'))
        self.assertTrue(f('cdcD'))
        self.assertFalse(f('cdcddc'))

    def test_length(self):
        f = self.registry.create_object({
            'type': 'length',
            'field': None,
            'value': 2,
        })
        self.assertTrue(f('aa'))
        self.assertTrue(f('=]'))
        self.assertFalse(f('"'))

    def test_listany(self):
        f = self.registry.create_object({
            'type': 'listany',
            'field': None,
            'value': 'cd',
            'condition': 'iequal',
        })
        self.assertTrue(f(['a', 'b', 'cd']))
        self.assertTrue(f(['a', 'cD', 'b']))
        self.assertFalse(f(['a', 'cdd', 'b']))

    def test_listall(self):
        f = self.registry.create_object({
            'type': 'listall',
            'field': None,
            'value': '@hotmail.com',
            'condition': 'substring',
        })
        self.assertTrue(f(['@hotmail.com', '@hotmail.comaa', 'aa@hotmail.com.']))
        self.assertTrue(f(['@hotmail.com@hotmail.com']))
        self.assertFalse(f(['@hotmail.com', 'cdd']))

    def test_any(self):
        f = self.registry.create_object({
            'type': 'any',
            'conditions': [
                {
                    'type': 'equal',
                    'field': None,
                    'value': 'p',
                },
                {
                    'type': 'regex',
                    'field': None,
                    'value': '.*aa(.*)',
                },
            ],
        })
        self.assertTrue(f('p'))
        self.assertTrue(f('aap'))
        self.assertTrue(f('paoskaaa'))
        self.assertFalse(f('pppp'))

    def test_all(self):
        f = self.registry.create_object({
            'type': 'all',
            'conditions': [
                {
                    'type': 'istartswith',
                    'field': None,
                    'value': 'p',
                },
                {
                    'type': 'iregex',
                    'field': None,
                    'value': '.*aa(.*)',
                },
            ],
        })
        self.assertTrue(f('paoskaaa'))
        self.assertFalse(f('p'))
        self.assertFalse(f('aap'))
        self.assertFalse(f('pppp'))

    def test_not(self):
        f = self.registry.create_object({
            'type': 'not',
            'condition': {
                'type': 'equal',
                'field': None,
                'value': 'llll',
            },
        })
        self.assertTrue(f('lll'))
        self.assertFalse(f('llll'))

    def test_invalid(self):
        with self.assertRaises(InvalidConfigException):
            self.registry.create_object({'type': 'aaa'})
