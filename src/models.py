"""Three cooperating classes: a booking, its shift, and a report."""

from .analysis import charge_for, summarize


class Booking:
    """Hold one valid booking and calculate its bill."""

    MAX_MINUTES = 300
    created_count = 0

    def __init__(self, booking_id, player, zone, minutes, snack_vnd,
                 paid_vnd, status, tags=None):
        """Initialize independent state from normalized data.

        TODO R4: Assign all eight fields. _tags is a fresh list even when a
        caller supplies a list. Reject invalid duration. Increment the class
        counter only after successful initialization. No non-None return.
        """
        raise NotImplementedError("R4: Booking.__init__")

    @classmethod
    def from_record(cls, record: dict):
        """Build an instance from an already normalized record using cls.

        TODO R4: Unpack keyword arguments. No second CSV parsing here.
        """
        raise NotImplementedError("R4: Booking.from_record")

    @staticmethod
    def valid_duration(minutes: int, status: str) -> bool:
        """Completed: int 1..300; cancelled: int 0. bool is not a duration.

        TODO R4: Unknown status or invalid type returns False.
        """
        raise NotImplementedError("R4: Booking.valid_duration")

    @property
    def is_completed(self) -> bool:
        """Report completion as a read-only computed attribute."""
        raise NotImplementedError("R4: Booking.is_completed")

    def tags(self) -> list[str]:
        """Return a fresh shallow copy of the internal tag list."""
        raise NotImplementedError("R4: Booking.tags")

    def charge(self, rates: dict) -> int:
        """Delegate to charge_for using the normalized fields on this instance."""
        raise NotImplementedError("R4: Booking.charge")

    def due(self, rates: dict) -> int:
        """Return max(charge minus payment, zero); do not change payment."""
        raise NotImplementedError("R4: Booking.due")


class Shift:
    """Contain Booking objects for one shift."""

    def __init__(self, label: str):
        """Create a label and a separate internal booking list for each shift."""
        raise NotImplementedError("R4: Shift.__init__")

    def add(self, booking: Booking) -> None:
        """Append a Booking; reject wrong types (TypeError) or duplicate IDs (ValueError)."""
        raise NotImplementedError("R4: Shift.add")

    def bookings(self) -> list[Booking]:
        """Return a shallow copy; contained Booking objects remain shared."""
        raise NotImplementedError("R4: Shift.bookings")

    def find(self, booking_id: str) -> Booking | None:
        """Find an exact normalized ID or return None without modifying state."""
        raise NotImplementedError("R4: Shift.find")

    def summary(self, rates: dict) -> dict:
        """Delegate all aggregation to summarize."""
        return summarize(self.bookings(), rates)


class Report:
    """Use a Shift to format a report without owning accounting rules."""

    def __init__(self, shift: Shift, config: dict):
        """Store the given shift and config as references. Plumbing supplied."""
        self.shift = shift
        self.config = config

    def render(self) -> str:
        """Return a readable closing report using Shift.summary.

        TODO P1: Include overall totals, zone breakdown, top three debtors.
        Use f-strings, aligned columns, thousands separators, and enumerate.
        Format missing averages as N/A. Wording need not match sample exactly.
        """
        raise NotImplementedError("P1: Report.render")
