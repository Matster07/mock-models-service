from src.usecase.validation_usecase import ValidationUseCase


def test_applied_model_must_return_true() -> None:
    data = "TEST"

    validation_use_case = ValidationUseCase()

    assert validation_use_case.validate(data=data) is True