from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class DirectSort(Strategy):
    def execute(self, data):
        return data.sort()


class ReverseSort(Strategy):
    def execute(self, data):
        return data.sort(reverse=True)


class Context:
    def __init__(self, dataset, strategy):
        self._strategy = strategy
        self.dataset = dataset

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def find_first(self):
        self._strategy.execute(self.dataset)
        return self.dataset[0]


if __name__ == '__main__':
    ds = [5, 1, 9]
    c = Context(ds, DirectSort())
    print(c.find_first())
    c.strategy = ReverseSort()
    print(c.find_first())