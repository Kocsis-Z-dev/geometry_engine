from geometry import tavolsag_3d
def utkozik_gomb_gomb(kozep1, r1, kozep2, r2):
    return tavolsag_3d(kozep1, kozep2) <= (r1 + r2)
def utkozik_box_box(box1, box2):
    min_x1, max_x1, min_y1, max_y1, min_z1, max_z1 = box1
    min_x2, max_x2, min_y2, max_y2, min_z2, max_z2 = box2
    if max_x1 < min_x2 or min_x1 > max_x2:
        return False
    if max_y1 < min_y2 or min_y1 > max_y2:
        return False
    if max_z1 < min_z2 or min_z1 > max_z2:
        return False
    return True
def utkozik_gomb_kocka(kozep, sugar, box):
    cx, cy, cz = kozep
    min_x, max_x, min_y, max_y, min_z, max_z = box
    closest_x = max(min_x, min(cx, max_x))
    closest_y = max(min_y, min(cy, max_y))
    closest_z = max(min_z, min(cz, max_z))
    legkozelebbi = (closest_x, closest_y, closest_z)
    return tavolsag_3d(kozep, legkozelebbi) <= sugar