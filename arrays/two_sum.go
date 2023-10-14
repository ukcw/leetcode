func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)

	for idx, element := range nums {
		leftover := target - element
		if _, ok := seen[leftover]; ok {
			return []int{seen[leftover], idx}
		}
		seen[element] = idx
	}

	return nil
}
