from src.usecase.validation_usecase import ValidationUseCase


def test_applying_model_return_false() -> None:
    data = "TEST"

    validation_use_case = ValidationUseCase()

    assert validation_use_case.validate(data=data) is True
