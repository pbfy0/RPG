import functools
def arg_deco(func):
	def _wrap(*args, **kwargs):
		@functools.wraps(func)
		def _wrap2(val):
			return func(val, *args, **kwargs)
		return _wrap2
	return _wrap

@arg_deco
def name(x, n):
	x.__name__ = n
	return x

def prompt(prompt, valid):
	v = input(prompt)
	t = '... '.rjust(len(prompt))
	while not v in valid:
		v = input(t)
	return valid[v]