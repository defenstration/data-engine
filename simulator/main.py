from simulator.models.production_line import PRODUCTION_LINE
from simulator.models.part import Part
from simulator.models.event import Event
from simulator.models.enums import EventType
from simulator.models.production_order import ProductionOrder


def main():
    print("THE DATA ENGINE")
    print()
    print("Production Line")

    for station in PRODUCTION_LINE:
        print(
            f"{station.sequence}, "
            f"{station.name} "
            f"({station.cycle_time_minutes} min)"   
        )

    print()
    print(f"{len(PRODUCTION_LINE)} stations loaded successfully.")

    order = ProductionOrder(
        order_id="WO-1001",
        part_number="HOUSING-100",
        quantity=3,
    )

    parts = []

    for number in range(1, order.quantity +1):
        part= Part(
            part_id=f"PART-{number:06d}",
            part_number=order.part_number,
            order_id=order.order_id,
        )

        parts.append(part)

    event = Event(
        part_id=parts[0].part_id,
        station_id="RECV",
        event_type=EventType.QUEUE_ENTERED,
    )

    print()
    print("Parts:")

    for part in parts:
        print(part)

    print()
    print("Sample Event")
    print(event)

    print()
    print("Sample Production Order")
    print(order)

if __name__ == "__main__":
    main()