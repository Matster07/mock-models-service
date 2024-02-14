import pytest

from src.usecase.models.model_usecase import ModelUseCase
from src.user_interface.http.exception_handlers import ModelCallException

model_use_case = ModelUseCase()


async def test_calling_model_must_return_true() -> None:
    """
    Тесты при проверке валидных данных должен вернуться результат True.
    """

    assert await model_use_case.execute(query="string_to_validate") is True
    assert await model_use_case.execute(query="another_string_to_validate") is True
    assert await model_use_case.execute(query="2131") is True


async def test_empty_input_query_must_return_false() -> None:
    """
    Тесты при проверке валидных данных должен вернуться результат False.
    """

    assert await model_use_case.execute(query="") is False


async def test_int_input() -> None:
    """
    Тесты на выбрасывание исключения при передаче int значения модели.
    """

    with pytest.raises(ModelCallException):
        await model_use_case.execute(query=312)


async def test_bool_input() -> None:
    """
    Тесты на выбрасывание исключения при передаче bool значения.
    """

    with pytest.raises(ModelCallException):
        await model_use_case.execute(query=False)


async def test_none_input() -> None:
    """
    Тест на выбрасывание исключения при передаче пустого значения.
    """

    with pytest.raises(ModelCallException):
        await model_use_case.execute(query=None)
