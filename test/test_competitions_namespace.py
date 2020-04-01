from .test_setup import Setup
import json

class TestCompetitionsNamespace(Setup):

    def test_get_empty_competitions_success(self):
        response = self.client.get('/api/competitions/')
        self.assertEqual(response.status_code,200)
        self.assertTrue(len(response.json) is 0)

    def test_post_competition_success(self):
        data  = {'name':'team'}
        response = self.client.post('/api/competitions/', data = json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('name' in response.json.keys())
        self.assertEqual(response.json['name'], data['name'])