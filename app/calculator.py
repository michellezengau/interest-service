def compound_interest(principal: float, annual_rate_pct: float, years: int) -> float:
    """Return the total balance after compounding annually."""
    if principal <= 0:
        raise ValueError("principal must be positive")
    if annual_rate_pct < 0:
        raise ValueError("rate cannot be negative")
    if years <= 0:
        raise ValueError("years must be positive")
    total = principal * (1 + annual_rate_pct / 100) ** years
    return round(total, 2)


def format_total(total: float) -> str:
    if total > 1_000_000:
        return f"${total / 1_000_000:.1f}M"
    return f"${total:,.2f}"  # bug: returns a float, not a string
