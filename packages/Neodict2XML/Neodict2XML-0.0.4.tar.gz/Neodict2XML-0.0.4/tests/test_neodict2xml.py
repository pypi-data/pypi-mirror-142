from xml.etree.ElementTree import Element, SubElement

from neodict2xml import dict2xml

def test_from_dict():
    # Given
    test_dict = {
        'test': {
            'plop': ({'attr': 'brrr'}, 'lol'),
            'lol': [
                'hello',
                'world'
            ],
            'deep': {
                'deeper': 1
            },
            'test2': [
                { 'foo': 'bar' },
                ( { 'id': 2 }, { 'foo': 'rab' } )
            ],
            'test3': ( { 'class': 'foo.Bar' }, ),
            'test4': None,
            'test5': {},
            'test6': ( { 'class': 'foo.Bar' }, None ),
            'test7': ( { 'class': 'foo.Bar' }, {} )
        }
    }

    # When
    xml = dict2xml.from_dict(test_dict)

    # Then
    top = Element('test')
    c1 = SubElement(top, 'plop')
    c1.set('attr', 'brrr')
    c1.text = 'lol'
    c21 = SubElement(top, 'lol')
    c21.text = 'hello'
    c22 = SubElement(top, 'lol')
    c22.text = 'world'
    c3 = SubElement(top, 'deep')
    c31 = SubElement(c3, 'deeper')
    c31.text = '1'
    c41 = SubElement(top, 'test2')
    c411 = SubElement(c41, 'foo')
    c411.text = 'bar'
    c42 = SubElement(top, 'test2', {'id': '2'})
    c421 = SubElement(c42, 'foo')
    c421.text = 'rab'
    SubElement(top, 'test3', {'class': 'foo.Bar'})
    SubElement(top, 'test4')
    SubElement(top, 'test5')
    SubElement(top, 'test6', {'class': 'foo.Bar'})
    SubElement(top, 'test7', {'class': 'foo.Bar'})
    print(dict2xml.prettify(top))
    print(dict2xml.prettify(xml))
    assert dict2xml.prettify(top) == dict2xml.prettify(xml)

def test_dict_to_xml_does_not_change_dict():
    # Given
    test_dict = {
        'test': (
            {'attr': 'brrr'},
            {'plop': 'lol'}
        )
    }

    # When
    xml = dict2xml.from_dict(test_dict)
    xml = dict2xml.from_dict(test_dict)

    # Then
    top = Element('test')
    top.set('attr', 'brrr')
    c1 = SubElement(top, 'plop')
    c1.text = 'lol'
    print(dict2xml.prettify(top))
    print(dict2xml.prettify(xml))
    assert dict2xml.prettify(top) == dict2xml.prettify(xml)

def test_from_xml():
    # Given
    test_xml = '''
    <test>
        <plop attr="brrr">lol</plop>
        <lol>hello</lol>
        <lol>world</lol>
        <lol2>hello</lol2>
        <lol2>world</lol2>
        <lol2>foo</lol2>
        <lol2>bar</lol2>
        <deep>
            <deeper>
                1
            </deeper>
        </deep>
        <test2>
            <foo>bar</foo>
        </test2>
        <test2 id="2">
            <foo>bar</foo>
        </test2>
        <test3 class="foo.Bar" />
        <test4 />
    </test>
    '''

    # When
    dict_ = dict2xml.from_xml(test_xml)

    # Then
    res_dict = {
        'test': {
            'plop': ({'attr': 'brrr'}, 'lol'),
            'lol': [
                'hello',
                'world'
            ],
            'lol2': [
                'hello',
                'world',
                'foo',
                'bar'
            ],
            'deep': {
                'deeper': '1'
            },
            'test2': [
                { 'foo': 'bar' },
                ( { 'id': '2' }, { 'foo': 'bar' } )
            ],
            'test3': ( { 'class': 'foo.Bar' }, ),
            'test4': None
        }
    }
    assert dict_ == res_dict
