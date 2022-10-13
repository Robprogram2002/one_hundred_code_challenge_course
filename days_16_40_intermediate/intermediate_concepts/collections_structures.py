from collections import Counter, namedtuple, deque, defaultdict, OrderedDict

# collections are apply to iterables

# ***** Counter
word = "aaaaabbbbccccdd"
word_counter = Counter(word)
print(word_counter)
print(word_counter.most_common(2))  # get the most common / most present elements in the counter
print(list(word_counter.elements()))

# **** Named Tuple
Point = namedtuple("Point", "x,y")
new_point = Point(3, -8)
print(new_point)

