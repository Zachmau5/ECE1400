#!/usr/bin/python3
import sys

# library
import hw05_lib as h5
from hw05_lib import Resistor


def main():
    resistor_input = input("Enter a resistor: ")

    try:
        resistor = Resistor(resistor_input)

    except:
        print(f"Resistor must start with an R: {resistor_input}")
        sys.exit(1)

    resistor.print()
    voltage_input = input("Enter a voltage: ")

    try:
        voltage = h5.decodeValue(voltage_input)

    except:
        print("Invalid value")
        sys.exit(1)

    current = resistor.current(voltage)
    print(f"I = {current:.2e}")


if __name__ == "__main__":
    main()
