import pytest

from api.jsonplaceholder_client import BASE_URL, TIMEOUT, get_post
from api.models import Post

pytestmark = pytest.mark.api  # все тесты файла — маркер api


def test_get_post_validates_with_pydantic(session):
    data = get_post(session, 1)
    post = Post.model_validate(data)
    assert post.id == 1


def test_get_posts_by_user_id(session):
    response = session.get(f"{BASE_URL}/posts", params={"userId": 1}, timeout=TIMEOUT)
    response.raise_for_status()
    posts = response.json()
    assert len(posts) > 0
    for item in posts:
        assert Post.model_validate(item).userId == 1


def test_create_post_returns_201_and_validates(session):
    payload = {"title": "Мой пост", "body": "текст", "userId": 1}
    response = session.post(f"{BASE_URL}/posts", json=payload, timeout=TIMEOUT)
    assert response.status_code == 201
    post = Post.model_validate(response.json())
    assert post.title == "Мой пост"


def test_delete_post_returns_200_or_204(session):
    response = session.delete(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert response.status_code in (200, 204)
