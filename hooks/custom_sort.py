CATEGORY_ORDER = {
    "Level Up": 0,
    "Soft Skills": 1,
}


def category_order(view):
    return CATEGORY_ORDER.get(view.name, 999)
