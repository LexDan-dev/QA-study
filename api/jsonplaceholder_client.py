import requests
from requests import Session

# --- Константы: URL и таймаут---
BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10  # seconds


def get_post(session: Session, post_id: int) -> dict:
    """Получить пост по id. Возвращает dict или бросает исключение."""
    url = f"{BASE_URL}/posts/{post_id}"
    response = session.get(url, timeout=TIMEOUT)
    response.raise_for_status()  # 4xx/5xx -> HTTPError
    return response.json()


def create_post(session: Session, title: str, body: str, user_id: int) -> dict:
    """Создать пост. Бросает понятные ошибки при таймауте/HTTP-ошибке."""
    url = f"{BASE_URL}/posts"
    payload = {"title": title, "body": body, "userId": user_id}
    try:
        response = session.post(url, json=payload, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Сервер не ответил за {TIMEOUT} с") from None
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            raise ValueError("Некорректные данные поста") from e
        raise  # остальные HTTP-ошибки пробрасываем как есть
