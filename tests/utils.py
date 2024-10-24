
def link_to_requirement(req_id):
    """
    Decorator to attach a requirement ID to a test function.
    """
    def decorator(func):
        func.__doc__ = f"Requirement: {req_id}"
        func.requirement_id = req_id  # Add the requirement ID as a custom attribute
        return func
    return decorator
