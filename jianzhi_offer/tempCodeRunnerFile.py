_max = 0
        tmp = ""
        for c in s:
            if c in tmp:
                if len(tmp) > _max:
                    _max = len(tmp)
                tmp = c
            else:
                tmp += c
        if len(tmp) > _max:
            _max = len(tmp)
        return count