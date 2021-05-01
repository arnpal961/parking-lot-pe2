import pytest
import parking_lot as pl

@pytest.fixture
def parking_lot_fixture_data():
    parking_lot = pl.ParkingLot()
    parking_lot.execute_command('Create_parking_lot 3')
    parking_lot.execute_command('Park KA-01-HH-1234 driver_age 21')
    parking_lot.execute_command('Park PB-01-HH-1234 driver_age 21')
    return parking_lot


class TestParkingLot:

    def test_ticket_allocation(self):
        ticket = pl.Ticket(slot_no=5)
        ticket.allocate('abc', '12')
        assert ticket.allocated is True

    def test_ticket_deallocation(self):
        ticket = pl.Ticket(slot_no=5)
        ticket.allocate('abc', '12')
        ticket.deallocate()
        assert ticket.allocated is False

    def test_create_parking_lot(self):
        parking_lot = pl.ParkingLot()
        parking_lot.execute_command('Create_parking_lot 6')
        assert len(parking_lot.tickets) == 6

    def test_allocation_status_after_creating_parking_lot(self):
        parking_lot = pl.ParkingLot()
        parking_lot.execute_command('Create_parking_lot 6')
        assert all([val.allocated is False for val in parking_lot.tickets.values()])

    def test_ticket_occupancy_after_parking_vehicle(self, parking_lot_fixture_data):
        assert parking_lot_fixture_data.tickets[1].allocated is True and parking_lot_fixture_data.tickets[2].allocated is True and parking_lot_fixture_data.tickets[3].allocated is False


    def test_occupancy_after_leave_vehicle(self, parking_lot_fixture_data):
        parking_lot_fixture_data.execute_command('Leave 2')
        assert parking_lot_fixture_data.tickets[2].allocated is False

    def test_query_get_slot_by_reg_no(self, parking_lot_fixture_data):
        assert parking_lot_fixture_data.execute_command('Slot_number_for_car_with_number PB-01-HH-1234') == 2


    def test_query_get_slots_by_age(self, parking_lot_fixture_data):
        assert parking_lot_fixture_data.execute_command('Slot_numbers_for_driver_of_age 21') == [1, 2]


    def test_quey_get_regs_by_age(self, parking_lot_fixture_data):
        assert parking_lot_fixture_data.execute_command('Vehicle_registration_number_for_driver_of_age 21') == ['KA-01-HH-1234', 'PB-01-HH-1234']
