from functools import wraps
from typing import Any, Union, List, Optional

from parking_lot.ticket import Ticket

# ALL AVAILABLE COMMANDS
PARK = "Park"
LEAVE = "Leave"
CREATE_PARKING_LOT = "Create_parking_lot"
SLOT_NUMBERS_FOR_DRIVER_OF_AGE = "Slot_numbers_for_driver_of_age"
SLOT_NUMBER_FOR_CAR_WITH_NUMBER = "Slot_number_for_car_with_number"
VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE = "Vehicle_registration_number_for_driver_of_age"


# command decorater will be used in methods
# will set the command attribute to the method
def command(name):

    def decorate(func):
        func.command = name
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(self, *args, **kwargs)

        return wrapper
    return decorate


# class decorater checks which method has a command attribute
# and sets the command as attribute to the class pointing the methods
def register(cls):
    cmd_funcs = []
    for _, attr in cls.__dict__.items():
        if callable(attr) and hasattr(attr, 'command'):
            cmd_funcs.append(attr)
    for func in cmd_funcs:
        setattr(cls, func.command, func)
    return cls


@register
class ParkingLot:

    @command(name=CREATE_PARKING_LOT)
    def _create(self, number_of_slots: str) -> None:
        '''Creates required number of slots for a parking lot'''

        self.tickets = {slot_no: Ticket(slot_no) for slot_no in range(1, int(number_of_slots) + 1)}
        print(f"Created parking of {number_of_slots} slots")

    @command(name=PARK)
    def _park(self, reg_no: str, driver_age: str) -> Union[int, str]:
        '''Park a vehicle based on reg_no and driver_age if a slot is available'''

        for slot_no, ticket in self.tickets.items():
            if not ticket.allocated:
                ticket.allocate(reg_no, driver_age)
                print(f'Car with vehicle registration number "{reg_no}" has been parked at slot number {slot_no}')
                return slot_no

        return "NO_PARKING_SLOT_AVAILABLE"

    @command(name=LEAVE)
    def _leave(self, slot_no: str) -> None:
        '''de-allocates a ticket and frees the parking slot'''
        ticket = self.tickets[int(slot_no)]
        reg_no = ticket.get_vehicle_registration_no()
        age = ticket.get_driver_age()
        ticket.deallocate()
        print(f'Slot number {slot_no} vacated, the car with vehicle registration number "{reg_no}" left the space, the driver of the car was of age {age}')

    @command(name=VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE)
    def _get_regs_by_age(self, age: str) -> List[Optional[str]]:
        '''Query for getting vehicle registration number by driver's age'''

        vehicle_registrations = []
        for _, ticket in self.tickets.items():
            if ticket.allocated:
                if ticket.get_driver_age() == age:
                    vehicle_registrations.append(ticket.get_vehicle_registration_no())

        if vehicle_registrations:
            print(*vehicle_registrations)
        else:
            print("No parked car matches the query")
        return vehicle_registrations

    @command(name=SLOT_NUMBERS_FOR_DRIVER_OF_AGE)
    def _get_slots_by_age(self, age: str) -> List[Optional[str]]:
        '''Query for getting slots by drivers age'''

        slots = []
        for slot, ticket in self.tickets.items():
            if ticket.allocated:
                if ticket.get_driver_age() == age:
                    slots.append(slot)
        if slots:
            print(*slots)
        else:
            print("No parked car matches the query")
        return slots

    @command(name=SLOT_NUMBER_FOR_CAR_WITH_NUMBER)
    def _get_slot_by_reg_no(self, reg_no: str) -> Optional[int]:
        '''Query for getting slot by vehicle registration number'''

        for slot, ticket in self.tickets.items():
            if ticket.allocated:
                if ticket.get_vehicle_registration_no() == reg_no:
                    print(slot)
                    return slot
        print("No parked car matches the query")

    def execute_command(self, command: str) -> Any:
        '''Executes a command passed by the input file'''

        cmd_name, *args = command.split(' ')

        if cmd_name == PARK:
            args = args[0], args[2]

        return getattr(self, cmd_name)(*args)
