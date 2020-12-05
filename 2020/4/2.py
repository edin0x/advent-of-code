import re
input = open("input", "r").read().split('\n\n')

optionalFields = ['cid']

check = {
  'byr': lambda x: int(x) >= 1920 and int(x) <= 2002,
  'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020,
  'eyr': lambda x: int(x) >= 2020 and int(x) <= 2030,
  'hgt': lambda x: ('cm' in x and int(x.split('cm')[0]) >= 150 and int(x.split('cm')[0]) <= 193) or ('in' in x and int(x.split('in')[0]) >= 59 and int(x.split('in')[0]) <= 76),
  'hcl': lambda x: re.findall(r"^\#[0-9a-f]+$", x) != [],
  'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
  'pid': lambda x: re.findall(r"^[0-9]{9}$", x) != [],
}

validPassports = 0
for pp in input:
  fieldValues = [x.split(':') for x in pp.replace('\n', ' ').split(' ')]
  validFields = [check[fv[0]](fv[1]) for fv in fieldValues if fv[0] not in optionalFields]

  isValidPassport = False not in validFields and sum(validFields) >= len(check)
  if isValidPassport:
    validPassports += 1

print('ANSWER: ' + str(validPassports))