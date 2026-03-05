CATEGORY_ORDER = {
    "AI": 0,
    "Tech": 1,
    "Level Up": 2,
    "Soft Skills": 3,
    "Life": 4,
}


def category_order(view):
    return CATEGORY_ORDER.get(view.name, 999)
