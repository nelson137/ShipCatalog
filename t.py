def f1():
	def f2():
		def f3():
			print(x)

	x = 4
	f3()

f1()