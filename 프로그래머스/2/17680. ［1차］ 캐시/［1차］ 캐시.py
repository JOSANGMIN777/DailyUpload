def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            answer += 5
            continue
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5
            if len(cache) >= cacheSize:
                cache.pop(0)
        cache.append(city)

    return answer