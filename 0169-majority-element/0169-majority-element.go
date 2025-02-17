func majorityElement(nums []int) int {
    hashmap := make(map[int]int)
    for i:= 0; i< len(nums); i++{
        hashmap[nums[i]]++
        if hashmap[nums[i]] > len(nums)/2{
            return nums[i]
        }
    }
    return -1
    
}