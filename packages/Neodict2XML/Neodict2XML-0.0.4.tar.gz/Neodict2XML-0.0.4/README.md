# Neodict2XML

Neomyte's dict to XML converter

<ins>Example:<ins>

```python
>>> from neodict2xml import dict2xml
>>> test_dict = {\
    'test': {\
        'plop': ({'attr': 'brrr'}, 'lol'),\
        'lol': [\
            'hello',\
            'world'\
        ],\
        'deep': {\
            'deeper': 1\
        },\
        'test2': [\
            { 'foo': 'bar' },\
            ( { 'id': 2 }, { 'foo': 'rab' } )\
        ],\
        'test3': ( { 'class': 'foo.Bar' }, )\
        'test4': None,\
        'test5': {},\
        'test6': ( { 'class': 'foo.Bar' }, None ),\
        'test7': ( { 'class': 'foo.Bar' }, {} )\
    }\
}
>>> xml = dict2xml.from_dict(test_dict)
>>> print(dict2xml.prettify(xml))
<?xml version="1.0" ?>
<test>
    <plop attr="brrr">lol</plop>
    <lol>hello</lol>
    <lol>world</lol>
    <deep>
        <deeper>1</deeper>
    </deep>
    <test2>
        <foo>bar</foo>
    </test2>
    <test2 id="2">
        <foo>rab</foo>
    </test2>
    <test3 class="foo.Bar"/>
    <test4/>
    <test5/>
    <test6 class="foo.Bar"/>
    <test7 class="foo.Bar"/>
</test>

```

```python
>>> from neodict2xml import dict2xml
>>> test_xml = test_xml = '''
... <test>
...     <plop attr="brrr">lol</plop>
...     <lol>hello</lol>
...     <lol>world</lol>
...     <lol2>hello</lol2>
...     <lol2>world</lol2>
...     <lol2>foo</lol2>
...     <lol2>bar</lol2>
...     <deep>
...         <deeper>
...             1
...         </deeper>
...     </deep>
...     <test2>
...         <foo>bar</foo>
...     </test2>
...     <test2 id="2">
...         <foo>bar</foo>
...     </test2>
...     <test3 class="foo.Bar" />
...     <test4 />
... </test>
... '''
>>> dict2xml.from_xml(test_xml)
{'test': {'plop': ({'attr': 'brrr'}, 'lol'), 'lol': ['hello', 'world'], 'lol2': ['hello', 'world', 'foo', 'bar'], 'deep': {'deeper': '1'}, 'test2': [{'foo': 'bar'}, ({'id': '2'}, {'foo': 'bar'})], 'test3': ({'class': 'foo.Bar'},), 'test4': None}}
```


# Contributors

 * Emmanuel Pluot (aka. Neomyte)
