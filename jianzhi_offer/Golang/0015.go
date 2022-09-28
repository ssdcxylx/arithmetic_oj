package main

func findAnagrams(s string, p string) (res []int) {
    flags := make([]int, 26)
    for _, c := range p {
        flags[c-'a']--
    }
    i, n := 0, len(p)
    for j, c := range s {
        x := c-'a'
        flags[x]++
        for ; flags[x]>0; i++ {
            flags[s[i]-'a']--
        }
        if j-i+1 == n{
            res = append(res, i)
        }
    }
    return
}