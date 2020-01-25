const factors = n => [...Array(n).keys()].map(x => x + 1).filter(x => n % x === 0);

const isEqualArray = (x, y) => JSON.stringify(x) == JSON.stringify(y);

const isPrime = n => isEqualArray(factors(n), [1, n]);

const sum = arr => arr.reduce((a, b) => a + b);

const combinations = nums => {
    return (function acc(xs, nums) {
        const x = xs[0];
        if(typeof x === "undefined")
            return nums;
        for(let i = 0, l = nums.length; i < l; ++i)
            nums.push(nums[i].concat(x));
        return acc(xs.slice(1), nums);
    })(nums, [[]]).slice(1);
};

function solution(nums) {
    return combinations(nums).filter(x => x.length === 3).map(sum).filter(isPrime).length;
};


var nums = [1,2,7,6,4]

// var combinations = nums => {
//     return (function acc(xs, nums) {
//         const x = xs[0];
//         if(typeof x === "undefined")
//             return nums;
//         for(let i = 0, l = nums.length; i < l; ++i)
//             nums.push(nums[i].concat(x));
//         return acc(xs.slice(1), nums);
//     })(nums, [[]]).slice(1);
// };

// const res = combinations(nums).filter(x => x.length === 3)

// var res = nums.reduce( (acc, v, i) => {
//     return acc.concat(array.slice(i+1).map(x => x.toString()).map(w => v + w ))
// }, []);

// var res = nums.reduce( (acc, v, i) => {
//     return acc.concat()
// }, []);

const res = solution(nums)

console.log(res);