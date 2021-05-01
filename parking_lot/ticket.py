
class Ticket:
    """
    Ticket for a parking system
    """

    def __init__(self, slot_no: int, allocated: bool = False) -> None:
        self.slot_no = slot_no
        self.allocated = allocated

    def allocate(self, reg_no: str, driver_age: str) -> None:
        self._reg_no = reg_no
        self._driver_age = driver_age
        self.allocated = True

    def deallocate(self) -> None:
        self.allocated = False
        delattr(self, '_reg_no')
        delattr(self, '_driver_age')

    def get_vehicle_registration_no(self) -> str:
        if self.allocated:
            return self._reg_no
        return "ALLOCATE_FIRST"

    def get_driver_age(self) -> str:
        if self.allocated:
            return self._driver_age
        return "ALLOCATE_FIRST"

    def __repr__(self) -> str:
        return "<%s(slot_no=%s, allocated=%s)>" % (self.__class__.__name__, self.slot_no, self.allocated)
