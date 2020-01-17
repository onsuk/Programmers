function solution(A, B) {
    let point = 0;
    A.sort(sortFunction);
    B.sort(sortFunction);
    let idxOfA = A.length - 1;
    let idxOfB = B.length - 1;
    while(idxOfA >= 0) {
        let valOfA = A[idxOfA];
        let valOfB = B[idxOfB];
        if(valOfB > valOfA) {
            idxOfB -= 1;
            point += 1;
        }
        idxOfA -= 1;
    }
    return point;
};

const sortFunction = (a, b) => a - b;
