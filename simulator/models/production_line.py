from simulator.models.enums import StationType
from simulator.models.station import Station

receiving_station = Station(
    station_id="RECV",
    name="Receiving",
    station_type=StationType.RECEIVING,
    sequence=1,
    cycle_time_minutes=10.0,
    capacity=1
)

PRODUCTION_LINE = [
    Station(
        station_id="RECV",
        name="Receiving",
        station_type=StationType.RECEIVING,
        sequence=1,
        cycle_time_minutes=10.0,
    ),
    Station(
        station_id="RECV_INSP",
        name="Receiving Inspection",
        station_type=StationType.INSPECTION,
        sequence=2,
        cycle_time_minutes=5.0,
    ),
    Station(
        station_id="STOCKING",
        name="Stocking",
        station_type=StationType.MATERIAL_HANDLING,
        sequence=3,
        cycle_time_minutes=10.0,
    ),
    Station(
        station_id="ORDER RELEASE",
        name="Order Release",
        station_type=StationType.CONTROL,
        sequence=4,
        cycle_time_minutes=2.0,
    ),
    Station(
        station_id="ORDER PULL",
        name="Order Pull",
        station_type=StationType.CONTROL,
        sequence=5,
        cycle_time_minutes=10.0,
    ),
    Station(
        station_id="CLEANING",
        name="Cleaning",
        station_type=StationType.PROCESSING,
        sequence=6,
        cycle_time_minutes=30.0,
    ),
    Station(
        station_id="ASSEMBLY 1",
        name="Assembly 1",
        station_type=StationType.ASSEMBLY,
        sequence=7,
        cycle_time_minutes=60.0,
    ),
    Station(
        station_id="WELDING",
        name="Welding",
        station_type=StationType.ASSEMBLY,
        sequence=8,
        cycle_time_minutes=90.0,
    ),
    Station(
        station_id="WELDING INSPECTION",
        name="Welding Inspection",
        station_type=StationType.INSPECTION,
        sequence=9,
        cycle_time_minutes=30.0,
    ),
    Station(
        station_id="ASSEMBLY 2",
        name="Assembly 2",
        station_type=StationType.ASSEMBLY,
        sequence=10,
        cycle_time_minutes=60.0,
    ),
    Station(
        station_id="MACHINING",
        name="Machining",
        station_type=StationType.PROCESSING,
        sequence=11,
        cycle_time_minutes=120.0,
    ),
    Station(
        station_id="MACHINING INSPECTION",
        name="Machining Inspection",
        station_type=StationType.INSPECTION,
        sequence=12,
        cycle_time_minutes=15.0,
    ),
    Station(
        station_id="FINISHING",
        name="Finishing",
        station_type=StationType.PROCESSING,
        sequence=13,
        cycle_time_minutes=30.0,
    ),
    Station(
        station_id="FINAL INSPECTION",
        name="Final Inspection",
        station_type=StationType.INSPECTION,
        sequence=14,
        cycle_time_minutes=30.0,
    ),
    Station(
        station_id="PACKAGING",
        name="Packaging",
        station_type=StationType.PACKAGING,
        sequence=15,
        cycle_time_minutes=20.0,
    ),
    Station(
        station_id="SHIPPING",
        name="Shipping",
        station_type=StationType.SHIPPING,
        sequence=16,
        cycle_time_minutes=15.0,
    )
]