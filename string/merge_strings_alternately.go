func mergeAlternately(word1 string, word2 string) string {
    result := ""
    for idx, _ := range word1 {
        if idx == len(word1) - 1 {
            return result + string(word1[idx]) + word2[idx:]
        }
        if idx == len(word2) {
            return result + word1[idx:]
        }
        result += string(word1[idx]) + string(word2[idx])
    }

    return result
}
