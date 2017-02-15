from Ships import Ships
from tkinter import Tk, Canvas, StringVar, OptionMenu, Listbox, END

def main():
	def outputTk():
		'''GUI for Catalog output'''
		rootOut = Tk()
		rootOut.title('Output')

		canvasOut = Canvas(rootOut, width=720, height=480)
		canvasOut.grid()

		rootOut.mainloop()

	ships = Ships()

	root = Tk()
	root.title('Star Citizen Ship Catalog')

	canvas = Canvas(root, width=720, height=480)
	canvas.grid()

	orderOptions = ['Chose One', 'Model', 'Manufacturer', 'Production Status', 'Cargo Capacity', 'Max Crew']
	var = StringVar(root)
	var.set(orderOptions[0])
	orderByMenu = OptionMenu(root, var, *orderOptions)
	canvas.create_window(100,100, window=orderByMenu)

	outputListbox = Listbox(root)
	for item in ['one', 'three', 'two', 'zero', 'four']:
		outputListbox.insert(END, item)
	canvas.create_window(250,100, window=outputListbox)

	root.mainloop()

if __name__ == "__main__":
    main()
