from entity import model

staff1 = model.Staff("123111", "kesong", 1)
staff2 = model.Staff("123111", "kesng", 1)

print staff1 == staff2
print id(staff1)
print id(staff2)
print staff1 != staff2
print staff1 is staff2

row1 = model.TableRow("1234", "abcd123")
row2 = model.TableRow("1234", "abcd123")
print row1 == row2
print len(row1.result)



