from tkinter import *
from Ships import Ships

def main():
	def onSortByUpdate(sortSelection):
		global lastSortSelection
		if sortSelection != lastSortSelection and sortSelection != 'Choose One':
			pass
		lastSortSelection = sortSelection

	def setText():
		global lastListSelection, listSelection
		try:
			listSelection = listbox1.get(listbox1.curselection())
			if listSelection != lastListSelection:
				text.config(text=listbox1.get(listbox1.curselection()))
			lastListSelection = listSelection
		except: pass

	ships = Ships()

	root = Tk()
	root.title('Star Citizen Ship Catalog')

	# Listbox 1
	listbox1 = Listbox(root)
	for item in ['one', 'three', 'two', 'zero', 'four']:
		listbox1.insert(END, item)
	listbox1.grid(column=0, row=0, padx=(5,0), pady=(5,5))
	global lastListSelection, listSelection
	lastListSelection = 'last'
	listSelection = 'current'

	# Listbox 2
	listbox2 = Listbox(root)
	for item in ['0', '1', '2', '3', '4']:
		listbox2.insert(END, item)
	listbox2.grid(column=1, row=0, padx=(0,5), pady=(5,5))

	# Drop down menu
	sortOptions = ['Choose One', 'model', 'manufacturer', 'production status', 'cargo capacity', 'max crew']
	var = StringVar()
	var.set(sortOptions[0])
	sortByMenu = OptionMenu(root, var, *sortOptions, command=onSortByUpdate)
	sortByMenu.config(width=16)
	sortByMenu.grid(column=0, row=1, padx=(5,5), pady=(0,5))
	global lastSortSelection
	lastSortSelection = 'last'

	root.mainloop()

if __name__ == "__main__":
    main()
