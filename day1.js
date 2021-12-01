const fs = require('fs');

const data = fs.readFileSync('day1.txt', 'utf8');

const nums = data.split(/\r?\n/g);
let count=0;

const groupNums=[];
let group;

for(let i=0; i<=nums.length-2; i++){
    group = parseInt(nums[i])+parseInt(nums[i+1])+parseInt(nums[i+2]);
    groupNums.push(group);
}
console.log(nums.length);
console.log(groupNums.length);
console.log(groupNums);

let previous = groupNums[0];

for(let i=1; i<=groupNums.length; i++){
    if(groupNums[i]>previous){
        count++;
    }
    previous=groupNums[i];
}
console.log(count);