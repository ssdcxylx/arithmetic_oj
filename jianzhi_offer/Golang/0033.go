package main

func groupAnagrams(strs []string) [][]string {
	mp := map[[26]int][]string{}
	for _, str := range strs {
		cnts := [26]int{}
		for _, c := range str {
			cnts[c-'a']++
		}
		mp[cnts] = append(mp[cnts], str)
	}
	ans := make([][]string, 0, len(mp))
	for _, v := range mp {
		ans = append(ans, v)
	}
	return ans
}