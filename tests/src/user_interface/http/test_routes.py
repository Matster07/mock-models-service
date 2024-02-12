from fastapi.testclient import TestClient

from src.user_interface.http.app import create_application

client = TestClient(app=create_application())


def test_validation_route_for_int_input_type() -> None:
    """
    Тесты на валидацию входных данных при передаче int значения.
    Также проверяется, что обработчик ошибок отдает ошибку в нужном формате.
    """

    response = client.post(url="/api/v1/text/validate", json={"data": 123})
    assert response.status_code == 422
    assert response.json() == {
        "errors": [
            {
                "msg": "Input should be a valid string",
                "type": "string_type",
                "input": "123"
            }
        ]
    }


def test_validation_route_for_bool_input_type() -> None:
    """
    Тест на валидацию входных данных при передаче bool значения.
    Также проверяется, что обработчик ошибок отдает ошибку в нужном формате.
    """

    response = client.post(url="/api/v1/text/validate", json={"data": False})
    assert response.status_code == 422
    assert response.json() == {
        "errors": [
            {
                "msg": "Input should be a valid string",
                "type": "string_type",
                "input": "False"
            }
        ]
    }


def test_validation_route_for_null_input_type() -> None:
    """
    Тест на валидацию входных данных при передаче null значения.
    Также проверяется, что обработчик ошибок отдает ошибку в нужном формате.
    """

    response = client.post(url="/api/v1/text/validate", json={"data": None})
    assert response.status_code == 422
    assert response.json() == {
        "errors": [
            {
                "msg": "Input should be a valid string",
                "type": "string_type",
                "input": "None"
            }
        ]
    }


def test_validation_route_for_empty_input() -> None:
    """
    Тест на валидацию входных данных при передаче пустого значения.
    Также проверяется, что обработчик ошибок отдает ошибку в нужном формате.
    """

    response = client.post(url="/api/v1/text/validate", json={})
    assert response.status_code == 422
    assert response.json() == {
        "errors": [
            {
                "msg": "Field required",
                "type": "missing",
                "input": "{}"
            }
        ]
    }
