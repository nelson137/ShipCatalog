from modules.tkinter import *
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

	# Model Listbox
	modelListbox = Listbox(root)
	for item in ships.getAllOf('model'):
		modelListbox.insert(END, item)
	modelListbox.grid(column=0, row=0, padx=(0,5), pady=(5,5))

	# Manufacturer Listbox
	mfrListbox = Listbox(root)
	for item in ships.getAllOf('manufacturer'):
		mfrListbox.insert(END, item)
	mfrListbox.grid(column=1, row=0, padx=(0,5), pady=(5,5))

	# Production Status Listbox
	prodstatListbox = Listbox(root, width=12)
	for item in ships.getAllOf('production status'):
		prodstatListbox.insert(END, item)
	prodstatListbox.grid(column=2, row=0, padx=(0,5), pady=(5,5))

	# Cargo Capacity Listbox
	cargocapListbox = Listbox(root, width=7)
	for item in ships.getAllOf('cargo capacity'):
		cargocapListbox.insert(END, item)
	cargocapListbox.grid(column=3, row=0, padx=(0,5), pady=(5,5))

	# Max Crew Listbox
	maxcrewListbox = Listbox(root, width=7)
	for item in ships.getAllOf('max crew'):
		maxcrewListbox.insert(END, item)
	maxcrewListbox.grid(column=4, row=0, padx=(0,5), pady=(5,5))

	# Drop down menu
	sortOptions = ['Choose One', 'Model', 'Manufacturer', 'Production Status', 'Cargo Capacity', 'Max Crew']
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
