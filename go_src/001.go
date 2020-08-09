import "fmt"

func twoSum(nums []int, target int) []int {
    m := map[int]int{}
    for index, value := range nums {
        missing := target - value
        index_value, exists := m[missing]
        if exists {
            return []int{index, index_value}
        }
        m[value] = index
    }
    return []int{0, 0}
}