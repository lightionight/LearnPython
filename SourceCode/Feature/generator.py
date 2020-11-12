# generator is time space trade-off expression
# the data iff creating when we using it.
# list列表可以通过储存的表达式 当需要这个元素的时候 计算它 并输出
l = [x * x for x in range(10)]
g = (x * x for x in range(10))

# l is list, will store every element. can read fast but need more data space
# g is generator ,will not store any element , not need data space but when using element need time to calculator.

for n in g:
    print(n)