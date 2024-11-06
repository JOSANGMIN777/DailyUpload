def solution(wallpaper):
    
    tmp = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                tmp.append([i,j])
    min_x = 999999
    min_y = 999999
    max_x = -1
    max_y = -1
    for i in tmp:
        if i[0] < min_x:
            min_x = i[0]
        if i[0] > max_x:
            max_x = i[0]
        if i[1] < min_y:
            min_y = i[1]
        if i[1] > max_y:
            max_y = i[1]
    return [min_x,min_y,max_x+1,max_y+1]
    