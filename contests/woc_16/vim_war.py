from itertools import chain, combinations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def subsets(s):
    return map(set, powerset(s))


def is_valid_skillset(skillset_requirement, total_skillset, num_possible_skills):
    for i in xrange(num_possible_skills):
        if total_skillset[i] < skillset_requirement[i]:
            return False
    return True


def is_valid_army(army, soldiers_array, skillset_requirement, num_possible_skills):
    total_skillset = [0] * num_possible_skills
    for soldier_num in army:
        for skill in xrange(num_possible_skills):
            if soldiers_array[soldier_num][skill] == 1:
                total_skillset[skill] = 1
    return is_valid_skillset(skillset_requirement, total_skillset, num_possible_skills)


def get_valid_armies(num_soldiers, soldiers_array, skillset_requirement, num_possible_skills):
    possible_armies = subsets(range(num_soldiers))
    valid_army_count = 0
    for army in possible_armies:
        if is_valid_army(army, soldiers_array, skillset_requirement, num_possible_skills):
            valid_army_count += 1
    return valid_army_count


def hackerrank():
    num_soldiers, num_possible_skills = [int(x) for x in raw_input().split()]
    soldiers_array = []
    for _ in xrange(num_solders):
        skill_to_soldier_array = [int(x) for x in raw_input().split()]
        soldiers_array.append(skill_to_soldier_array)
    skillset_requirement = [int(x) for x in raw_input().split()]
    print get_valid_armies(num_soldiers, soldiers_array, skillset_requirement, num_possible_skills)


def local():
    num_soldiers = 4
    num_possible_skills = 2
    soldiers_array = [[0,0], [1, 0], [0, 1], [1, 1]]
    skillset_requirement = [1, 1]
    print get_valid_armies(num_soldiers, soldiers_array, skillset_requirement, num_possible_skills)


if __name__ == "__main__":
    # hackerrank()
    local()
