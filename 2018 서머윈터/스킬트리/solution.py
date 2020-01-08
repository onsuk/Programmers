def solution(skill, skill_trees):
    comparable = [filter_skill(skill, skill_tree) for skill_tree in skill_trees]
    answer = compare(skill, comparable)
    return len(answer)


def filter_skill(skill, skill_tree):
    return "".join(filter(lambda x: x in set(skill), skill_tree))


def compare(skill, comparable):
    return list(filter(lambda x: skill.startswith(x), comparable))
