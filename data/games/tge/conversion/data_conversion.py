







def convertFloat(input_string: int) -> float:
    """
    Checks if the given string can be converted to a float.
    """
    try:
        input_string = float(input_string)
        return input_string
    except ValueError:
        return 0

def convertInt(input_string: str) -> int:
    """
    Checks if the given string can be converted to an integer.
    """
    try:
        input_string = int(input_string)
        return input_string
    except ValueError:
        return 0



def compareType(*objs) -> bool:
    """
    Check if any of the objects share a common ancestor class in their class hierarchy.
    """
    def get_class_hierarchy(cls):
        """
        Get the class hierarchy of a class, including all base classes.
        """
        hierarchy = set()
        queue = [cls]
        while queue:
            cls = queue.pop(0)
            hierarchy.add(cls)
            queue.extend(b for b in cls.__bases__ if b not in hierarchy and b is not object)
        return tuple(hierarchy)
    class_hierarchy_tuples = [get_class_hierarchy(o.__class__) for o in objs]
    intersection = {t for t in class_hierarchy_tuples[0] if all(t in ct for ct in class_hierarchy_tuples[1:])}
    return len(intersection) > 0
