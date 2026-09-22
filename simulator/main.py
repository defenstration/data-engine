from simulator.models.production_line import PRODUCTION_LINE
from simulator.models.part import Part
from simulator.models.event import Event
from simulator.models.enums import EventType
from simulator.models.production_order import ProductionOrder
from datetime import datetime, timedelta


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

    receiving= PRODUCTION_LINE[0]
    simulation_start = datetime(2026, 9, 18, 8, 0)


    events, exit_time = receiving.process_part(
        part=parts[0],
        arrival_time=simulation_start
    )

    print()
    print("Event History")
    for event in events:
        print(
            f"{event.timestamp:%H:%M} - "
            f"{event.part_id} - "
            f"{event.station_id} - "
            f"{event.event_type.value}"
        )

    print()
    print(f"Station exit: {exit_time:%H:%M}")

if __name__ == "__main__":
    main()