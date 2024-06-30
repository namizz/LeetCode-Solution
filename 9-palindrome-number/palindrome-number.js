/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let check = "true";
    let lp = 0;
    let rp = (String(x)).length - 1;
    let num = x+'';
    if (Number(x) < 0){
        check = 0;
    }
    while(lp <= rp){
        if(num[lp] != num[rp]){
            check = 0;
        }
        lp++;
        rp--;
    } 
    return check;
};