import pytest


@pytest.fixture
def open_resource():
    print("\n[OPEN] открываю ресурс")
    resource = {"status": "open"}
    yield resource
    print("\n[CLOSE] закрываю ресурс")
    resource["status"] = "closed"


def test_uses_resource(open_resource):
    print("\n[TEST] использую ресурс")
    assert open_resource["status"] == "open"


@pytest.fixture(autouse=True)
def before_each():
    print("\n[autouse = 4] выполняюсь автоматически перед каждым тестом")


@pytest.fixture(scope="module")
def shared_module_resource():
    print("\n[SETUP = 1] создаю ресурс — должно быть ОДИН раз на модуль")
    return {"value": 1}


def test_general_fixture(general_fixture):
    assert general_fixture == "фикстура из conftest.py"


def test_module_one(shared_module_resource):
    assert shared_module_resource["value"] == 1


def test_module_two(shared_module_resource):
    assert shared_module_resource["value"] == 1


@pytest.fixture(scope="function")
def shared_function_resource():
    print("\n[SETUP = 2] создаю ресурс — должно быть ДВА раза на модуль")
    return {"value": 1}


def test_function_one(shared_function_resource):
    assert shared_function_resource["value"] == 1


def test_function_two(shared_function_resource):
    assert shared_function_resource["value"] == 1
