from interfaces import ObserverInterface

class GameObserver:
    def __init__(self) -> None:
        pass

    def notifyEverybody(state:str) -> None:
        ObserverInterface.notify(state)