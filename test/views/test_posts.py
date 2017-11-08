import json
import unittest

import bcrypt

import api


class APIBaseCase(unittest.TestCase):
    def setUp(self):
        self.app = api.api.test_client()
        self.app.post('/admin/login',
                      data=json.dumps({'username': 'jyp', 'password': 'jyp'}),
                      content_type='application/json')

    def tearDown(self):
        self.app.get('/admin/logout')

    @classmethod
    def setUpClass(cls):
        api.api.testing = True
        # Create the default user.
        cursor = api.db.cursor()
        cursor.execute(
            "insert into Users (username, password, nickname, user_level) "
            "values ('jyp', %s, 'jyp', 'admin');", (bcrypt.hashpw(b'jyp', bcrypt.gensalt()),))
        cursor.close()

    @classmethod
    def tearDownClass(cls):
        cursor = api.db.cursor()
        cursor.execute("SELECT id FROM Users WHERE username='jyp';")
        user_id = cursor.fetchone()[0]
        print(user_id)
        cursor.execute("DELETE From Posts WHERE author_id=%s", (user_id,))
        api.db.commit()
        cursor.execute("DELETE From Sessions WHERE user_id=%s", (user_id,))
        api.db.commit()
        cursor.execute("DELETE FROM Users WHERE username = 'jyp';")
        api.db.commit()
        cursor.close()

    def test_posts_get(self):
        response = self.app.get('/posts')
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.get_data().decode())
        self.assertEqual(response_json, [])

    def test_posts_get_one(self):
        response = self.app.post('/posts',
                                 data=json.dumps({'title': 'test', 'content': 'test content'}),
                                 content_type='application/json')
        json_response = json.loads(response.get_data().decode())
        self.assertEqual(json_response['title'], 'test')
        self.assertEqual(json_response['content'], 'test content')

        response = self.app.get('/posts/{}'.format(json_response['id']))
        json_response = json.loads(response.get_data().decode())
        self.assertEqual(json_response['title'], 'test')
        self.assertEqual(json_response['content'], 'test content')
        self.app.delete('/posts/{}'.format(json_response['id']))
    def test_posts_put(self):
        pass

    def test_posts_delete(self):
        pass

    def test_posts_post(self):
        response = self.app.post('/posts',
                                 data=json.dumps({'title': 'test', 'content': 'test content'}),
                                 content_type='application/json')
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
