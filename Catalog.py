from modules.tkinter import *
from Ships import Ships

def main():
	def onSortByUpdate(sortSelection):
		global lastSortSelection
		if sortSelection != lastSortSelection:
			for stat in listboxes.keys():
				listboxes[stat].delete(0, END)
				for item in shipsObj.getAllOf(stat, order=sortSelection.lower()):
					listboxes[stat].insert(END, item)

		lastSortSelection = sortSelection

	def seeMoreInfo():
		shipsList = list(allShips.items())
		key = False
		for lb in listboxes.values():
			if lb.curselection():
				key = shipsList[lb.curselection()[0]][0] # key for ship
		
		if key:
			iRoot = Tk()
			iRoot.title('%s Info' % key)

			iRoot.mainloop()

	def yview(*args):
		modelListbox.yview(*args)
		mfrListbox.yview(*args)
		prodstatListbox.yview(*args)
		cargocapListbox.yview(*args)
		maxcrewListbox.yview(*args)

	shipsObj = Ships()
	allShips = shipsObj.byModel

	root = Tk()
	root.title('Star Citizen Ship Catalog')

	modelFrame = Frame(root)
	modelScrollbar = Scrollbar(modelFrame, orient=VERTICAL)
	modelListbox = Listbox(modelFrame, yscrollcommand=modelScrollbar.set)
	modelScrollbar.config(command=yview)
	for item in shipsObj.getAllOf('model', order='model'):
		modelListbox.insert(END, item)
	modelListbox.pack(side=LEFT)
	modelScrollbar.pack(side=RIGHT, fill=Y)
	modelFrame.grid(column=0, row=0)
	
	mfrFrame = Frame(root)
	mfrScrollbar = Scrollbar(mfrFrame, orient=VERTICAL)
	mfrListbox = Listbox(mfrFrame, yscrollcommand=mfrScrollbar.set)
	mfrScrollbar.config(command=yview)
	for item in shipsObj.getAllOf('manufacturer', order='model'):
		mfrListbox.insert(END, item)
	mfrListbox.pack(side=LEFT)
	mfrScrollbar.pack(side=RIGHT, fill=Y)
	mfrFrame.grid(column=1, row=0)
	
	prodstatFrame = Frame(root)
	prodstatScrollbar = Scrollbar(prodstatFrame, orient=VERTICAL)
	prodstatListbox = Listbox(prodstatFrame, yscrollcommand=prodstatScrollbar.set)
	prodstatScrollbar.config(command=yview)
	for item in shipsObj.getAllOf('production status', order='model'):
		prodstatListbox.insert(END, item)
	prodstatListbox.pack(side=LEFT)
	prodstatScrollbar.pack(side=RIGHT, fill=Y)
	prodstatFrame.grid(column=2, row=0)
	
	cargocapFrame = Frame(root)
	cargocapScrollbar = Scrollbar(cargocapFrame, orient=VERTICAL)
	cargocapListbox = Listbox(cargocapFrame, yscrollcommand=cargocapScrollbar.set)
	cargocapScrollbar.config(command=yview)
	for item in shipsObj.getAllOf('cargo capacity', order='model'):
		cargocapListbox.insert(END, item)
	cargocapListbox.pack(side=LEFT)
	cargocapScrollbar.pack(side=RIGHT, fill=Y)
	cargocapFrame.grid(column=3, row=0)
	
	maxcrewFrame = Frame(root)
	maxcrewScrollbar = Scrollbar(maxcrewFrame, orient=VERTICAL)
	maxcrewListbox = Listbox(maxcrewFrame, yscrollcommand=maxcrewScrollbar.set)
	maxcrewScrollbar.config(command=yview)
	for item in shipsObj.getAllOf('max crew', order='model'):
		maxcrewListbox.insert(END, item)
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
	sortByLabel = Label(root, text='Sort By:')
	sortByLabel.grid(column=0, row=1, sticky=E)

	# SortBy OptionMenu
	sortOptions = ['Model', 'Manufacturer', 'Production Status', 'Cargo Capacity', 'Max Crew']
	sortOptionsVar = StringVar()
	sortOptionsVar.set(sortOptions[0])
	sortByMenu = OptionMenu(root, sortOptionsVar, *sortOptions, command=onSortByUpdate)
	sortByMenu.config(width=16)
	sortByMenu.grid(column=1, row=1)
	global lastSortSelection
	lastSortSelection = 'last'

	# See info Button
	seeInfoButton = Button(root, text='See More Info', command=seeMoreInfo)
	seeInfoButton.grid(column=2, row=1)

	root.mainloop()

if __name__ == "__main__":
    main()
