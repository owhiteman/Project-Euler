num1 = 1
num2 = 2
evenSum = 0

while num2 < 4000000:

    if num2 % 2 == 0:
        evenSum += num2
    fibSum = num1 + num2
    num1 = num2
    num2 = fibSum


print "Sum of even valued terms:"
print evenSum
