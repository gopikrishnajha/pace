from shapely.geometry import box

def intersects(b1, b2):
    # b = [x, y, w, h] -> convert to x1,y1,x2,y2
    def to_poly(b):
        x, y, w, h = b
        return box(x, y, x + w, y + h)
    return to_poly(b1).intersects(to_poly(b2))
