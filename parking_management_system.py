from datetime import datetime
import math

TOTAL_SLOTS = 100
GST_RATE = 18

parking_slots = {}
vehicles = {}

for i in range(1, TOTAL_SLOTS + 1):
    parking_slots[i] = None


def calculate_charge(hours):
    if hours <= 1:
        return 20
    else:
        return 20 + ((hours - 1) * 10)


def show_slots():
    print("\n========== PARKING STATUS ==========")

    for slot, vehicle in parking_slots.items():
        if vehicle is None:
            print(f"Slot {slot}: Available")
        else:
            print(f"Slot {slot}: {vehicle}")

    available = sum(1 for vehicle in parking_slots.values() if vehicle is None)

    print("------------------------------------")
    print(f"Total Slots     : {TOTAL_SLOTS}")
    print(f"Available Slots : {available}")
    print(f"Occupied Slots  : {TOTAL_SLOTS - available}")

    if available == 0:
        print("STATUS: PARKING FULL")
    else:
        print("STATUS: PARKING AVAILABLE")


def find_available_slot():
    for slot, vehicle in parking_slots.items():
        if vehicle is None:
            return slot
    return None


def vehicle_entry():
    vehicle_number = input("\nEnter vehicle number: ").upper()

    if vehicle_number in vehicles:
        print("Vehicle is already parked.")
        return

    slot = find_available_slot()

    if slot is None:
        print("\nParking Full!")
        print("No slots are available.")
        return

    entry_time = datetime.now()

    parking_slots[slot] = vehicle_number

    vehicles[vehicle_number] = {
        "slot": slot,
        "entry_time": entry_time
    }

    print("\nVehicle Entry Successful")
    print(f"Vehicle Number : {vehicle_number}")
    print(f"Allocated Slot : {slot}")
    print(f"Entry Time     : {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")


def vehicle_exit():
    vehicle_number = input("\nEnter vehicle number: ").upper()

    if vehicle_number not in vehicles:
        print("Vehicle not found.")
        return

    vehicle = vehicles[vehicle_number]

    slot = vehicle["slot"]
    entry_time = vehicle["entry_time"]

    exit_time = datetime.now()
    duration = exit_time - entry_time
    total_seconds = duration.total_seconds()

    hours = max(1, math.ceil(total_seconds / 3600))
    charge = calculate_charge(hours)

    parking_slots[slot] = None
    del vehicles[vehicle_number]

    print("\n========== PARKING BILL ==========")
    print(f"Vehicle Number : {vehicle_number}")
    print(f"Parking Slot   : {slot}")
    print(f"Entry Time     : {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Exit Time      : {exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Duration       : {hours} hour(s)")
    print(f"Parking Charge : ₹{charge}")
    print("==================================")
    print("Slot Released Successfully.")


def search_vehicle():
    vehicle_number = input("\nEnter vehicle number: ").upper()

    if vehicle_number in vehicles:
        vehicle = vehicles[vehicle_number]

        print("\nVehicle Found")
        print(f"Vehicle Number : {vehicle_number}")
        print(f"Parking Slot   : {vehicle['slot']}")
        print(f"Entry Time     : {vehicle['entry_time'].strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("Vehicle not found.")


def main():
    while True:
        print("\n========== PARKING MANAGEMENT SYSTEM ==========")
        print("1. Vehicle Entry")
        print("2. Vehicle Exit")
        print("3. Show Parking Slots")
        print("4. Search Vehicle")
        print("5. Check Parking Status")
        print("6. Exit System")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            vehicle_entry()

        elif choice == "2":
            vehicle_exit()

        elif choice == "3":
            show_slots()

        elif choice == "4":
            search_vehicle()

        elif choice == "5":
            available = sum(
                1 for vehicle in parking_slots.values()
                if vehicle is None
            )

            if available == 0:
                print("\nParking Area is FULL.")
            else:
                print("\nParking Available.")
                print(f"{available} slot(s) available.")

        elif choice == "6":
            print("\nThank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
