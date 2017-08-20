import json
import unittest

import api


class APIBaseCase(unittest.TestCase):
    def setUp(self):
        api.api.testing = True
        self.app = api.api.test_client()

        # Create the default user.
        cursor = api.db.cursor()
        cursor.execute("""insert into user (username, password, nickname) values ('jyp', 'jyp', 'jyp');""")
        cursor.close()

    def test_posts_GET(self):
        response = self.app.get('/posts')
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.get_data())
        self.assertEqual(response_json, [])

    def test_posts_POST(self):
        response = self.app.post('/posts', data=json.dumps({ 'title': 'test', 'content': 'test content' }), content_type='application/json')
        json_response = json.loads(response.get_data())
        post_id = json_response['id']
        self.assertEqual(json_response['title'], 'test')
        self.assertEqual(json_response['content'], 'test content')

        # Test that the post shows up in the list of all posts.
        response = self.app.get('/posts')
        json_response = json.loads(response.get_data())
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['id'], post_id)

        # Clean up the post for future tests.
        self.app.delete('/posts/{}'.format(json_response[0]['id']))
