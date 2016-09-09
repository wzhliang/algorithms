def strinify(fn):
	def wrapper(*args):
		r = fn(*args)
		return [str(x) for x in r]
	return wrapper


@strinify
def coins(amount, denom, pay):
	if amount == 0:
		return pay
	if amount < 0:
		raise Value("Unable to do it")
	r = [x for x in denom if x <= amount]
	pay.append(r[0])
	amount -= r[0]
	return coins(amount, r, pay)


if __name__ == '__main__':
	denom = [1000, 500, 50, 10, 5, 2, 1]
	fmt = "{}: {}"
	values = [50, 1557, 7745, 8129]
	for v in values:
		print(fmt.format(v, " + ".join(coins(v, denom, []))))
