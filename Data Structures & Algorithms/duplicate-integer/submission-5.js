class Solution {
  hasDuplicate(nums) {
    let seen = new Set();

    for (let i = 0; i < nums.length; i++) {
      // Check whether nums[i] is in seen
      if (seen.has(nums[i])){
        return true;
      }
        seen.add(nums[i]);
      

      // If it is, return true

      // Otherwise, add nums[i] to seen
    }

    return false;
  }
}