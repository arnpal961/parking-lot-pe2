import argparse
from parking_lot import ParkingLot

def main():
    parser = argparse.ArgumentParser(description="Vehichle Ticket booking System")
    parser.add_argument('input_file', type=str, help="Absolute path of the input file")

    args = parser.parse_args()
    fpath = args.input_file

    parking_lot = ParkingLot()

    with open(fpath, 'r') as fd:
        commands = fd.readlines()
        for command in commands:
            parking_lot.execute_command(command.strip())

# Run as a commandline function
main()
