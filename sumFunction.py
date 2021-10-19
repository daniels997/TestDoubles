def sumIntegers(filepath):
    file = open(filepath, "r")
    line = file.read()
    line.split(",")
    total = sum([int(num) for num in line.split(',')])
    strTotal = str(total)
    file.close
    file = open(filepath, "a")
    file.write(",")
    file.write(strTotal)
    return total