import types


def link_to_requirement(req_id):
    """
    This decorator can be used to annotate test functions or classes with a specific
    requirement ID. The requirement ID will be added to the docstring and as a custom
    attribute (`requirement_id`) of the decorated function or class.

    Args:
        req_id (str): The requirement ID to attach.

    Returns:
        function: The decorator function that attaches the requirement ID.

    Usage:
        @link_to_requirement("REQ-1234")
        def test_function():
            pass

        @link_to_requirement("REQ-5678")
        class TestClass:
            def test_method(self):
                pass
    """
    def decorator(obj):
        if isinstance(obj, types.FunctionType):
            obj.__doc__ = f"Requirement: {req_id}"
            obj.requirement_id = req_id  # Add the requirement ID as a custom attribute
        elif isinstance(obj, type):
            obj.__doc__ = f"Requirement: {req_id}"
            obj.requirement_id = req_id  # Add the requirement ID as a custom attribute
            for attr_name in dir(obj):
                attr = getattr(obj, attr_name)
                if isinstance(attr, types.FunctionType):
                    attr.__doc__ = f"Requirement: {req_id}"
                    attr.requirement_id = req_id
        return obj
    return decorator
