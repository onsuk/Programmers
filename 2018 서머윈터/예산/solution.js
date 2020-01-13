function solution(d, budget) {
    d.sort((a, b) => a - b);
    return canSupply(d, budget);
};

const canSupply = (suppliable, budget) => {
    if(sum(suppliable) <= budget) return suppliable.length
    suppliable.pop();
    return canSupply(suppliable, budget);
};

const sum = sup => {
    if(sup.length === 0) return 0;
    return sup.reduce((x, acc) => x + acc);
}
