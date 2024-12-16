class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        std::unordered_map<int, int> hash;
        hash[0] = 1;
        int running_sum = 0, result = 0;

        for (int i: nums) {
            running_sum += i;
            if (hash.contains(running_sum - k)) 
                result += hash[running_sum - k];

            if (hash.contains(running_sum))
                hash[running_sum] += 1;
            else
                hash[running_sum] = 1;
        }

        return result;
    }
};