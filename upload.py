from internetarchive import upload

md = {'collection': 'test_collection', 'title': 'American Psycho', 'mediatype': 'movies'}

r = upload('<identifier>', files=['foo.txt', 'AmericanPsycho.mov'], metadata=md)

r[0].status_code
