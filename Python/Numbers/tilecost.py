def tile_cost(width, height, cost):
    if (type(width) not in [float, int]) or (type(height) not in [float, int]) or (type(cost) not in [float, int]):
        raise TypeError("The values need to be non-negative integer numbers.")
    if (width <= 0) or (height <= 0) or (cost <= 0):
        raise ValueError("The values need to be non-negative.")
    return width * height * cost


def main():
    while True:
      try:
        width = float(input("Isert the Widht of the area to cover: "))
        if width < 1:
            raise ValueError
        height = float(input("Isert the Height of the area to cover: "))
        if height < 1:
            raise ValueError
        cost = float(input("Insert the Cost of the tile: "))
        if cost < 1:
            raise ValueError
      except ValueError:
        print("ERROR: The values need to be non-negative integer numbers.")
      else:
        res = tile_cost(width, height, cost)
        print("It will cost {cost}$ to cover a floor plan of {width}m and {height}m.".format(cost=res, width=width, height=height))
        break


if __name__ == '__main__':
    main()