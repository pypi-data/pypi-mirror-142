# ua
User-Agent parsing and creation

## Installation
```console
pip install ua
```

## Usage
```python
>>> import ua
```

### Parsing
```python
>>> user_agent = ua.parse('Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0')
>>>
>>> user_agent
UserAgent(
    products=[
        Product(name='Mozilla', version='5.0', comments=['X11', 'Linux x86_64', 'rv:88.0']),
        Product(name='Gecko', version='20100101', comments=[]),
        Product(name='Firefox', version='88.0', comments=[])
    ]
)
>>>
>>> str(user_agent)
'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
```

### Creation
```python
>>> user_agent = ua.UserAgent(
    products=[
        ua.Product(
            name='SomeProduct',
            version='1.0',
            comments=['SomeComment']
        )
    ]
)
>>>
>>> str(user_agent)
'SomeProduct/1.0 (SomeComment)'
```

## References
* [User agent - Wikipedia](https://en.wikipedia.org/wiki/User_agent)
* [User-Agent - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)
* [RFC 7231 - Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content](https://datatracker.ietf.org/doc/html/rfc7231#section-5.5.3)