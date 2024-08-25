class Colors:
    DARK_GRAY = (26, 31, 40)
    GREEN = (47, 230, 23)
    RED = (232, 18, 18)
    ORANGE = (226, 116, 17)
    YELLOW = (237, 234, 4)
    PURPLE = (166, 0, 247)
    CYAN = (21, 204, 209)
    BLUE = (13, 64, 216)

    @classmethod
    def get_cell_colors(cls):
        return [cls.DARK_GRAY, cls.GREEN, cls.RED, cls.ORANGE, cls.YELLOW, cls.PURPLE, cls.CYAN, cls.BLUE]