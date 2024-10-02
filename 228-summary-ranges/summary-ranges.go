func summaryRanges(nums []int) []string {
    if len(nums) == 0 {
        return []string{}
    }
    start, end := nums[0], nums[0]
    ans := make([] string,0)
    i := 0
    for i < len(nums){
        if i < len(nums)-1 && nums[i] + 1 == nums[i+1]{
            end += 1        

        }else{
            if start == end{
                ans = append(ans, strconv.Itoa(start))

            }else{
                ans = append(ans, strconv.Itoa(start) + "->" + strconv.Itoa(end))
            }
            if i < len(nums) - 1{
                start,end = nums[i+1],nums[i+1]
            }       
            
            
        }
        i += 1
    }
    return ans
    
}