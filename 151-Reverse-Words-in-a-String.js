/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let i = s.length - 1;
    let ans = \\;
    while (i >= 0) {
        if (s[i] != \ \) {
            let word = \\;
            let end = i;
        while (i >= 0 && s[i] != \ \) {
            i--;
      }
      let start = i;
      word = s.slice(start + 1, end + 1);
      if (word && ans != \\) ans += \ \;
      ans += word;
    }
    i--;
  }
  return ans
    
    
};