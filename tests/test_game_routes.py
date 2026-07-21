import pytest


class TestGameList:
    def test_game_list_requires_login(self, client):
        resp = client.get('/games/')
        assert resp.status_code == 302
        assert '/auth/login' in resp.headers['Location']

    def test_game_list_loads(self, logged_in_client):
        resp = logged_in_client.get('/games/')
        assert resp.status_code == 200


class TestGamePages:
    def test_word_scramble_page(self, logged_in_client):
        resp = logged_in_client.get('/games/word-scramble')
        assert resp.status_code == 200

    def test_hangman_page(self, logged_in_client):
        resp = logged_in_client.get('/games/hangman')
        assert resp.status_code == 200

    def test_memory_page(self, logged_in_client):
        resp = logged_in_client.get('/games/memory')
        assert resp.status_code == 200

    def test_fill_gaps_page(self, logged_in_client):
        resp = logged_in_client.get('/games/fill-gaps')
        assert resp.status_code == 200

    def test_quick_quiz_page(self, logged_in_client):
        resp = logged_in_client.get('/games/quick-quiz')
        assert resp.status_code == 200

    def test_speed_typing_page(self, logged_in_client):
        resp = logged_in_client.get('/games/speed-typing')
        assert resp.status_code == 200


class TestGameAuthRequired:
    def test_word_scramble_requires_login(self, client):
        resp = client.get('/games/word-scramble')
        assert resp.status_code == 302
        assert '/auth/login' in resp.headers['Location']

    def test_hangman_requires_login(self, client):
        resp = client.get('/games/hangman')
        assert resp.status_code == 302
        assert '/auth/login' in resp.headers['Location']
