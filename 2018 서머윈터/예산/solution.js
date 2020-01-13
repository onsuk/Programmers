function solution(d, budget) {
    d.sort((a, b) => a - b);
    return canSupply(d, budget);
};

const canSupply = (suppliable, budget) => {
    if(sum(suppliable) <= budget) return suppliable.length
    suppliable.pop();
    return canSupply(suppliable, budget);
};

const sum = sup => sup.reduce((x, acc) => x + acc, 0);
