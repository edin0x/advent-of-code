input = open("input", "r").read().split('\n\n')

allRequiredFields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'] # without cid

validPassports = sum([(sum([1 for rf in allRequiredFields if rf in passport]) == len(allRequiredFields)) for passport in input])

print('ANSWER: ' + str(validPassports))