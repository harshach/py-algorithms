def binary_search(list,key):
    if key == None or list == None:
        return None
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low+high) / 2
        val = list[mid]
        if val > mid:
            high = mid - 1
        elif val < item:
            low = mid + 1
        else:
            return val
    
    return None

def kmp_search(string,substring):
    if string == None or substring == None:
        return None
    
    pos = 2
    cnd = 0
    failure_table = [-1,0]
    while pos < len(substring):
        if substring[pos - 1] == substring[cnd]:
            failure_table.insert(pos,cnd + 1)
            pos += 1
            cnd += 1
        elif cnd > 0:
            cnd = failure_table[cnd]
        else:
            failure_table.insert(pos,0)
            pos += 1
    
    m = i = 0
    while (m + i) < len(string):
        if substring[i] == string[m + i]:
            i += 1
            if i == len(substring):
                return m 
        else:
            m = m + i - failure_table[i]
            if i > 0:
                i = failure_table[i] 
      
    return None

