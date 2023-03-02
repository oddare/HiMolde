def triangle(a: int, b: int, c: int) -> str:
    if a + b < c or b + c < a or c + a < b:
        return 'Invalid'
    if a == b == c:
        return 'Equilateral'
    if a == b and b != c or b == c and b != a or a == c and a != b:
        return 'Isosceles'
    if a != b and b != c and c != a:
        return 'Scalene'


print(triangle(2, 7, 12))
print(triangle(3, 3, 3))
print(triangle(12, 7, 12))
print(triangle(10, 5, 9))