"""Enumerated utilities"""
from enum import Enum, unique
from typing import Optional, Union


class SkydlEnum(str, Enum):
    """Type of any enumerator with allowed comparison to string invariant to cases."""

    @classmethod
    def from_str(cls, value: str) -> Optional["SkydlEnum"]:
        statuses = [status for status in dir(cls) if not status.startswith("_")]
        for st in statuses:
            if st.lower() == value.lower():
                return getattr(cls, st)
        return None

    def __eq__(self, other: Union[str, Enum]) -> bool:
        other = other.value if isinstance(other, Enum) else str(other)
        return self.value.lower() == other.lower()

    def __hash__(self) -> int:
        # re-enable hashtable so it can be used as a dict key or in a set
        # example: set(LightningEnum)
        return hash(self.value.lower())


@unique
class TrainPhaseEnum(SkydlEnum):
    """
    fit、validate、test、predict、tune
    """
    Fit = 'fit'  # fit phase
    Validate = 'validate'  # validate phase
    Test = 'test'  # test phase(i.e. evaluation phase)
    Predict = 'predict'  # predict model
    Tune = "tune"  # tune model


if __name__ == '__main__':
    print(f"TrainPhaseEnum.from_str('Fit')==TrainPhaseEnum.Train? {TrainPhaseEnum.from_str('Fit') == TrainPhaseEnum.Fit}")
    print(f"TrainPhaseEnum.Fit=='fit'? {TrainPhaseEnum.Fit == 'fit'}")
    print(f"TrainPhaseEnum.Fit==TrainPhaseEnum.Fit? {TrainPhaseEnum.Fit == TrainPhaseEnum.Fit}")


