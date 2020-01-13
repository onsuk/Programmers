function solution(skill, skillTrees) {
    return skillTrees
        .map(filterComparable(skill))
        .filter(compare(skill))
        .length;
};

const filterComparable = skill => skillTree => {
    return skillTree.split('').filter(eachSkill => skill.includes(eachSkill)).join('');
};

const compare = skill => comparable => {
    return skill.startsWith(comparable);
};
