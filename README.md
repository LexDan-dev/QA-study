# QA-study

Учебный проект по автотестам на Python (pytest).

## Структура

- `tests/` — тесты
- `pages/` — Page Objects (POM): `BasePage`, `LoginPage`
- `ui/` — UI-тесты (появятся на Неделе 4)
- `api/` — API-тесты (появятся на Неделе 6)
- `study_cases/` — учебные упражнения (классы, циклы, функции)
- `conftest.py` — общие фикстуры pytest
- `pytest.ini` — конфигурация pytest (опции, маркеры)
- `requirements.txt` — зависимости
- `.env.example` — шаблон переменных окружения

## Запуск

```bash
# 1. клонировать
git clone https://github.com/LexDan-dev/QA-study.git
cd QA-study

# 2. создать и активировать виртуальное окружение
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. установить зависимости
pip install -r requirements.txt

# 4. запустить тесты
pytest
```

## Переменные окружения

Скопируй `.env.example` в `.env` и подставь свои значения:

```bash
cp .env.example .env
```

| Переменная | Назначение |
|---|---|
| `BASE_URL` | базовый адрес тестируемого сайта |
| `LOGIN` | логин для тестов |
| `PASSWORD` | пароль для тестов |
| `GH_USER` | логин github.com для UI-теста логина (позитив) |
| `GH_PASS` | пароль github.com для UI-теста логина (позитив) |

Файл `.env` в `.gitignore` — секреты в репозиторий не попадают.

## Маркеры

```bash
pytest -m smoke     # быстрые проверки
pytest -m ui        # UI-тесты
pytest -m api       # API-тесты
pytest -m "not ui"  # всё, кроме UI (без браузера)
```

## UI-тесты (Playwright)

Один раз скачать браузер:

```bash
playwright install chromium
```

Запуск:

```bash
pytest -m ui               # только UI-тесты
pytest tests/ui            # папка UI
pytest tests/ui --headed   # видеть окно браузера
```

Логин-тесты:

- **позитив** (`test_login_success`) — на **saucedemo.com** (тест-стенд, публичные креды):
  вход валидными → приёмка «признак входа»: URL содержит `/inventory` **и** видно юзер-меню.
  Позитивный поток гоняют против тест-стенда, а не прода.
- **негатив** (`test_login_fail`) — на **github.com**: неверные креды → контейнер ошибки
  (ждём через `expect`). Нюанс: логин **без подчёркиваний** (`Lexar996`) — иначе клиентская
  валидация github отключает поле пароля. Урок: тестовые данные влияют на поведение UI.
- **github-позитив** (`test_github_login_success`) — `skipif` без `GH_USER`/`GH_PASS`: реальный
  вход на github **не автоматизируем** (2FA/бот-защита/ToS), поэтому по умолчанию **скипается**.
