func canPlaceFlowers(flowerbed []int, n int) bool {
	if n == 0 {
		return true
	}

	for idx := range flowerbed {
		if flowerbed[idx] == 0 && (idx == 0 || flowerbed[idx-1] == 0) && (idx == len(flowerbed)-1 || flowerbed[idx+1] == 0) {
			flowerbed[idx] = 1
			n--
			if n == 0 {
				return true
			}
		}
	}
	return false
}
