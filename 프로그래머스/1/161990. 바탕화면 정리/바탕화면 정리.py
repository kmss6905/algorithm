def solution(wallpaper):
    answer = []
    min_y, min_x, max_x, max_y = [51, 51, -1, -1]
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == '#':
                min_y = min(y, min_y)
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                max_y = max(y, max_y)
    return [min_y,min_x, max_y+1, max_x+1]