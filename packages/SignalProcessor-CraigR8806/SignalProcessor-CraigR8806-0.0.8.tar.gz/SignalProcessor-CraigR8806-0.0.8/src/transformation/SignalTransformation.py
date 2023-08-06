from abc import ABC, abstractmethod


class SignalTransformation(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def transform(self, signal):
        pass