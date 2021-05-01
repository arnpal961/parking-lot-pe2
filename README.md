# parking-lot-pe2

## Using this repository

    git clone  git@github.com:arnpal961/parking-lot-pe2.git
    cd parking-lot-pe2
    python3.8 -m venv venv
    source venv/bin/activate
    python -m pip install --upgrade build
    python -m build
    pip install dist/parking_lot-0.0.0-py3-none-any.whl

## Running the tests

    # activate the virtual environment
    pip install -r requirements.txt
    pytest tests/tests_parking.py

## Giving Input

    # activate the virtual environment
    python -m parking_lot <ABSOLUTE PATH TO INPUT FILE>

## Code Structure

    parking_lot
    ├── __init__.py
    ├── __main__.py  # Main entry point for the application
    ├── parking_lot.py  # contains the ParkingLot class
    └── ticket.py  # contains the Ticket Class

## Description

    Every method in ParkingLot with a command decorator represents a command.
    The register decorater over the ParkingLot class sets the command name as
    attribute pointing to the methods with same command decorater.

    To add any new commands need to add an method in ParkingLot class with the
    command decorater. And if it takes multiple arguments then that case must be
    handled from the main() function in __main__.py

    Ticket - Can be issued by Parking Lot

    ParkingLot - with the capacity given, it will create same number un-allocated tickets for each slot number.

    Park command will mark the first available un-allocated ticket as allocated
    and issue it to the user.

    Leave command will take the slot number and releases the ticket by setting it un-allocated.

    Other commands reprents some queries over the data stored in  the ParkingLot instance.

    Test Cases are defined in the methods of TestParkingLot class in tests/test_parking_lot.py
    Total 9 cases has been covered but there we can cover more tests.

    All outputs of the instructions will be printed on the console.

## Improvements

    More validations must be added. There should be a check that for any
    input file the first command must be Create_parking_lot otherwise it will
    throw an error message.

    More edge cases must be handled.
