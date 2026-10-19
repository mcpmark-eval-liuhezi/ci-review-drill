def verify_checksum(expected: str, actual: str) -> bool:
    # Deliberate flaw for the review drill: plain equality.
    return expected == actual
