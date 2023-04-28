def in_range(start,end,step=1):
    result = []
    i = start
    if step == 0:
        raise ValueError('step cannot by 0')
    if step > 0:
        while i < end:
            result.append(i)
            i += step
    if step < 0:
        while i > end:
            result.append(i)
            i += step
    return result


print(in_range(1,11,1))
print(in_range(-1,-16,-1))






