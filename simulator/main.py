from simulator.models.station import Station
from simulator.models.enums import StationType

def main():
    cnc = Station(
        station_id="CNC",
        name="CNC Machining",
        station_type=StationType.PROCESSING,
        sequence=3,
        cycle_time_minutes=45.0,
        capacity=1
    )

    print(cnc)

if __name__ == "__main__":
    main()