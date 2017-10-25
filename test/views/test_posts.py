import json
import unittest

import api


class APIBaseCase(unittest.TestCase):
    def setUp(self):
        self.app = api.api.test_client()

    @classmethod
    def setUpClass(cls):
        api.api.testing = True
        # Create the default user.
        cursor = api.db.cursor()
        cursor.execute("""insert into Users (username, password, nickname, user_level) values ('jyp', 'jyp', 'jyp', 'admin');""")
        cursor.close()

    @classmethod
    def tearDownClass(cls):
        cursor = api.db.cursor()
        cursor.execute("""DELETE FROM Users WHERE username = 'jyp';""")
        cursor.close()
        # TODO: before adding new test files (test_users.py) you should
        # implement deleting the test user above ^^ so that all other
        # files start from a clean state. Alternatively, you could
        # do something like delete all things from all tables here. Truncate?
        
    def test_posts_GET(self):
        response = self.app.get('/posts')
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.get_data().decode())
        self.assertEqual(response_json, [])

    def test_posts_GET_one(self):
        response = self.app.post('/posts', data=json.dumps({ 'title': 'test', 'content': 'test content'}),
                                 content_type='application/json')
        json_response = json.loads(response.get_data().decode())
        post_id = json_response['id']
        self.assertEqual(json_response['title'], 'test')
        self.assertEqual(json_response['content'], 'test content')

        response = self.app.get('/posts/{}'.format(json_response['id']))
        json_response = json.loads(response.get_data().decode())
        self.assertEqual(json_response['title'], 'test')
        self.assertEqual(json_response['content'], 'test content')

        self.app.delete('/posts/{}'.format(json_response['id']))
        
    def test_posts_PUT(self):
        pass

    def test_posts_DELETE(self):
        pass

    def test_posts_POST(self):
        response = self.app.post('/posts', data=json.dumps({ 'title': 'test', 'content': 'test content' }), content_type='application/json')
        json_response = json.loads(response.get_data().decode())
        post_id = json_response['id']
        self.assertEqual(json_response['title'], 'test')
        self.assertEqual(json_response['content'], 'test content')

        # Test that the post shows up in the list of all posts.
        response = self.app.get('/posts')
        json_response = json.loads(response.get_data().decode())
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['id'], post_id)

        # Clean up the post for future tests.
        self.app.delete('/posts/{}'.format(json_response[0]['id']))
