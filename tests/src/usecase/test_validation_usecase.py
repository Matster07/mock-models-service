import pytest

from src.usecase.validation.validation_usecase import ValidationUseCase
from src.user_interface.http.exception_handlers import ValidationException

validation_use_case = ValidationUseCase()


def test_applied_model_must_return_true() -> None:
    """
    Тесты при проверке валидных данных, результат должен быть True.
    """

    assert validation_use_case.validate(data="string_to_validate") is True
    assert validation_use_case.validate(data="another_string_to_validate") is True
    assert validation_use_case.validate(data="2131") is True


def test_empty_input_string_must_return_false() -> None:
    """
    Тест при проверке валидных данных, результат должен быть False.
    """

    assert validation_use_case.validate(data="") is False


def test_int_input() -> None:
    """
    Тесты на выбрасывание исключения при передаче int значения на валидацию.
    """

    with pytest.raises(ValidationException):
        validation_use_case.validate(data=312)


def test_bool_input() -> None:
    """
    Тесты на выбрасывание исключения при передаче bool значения.
    """

    with pytest.raises(ValidationException):
        validation_use_case.validate(data=False)


def test_none_input() -> None:
    """
    Тест на выбрасывание исключения при передаче пустого значения.
    """

    with pytest.raises(ValidationException):
        validation_use_case.validate(data=None)
