import pytest

from src.usecase.validation_usecase import ValidationUseCase
from src.user_interface.http.exception_handlers import ValidationException

validation_use_case = ValidationUseCase()


def test_applied_model_must_return_true() -> None:
    assert validation_use_case.validate(data="string_to_validate") is True
    assert validation_use_case.validate(data="another_string_to_validate") is True
    assert validation_use_case.validate(data="2131") is True


def test_empty_input_string_must_return_false() -> None:
    assert validation_use_case.validate(data="") is False


def test_int_input() -> None:
    with pytest.raises(ValidationException):
        validation_use_case.validate(data=312)


def test_bool_input() -> None:
    with pytest.raises(ValidationException):
        validation_use_case.validate(data=False)


def test_none_input() -> None:
    with pytest.raises(ValidationException):
        validation_use_case.validate(data=None)
