def water_container(heights):
    l = 0
    r = len(heights) - 1
    area = 0
    while l < r:
        Min = min(heights[l],heights[r])
        
        area = max(area , Min * (r - l))
        
        if heights[l] > heights[r]:
            r-=1
        else:
            l+=1
    return area

if __name__ == '__main__':
    arr = [1,8,6,2,5,4,8,3,7]
    print(water_container(arr))             