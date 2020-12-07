#Custom For Loop using iterators

def my_for_loop(iterable, func):
	iterator = iter(iterable)

	try:
		thing = next(iterator)
	except StopIteration as e:
		break
	else:
		func(thing)


my_for_loop('Hello', print)