class Car:
    def __init__(self) -> None:
        self.carname = None
        self.carhp = None
        self.carprice = None
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        pass

    def __getattribute__(self, __name: str) -> Any:
        pass

    