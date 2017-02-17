from Ships import Ships
from tkinter import *
from subprocess import *

def main():
	def outputTk():
		'''GUI for Catalog output'''
		rootOut = Tk()
		rootOut.title('Output')

		canvasOut = Canvas(rootOut, width=720, height=480)
		canvasOut.grid()

		rootOut.mainloop()

	def onSortByUpdate(x):
		print('updated')

	def setText():
		global lastListSelection, listSelection
		try:
			listSelection = listbox1.get(listbox1.curselection())
			if listSelection != lastListSelection:
				text.config(text=listbox1.get(listbox1.curselection()))
			lastListSelection = listSelection
		except: pass

	ps_aux = Popen(['ps'], stdout=PIPE, shell=True).communicate()[0].decode()
	print(ps_aux)

	ships = Ships()

	root = Tk()
	root.title('Star Citizen Ship Catalog')

	# Canvas
	canvas = Canvas(root, width=720, height=480)
	canvas.grid()

	# Drop down menu
	sortOptions = ['Chose One', 'Model', 'Manufacturer', 'Production Status', 'Cargo Capacity', 'Max Crew']
	var = StringVar()
	var.set(sortOptions[0])
	sortByMenu = OptionMenu(root, var, *sortOptions, command=onSortByUpdate)
	sortByMenu.config(width=16)
	canvas.create_window(500,100, window=sortByMenu)

	# Lisboxes Frame
	frame = Frame(root)
	canvas.create_window(10,10, window=frame, anchor=NW)

	# Listbox 1
	listbox1 = Listbox(frame, width=10)
	for item in ['one', 'three', 'two', 'zero', 'four']:
		listbox1.insert(END, item)
	listbox1.pack(side=LEFT)
	global lastListSelection, listSelection
	lastListSelection = 'last'
	listSelection = 'current'


	# Listbox 2
	listbox2 = Listbox(frame)
	for item in ['0', '1', '2', '3', '4']:
		listbox2.insert(END, item)
	listbox2.pack(side=RIGHT)

	# Label
	text = Label(root, text=sortOptions[0])
	canvas.create_window(10,200, window=text, anchor=NW)

	# Set Text button
	setTextButton = Button(root, text='Set Text', command=setText)
	canvas.create_window(10,250, window=setTextButton, anchor=NW)

	def quit():
		pass

	quitButton = Button(root, text='Quit', command=quit)
	canvas.create_window(10,canvas.winfo_width()-10, window=quitButton, anchor=SW)

	root.mainloop()

if __name__ == "__main__":
    main()
