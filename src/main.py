"""Run with python -m src.main, from the NightShift folder."""

from .data_io import RAW, load_bookings, load_config, write_outputs
from .models import Booking, Report, Shift


def command_loop(shift: Shift, config: dict) -> None:
    """Support summary, find ID, zone NAME, and quit/q using while and match.

    TODO P2: Match input().strip().split() as a sequence. Unknown commands
    print help and continue. quit/q breaks the loop. Exact command shapes
    matter: 'zone PC extra' must not count as 'zone PC'. Uppercase IDs/zones.
    A missing booking prints 'Not found'. EOF exits gracefully.
    This is a read-only exploration menu; payment editing is out of scope.
    """
    raise NotImplementedError("P2: command_loop")


def main() -> None:
    """Connect the functions you implement. Orchestration supplied."""
    config = load_config()
    records, rejected, duplicates = load_bookings(RAW / "bookings.csv")
    shift = Shift(config["shift_date"])
    for record in records:
        shift.add(Booking.from_record(record))
    summary = shift.summary(config["rates_vnd"])
    text = Report(shift, config).render()
    write_outputs(records, rejected, duplicates, summary, text)
    print(f"Read {len(records)} valid, {len(rejected)} rejected, {len(duplicates)} duplicates.")
    print(text)
    command_loop(shift, config)


if __name__ == "__main__":
    main()
