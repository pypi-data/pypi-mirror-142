__all__ = ['find_last']


def find_last(elements: list, element):
    if element not in elements:
        return -1

    elements.reverse()
    index = elements.index(element)
    elements.reverse()
    return len(elements) - index - 1
