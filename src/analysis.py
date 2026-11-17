"""Small pure calculations, deliberately independent of file I/O."""


def charge_for(record: dict, rates: dict, /, *, block_minutes: int = 30) -> int:
    """Return zero for cancelled bookings, otherwise rounded-up block fees + snacks.

    TODO R3: Inputs are normalized. Round the number of blocks up, not down.
    Keep currency as integer VND. Do not mutate either argument.
    """
    raise NotImplementedError("R3: charge_for")


def balance_band(due: int, *, threshold: int = 20000) -> str:
    """Return 'settled' for zero, 'urgent' for due >= threshold, else 'follow_up'.

    TODO R3: Reject negative due or non-positive threshold with ValueError.
    """
    raise NotImplementedError("R3: balance_band")


def summarize(bookings: list, rates: dict) -> dict:
    """Aggregate Booking objects without modifying them; see expected schema.

    TODO P1: Counts, charges, payments, due, completed-play mean, zone totals,
    and top three outstanding bookings. Include PC, CONSOLE, VR even if empty.
    Ranking: descending due, then ascending booking_id; omit zero due.
    Mean minutes excludes cancelled bookings; use None if no completed rows.
    """
    raise NotImplementedError("P1: summarize")
