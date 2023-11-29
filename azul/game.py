class Game:
    _isGameEnd: bool = False
    
    def setEnd(self) -> None:
        self._isGameEnd = True