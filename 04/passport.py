import functools
import re

END_OF_PASSPORT = "\n"
REQUIRED_KEYS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
    # "cid"
]

HEIGHT_REGEX = re.compile(r"(\d+)((cm|in))")
COLOR_REGEX = re.compile(r"(#[0-9a-f]{6})")
PID_REGEX = re.compile(r"([0-9]{9})")
VALID_EYE_COLORS = [
    "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
]

def generatePassports(lines):
    passports = []
    currentPassport = []
    for line in lines:
        if line == END_OF_PASSPORT:
            joinedPassport = " ".join(currentPassport)
            passports.append(joinedPassport)
            currentPassport = []
        else:
            currentPassport.append(line.strip())

    oinedPassport = " ".join(currentPassport)
    passports.append(joinedPassport)

    return passports

def validatePassportSimple(passport):
    fields = passport.split(" ")
    tokens = [field.split(":") for field in fields]
    keys = [ key for [key, value] in tokens]
    for requiredKey in REQUIRED_KEYS:
        if requiredKey not in keys:
            return False
    return True

def validatePassportComplex(passport):
    fields = passport.split(" ")
    tokens = [field.split(":") for field in fields]
    keys = {key: value for [key, value] in tokens}
    for requiredKey in REQUIRED_KEYS:
        if requiredKey not in keys:
            return False
        key = requiredKey
        value = keys[key]
        if key == "byr":
            year = int(value)
            if not (len(value) == 4 and year >= 1920 and year <= 2002):
                return False
        elif key == "iyr":
            year = int(value)
            if not (len(value) == 4 and year >= 2010 and year <= 2020):
                return False
        elif key == "eyr":
            year = int(value)
            if not (len(value) == 4 and year >= 2020 and year <= 2030):
                return False
        elif key == "hgt":
            checkValidHeight = re.match(HEIGHT_REGEX, value)
            if checkValidHeight is None:
                return False
            sizeUnitTuple = checkValidHeight.group(1, 2)
            size = int(sizeUnitTuple[0])
            unit = sizeUnitTuple[1]
            if unit == "cm" and not (size >= 150 and size <= 193):
                return False
            elif unit == "in" and not (size >= 59 and size <= 76):
                return False
        elif key == "hcl":
            if re.match(COLOR_REGEX, value) is None:
                return False
        elif key == "ecl":
            if value not in VALID_EYE_COLORS:
                return False
        elif key == "pid":
            if re.match(PID_REGEX, value) is None:
                return False
    return True


with (open('input.txt', 'r')) as file:
    lines = file.readlines()
    passports = generatePassports(lines)
    passportValidations = [ validatePassportComplex(passport) for passport in passports ]
    numberOfValidPassports = functools.reduce(lambda acc, cur: acc + 1 if cur else acc, passportValidations, 0)
    print(numberOfValidPassports)
    # for v in passportValidations:
    #     print(v)
    