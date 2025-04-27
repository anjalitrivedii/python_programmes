def grade_to_letter(grade):
    if 90 <= grade <=100:
        return 'A'
    elif 80 <= grade <=90:
        return 'B'
    elif 70 <= grade <=80:
        return 'C'
    elif 60 <= grade <=70:
        return 'D'
    elif 0 <= grade <=60:
        return 'F'
    else:
        return 'invalid grade'

numeric_grade =float(input("enter a numeric grade:"))
letter_grade =grade_to_letter(numeric_grade)
print(f"letter grade:{letter_grade}")