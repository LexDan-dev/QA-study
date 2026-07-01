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

Файл `.env` в `.gitignore` — секреты в репозиторий не попадают.

## Маркеры

```bash
pytest -m smoke     # быстрые проверки
pytest -m ui        # UI-тесты
pytest -m api       # API-тесты
```
