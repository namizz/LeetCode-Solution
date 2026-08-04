function differenceOfSum(nums: number[]): number {
    let total = 0;
    let digit = 0;
    for (let i = 0; i < nums.length; i++ ){
        let temp = nums[i];
        total += nums[i]

        while(temp > 0){
            digit += temp%10;
            temp = Math.floor(temp /10)
        }
    }
    return total-digit
    
};