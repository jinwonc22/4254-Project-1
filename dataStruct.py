import json

class Shape:
    def __init__(self, pos, color, shape_type):
        self.pos = pos
        self.color = color
        self.shape_type = shape_type

    def to_dict(self):
        return {
            "position": self.pos,
            "color": self.color,
            "shape_type": self.shape_type
        }

shapes = []

s = Shape((10, 20), "red", "circle")

shapes.append(s)

shapes_json = json.dumps([shape.to_dict() for shape in shapes], indent=2)

print(shapes_json)

with open("shapes.json", "w") as f:
    f.write(shapes_json)
