class RateLimitError(Exception):
    """
    Error returned when we hit the rate limit of the used AI service.
    """