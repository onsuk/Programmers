function solution(n) {
    return Array.from(n.toString(2)).filter(x => x === '1').length
}
