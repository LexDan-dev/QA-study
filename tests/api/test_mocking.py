"""6.4 - изоляция от сети: responses vs mocker.patch.

- responses - сетевой stub: перехватывает HTTP на уровне requests-адаптера.
  Реалистично, видно реальный URL/метод/тело. Для интеграционного слоя и
  большинства API-тестов.
- mocker.patch - monkey-patch: подменяет Python-объект (requests.get) внутри
  кода. Настоящего HTTP нет. Когда тестируем функцию, что внутри зовёт
  requests.get, и хотим проверить факт/аргументы вызова.
  Подвох: патчить ТАМ, ГДЕ ИМЯ ИСПОЛЬЗУЕТСЯ, а не где определено.
Оба варианта делают тесты полностью независимыми от интернета.
"""

import pytest
import requests
import responses

from api.jsonplaceholder_client import BASE_URL, TIMEOUT, get_post
from api.models import Post

pytestmark = pytest.mark.api

POST_URL = f"{BASE_URL}/posts/1"


# --- responses: сетевой stub (HTTP перехвачен, реальной сети нет) ---
@responses.activate
def test_get_post_responses_success(session):
    responses.add(
        responses.GET,
        POST_URL,
        json={"userId": 1, "id": 1, "title": "Mocked", "body": "Test"},
        status=200,
    )
    post = Post.model_validate(get_post(session, 1))
    assert post.title == "Mocked"


@responses.activate
def test_get_post_responses_404(session):
    responses.add(responses.GET, POST_URL, status=404)
    with pytest.raises(requests.exceptions.HTTPError):
        get_post(session, 1)


@responses.activate
def test_get_post_responses_500(session):
    responses.add(responses.GET, POST_URL, status=500)
    with pytest.raises(requests.exceptions.HTTPError):
        get_post(session, 1)


# --- mocker.patch: подмена Python-функции requests.get ---
def test_get_post_mocker_patch(mocker):
    fake = mocker.Mock(status_code=200)
    fake.json.return_value = {"userId": 1, "id": 1, "title": "Patched", "body": "x"}
    mock_get = mocker.patch("requests.get", return_value=fake)

    resp = requests.get(POST_URL, timeout=TIMEOUT)
    assert Post.model_validate(resp.json()).title == "Patched"
    mock_get.assert_called_once()
