/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let i = 0;
    const str = [];
    const arr = [1,4,5,9,10,40,50,90,100,400,500,900,1000];
    const map={
        1:"I", 4:"IV" , 5:"V" , 9:"IX" , 10:"X",40:"XL", 50:"L",
        90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"

    };
    while( i<= arr.length && num > 0){
        if (num >= arr[i]) i++;
        else{
            num -= arr[i-1];
            str.push(map[arr[i-1]]);
            i = 0;
        }
    }
    return str.join("");


    
};