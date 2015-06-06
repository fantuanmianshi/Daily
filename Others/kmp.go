
// https://github.com/reterVision/go-algorithms/tree/master/kmp
package kmp

func getOverlap(pattern string) []int {
    overlap := make([]int, len(pattern)+1)
    overlap[0] = -1
    for i, _ := range pattern {
        overlap[i+1] = overlap[i] + 1
        for overlap[i+1] > 0 && pattern[i] != pattern[overlap[i+1]-1] {
            overlap[i+1] = overlap[overlap[i+1]-1] + 1
        }
    }
    return overlap
}

// KMP returns the index of target in src if it exists, otherwise -1
func KMP(source, target string) int {
    i, j := 0, 0
    overlap := getOverlap(target)
    for i+j < len(source) {
        if source[i+j] == target[j] {
            if j == len(target)-1 {
                return i
            }
            j += 1
        } else if overlap[j] > -1 {
            i = i + j - overlap[j]
            j = overlap[j]
        } else {
            i, j = i+1, 0
        }
    }

    return -1
}
