def remove_all(item, fromlist):
    """Remove all instances of item from fromlist."""
    while True:
        try:
            fromlist.remove(item)
        except ValueError:
            return None
