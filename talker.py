import datetime

import requests

from api.data import posts

def parse_time(t):
    return datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%S")

r = requests.get('http://localhost:5000/posts')
post_array = r.json()
print('This is post array', post_array)
sorted_array = sorted(post_array, key=lambda post: parse_time(post['updated']))
print('This is sorted_array', sorted_array)

for i in range(5):
    nth_post = i + 1
    post_dictionary = {}
    post_dictionary['title'] = 'Title %s' % nth_post
    post_dictionary['content'] = 'Content %s' % nth_post
    print('This is post_dictionary', post_dictionary)
    post = requests.post('http://localhost:5000/posts', json=post_dictionary)
    print('This post has been created:', post)
