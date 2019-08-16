full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("    leonhard", "EULER "))
# sorted by last name authors list
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein",
"Arthur C. Clarke", "Douglas Adams", "Leigh Brackett"]
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)


def build_quadratic_function(a, b, c):
	"""Returns the function f(x) = ax^2 + bx + c"""
	return lambda x: a*x**2 + b*x + c


f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(3))
print('-----------------')
f1 = build_quadratic_function(3, 0, 1)
print(f1(2))
print("Compare to:")
print(build_quadratic_function(3, 0, 1)(2))
