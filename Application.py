from modules.tkinter import *
from modules.tkinter.font import Font
from Catalog import Catalog
from App import TopApp

def main():
	def onSortByUpdate(sortSelection):
		global lastSortSelection
		if sortSelection != lastSortSelection:
			for stat in listboxes.keys():
				listboxes[stat].delete(0, END)
				for item in catalog.getAllOf(stat, order=sortSelection.lower()):
					listboxes[stat].insert(END, item)

		lastSortSelection = sortSelection

	def moreInfo():
		index = 'no'
		for lb in listboxes.values():
			if lb.curselection():
				index = lb.curselection()[0]

		if index != 'no':
			sortBy = sortOptionsVar.get().lower()
			ship = list(catalog.allOrders[sortBy].values())[index]

			top = Toplevel()
			topApp = TopApp(top, ship)
			top.mainloop()

	def yview(*args):
		modelListbox.yview(*args)
		mfrListbox.yview(*args)
		prodstatListbox.yview(*args)
		cargocapListbox.yview(*args)
		maxcrewListbox.yview(*args)

	catalog = Catalog()

	root = Tk()
	root.title('Star Citizen Ship Catalog')

	font = Font(root, size=12)

	# Model Frame
	modelFrame = Frame(root)
	modelScrollbar = Scrollbar(modelFrame, orient=VERTICAL)
	modelListbox = Listbox(modelFrame, font=font, yscrollcommand=modelScrollbar.set)
	modelScrollbar.config(command=yview)
	for item in catalog.getAllOf('model', order='model'): modelListbox.insert(END, item)
	modelListbox.pack(side=LEFT)
	modelScrollbar.pack(side=RIGHT, fill=Y)
	modelFrame.grid(column=0, row=0)

	# Manufacturer Frame
	mfrFrame = Frame(root)
	mfrScrollbar = Scrollbar(mfrFrame, orient=VERTICAL)
	mfrListbox = Listbox(mfrFrame, font=font, yscrollcommand=mfrScrollbar.set)
	mfrScrollbar.config(command=yview)
	for item in catalog.getAllOf('manufacturer', order='model'): mfrListbox.insert(END, item)
	mfrListbox.pack(side=LEFT)
	mfrScrollbar.pack(side=RIGHT, fill=Y)
	mfrFrame.grid(column=1, row=0)
	
	# Production Status Frame
	prodstatFrame = Frame(root)
	prodstatScrollbar = Scrollbar(prodstatFrame, orient=VERTICAL)
	prodstatListbox = Listbox(prodstatFrame, font=font, yscrollcommand=prodstatScrollbar.set)
	prodstatScrollbar.config(command=yview)
	for item in catalog.getAllOf('production status', order='model'): prodstatListbox.insert(END, item)
	prodstatListbox.pack(side=LEFT)
	prodstatScrollbar.pack(side=RIGHT, fill=Y)
	prodstatFrame.grid(column=2, row=0)
	
	# Cargo Capacity Frame
	cargocapFrame = Frame(root)
	cargocapScrollbar = Scrollbar(cargocapFrame, orient=VERTICAL)
	cargocapListbox = Listbox(cargocapFrame, font=font, yscrollcommand=cargocapScrollbar.set)
	cargocapScrollbar.config(command=yview)
	for item in catalog.getAllOf('cargo capacity', order='model'): cargocapListbox.insert(END, item)
	cargocapListbox.pack(side=LEFT)
	cargocapScrollbar.pack(side=RIGHT, fill=Y)
	cargocapFrame.grid(column=3, row=0)
	
	# Max Crew Frame
	maxcrewFrame = Frame(root)
	maxcrewScrollbar = Scrollbar(maxcrewFrame, orient=VERTICAL)
	maxcrewListbox = Listbox(maxcrewFrame, font=font, yscrollcommand=maxcrewScrollbar.set)
	maxcrewScrollbar.config(command=yview)
	for item in catalog.getAllOf('max crew', order='model'): maxcrewListbox.insert(END, item)
	maxcrewListbox.pack(side=LEFT)
	maxcrewScrollbar.pack(side=RIGHT, fill=Y)
	maxcrewFrame.grid(column=4, row=0)

	listboxes = {
		'model' : modelListbox,
		'manufacturer' : mfrListbox,
		'production status' : prodstatListbox,
		'cargo capacity' : cargocapListbox,
		'max crew' : maxcrewListbox
	}

	# SortBy Label
	sortByLabel = Label(root, text='Sort By:', font=font)
	sortByLabel.grid(column=0, row=1, sticky=E)

	# SortBy OptionMenu
	sortOptions = ['Model', 'Manufacturer', 'Production Status', 'Cargo Capacity', 'Max Crew']
	sortOptionsVar = StringVar()
	sortOptionsVar.set(sortOptions[0])
	sortByMenu = OptionMenu(root, sortOptionsVar, *sortOptions, command=onSortByUpdate)
	sortByMenu.config(width=16, font=font)
	sortByMenu.grid(column=1, row=1)
	global lastSortSelection
	lastSortSelection = 'last'

	# More info Button
	moreInfoButton = Button(root, text='More Info', font=font, command=moreInfo)
	moreInfoButton.grid(column=2, row=1)

	root.mainloop()

if __name__ == "__main__":
    main()
