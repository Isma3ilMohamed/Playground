def sort_colors(colors: list[int]) -> list[int]:
    start = 0
    current = 0
    end = len(colors) - 1
    while current <= end:
        if colors[current] == 0:
            if colors[start] == 0:
                temp = colors[start]
                colors[start] = colors[current]
                colors[current] = temp
            current += 1
            start += 1

        elif colors[current] == 1:
            current += 1

        else:
            if colors[end] != 2:
                temp = colors[current]
                colors[current] = colors[end]
                colors[end] = temp

            end -= 1

    return colors
