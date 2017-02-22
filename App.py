from modules.tkinter import *
from modules.tkinter.font import Font
from Catalog import Catalog

class TopApp():
	'''More Info TopApp GUI class'''
	def __init__(self, top, ship):
		self.top = top
		self.top.title('%s Info' % ship['model'])

		font = Font(top, size=12)

		focusTitleLabel = Label(top, text='Focus:', justify=RIGHT, font=font)
		focusTitleLabel.grid(column=0, row=0, sticky=NE)

		focusLabel = Label(top, text=ship['focus'], justify=LEFT, font=font)
		focusLabel.grid(column=1, row=0, sticky=W)

		descTitleLabel = Label(top, text='Description:', justify=RIGHT, font=font)
		descTitleLabel.grid(column=0, row=1, sticky=NE)

		descLabel = Label(top, text=ship['description'], justify=LEFT, wraplength=500, font=font)
		descLabel.grid(column=1, row=1, sticky=W)

		top.mainloop()

class MainApp():
	'''Main Application GUI class

	TODO:
		Bind mousewheel to all scrollbars
	'''
	def __init__(self, root):
		self.catalog = Catalog()

		self.root = root
		self.root.title('Star Citizen Ship Catalog')

		font = Font(self.root, size=12)

		# Model Frame
		modelFrame = Frame(root)
		modelScrollbar = Scrollbar(modelFrame, orient=VERTICAL)
		modelListbox = Listbox(modelFrame, font=font, yscrollcommand=modelScrollbar.set)
		modelScrollbar.config(command=self.yview)
		modelListbox.bind('<Button-4>', self.onMouseWheel)
		modelListbox.bind('<Button-5>', self.onMouseWheel)
		for item in self.catalog.getAllOf('model', order='model'): modelListbox.insert(END, item)
		modelListbox.pack(side=LEFT)
		modelScrollbar.pack(side=RIGHT, fill=Y)
		modelFrame.grid(column=0, row=0)

		# Manufacturer Frame
		mfrFrame = Frame(root)
		mfrScrollbar = Scrollbar(mfrFrame, orient=VERTICAL)
		mfrListbox = Listbox(mfrFrame, font=font, yscrollcommand=mfrScrollbar.set)
		mfrScrollbar.config(command=self.yview)
		mfrListbox.bind('<Button-4>', self.onMouseWheel)
		mfrListbox.bind('<Button-5>', self.onMouseWheel)
		for item in self.catalog.getAllOf('manufacturer', order='model'): mfrListbox.insert(END, item)
		mfrListbox.pack(side=LEFT)
		mfrScrollbar.pack(side=RIGHT, fill=Y)
		mfrFrame.grid(column=1, row=0)
		
		# Production Status Frame
		prodstatFrame = Frame(root)
		prodstatScrollbar = Scrollbar(prodstatFrame, orient=VERTICAL)
		prodstatListbox = Listbox(prodstatFrame, font=font, yscrollcommand=prodstatScrollbar.set)
		prodstatScrollbar.config(command=self.yview)
		prodstatListbox.bind('<Button-4>', self.onMouseWheel)
		prodstatListbox.bind('<Button-5>', self.onMouseWheel)
		for item in self.catalog.getAllOf('production status', order='model'): prodstatListbox.insert(END, item)
		prodstatListbox.pack(side=LEFT)
		prodstatScrollbar.pack(side=RIGHT, fill=Y)
		prodstatFrame.grid(column=2, row=0)
		
		# Cargo Capacity Frame
		cargocapFrame = Frame(root)
		cargocapScrollbar = Scrollbar(cargocapFrame, orient=VERTICAL)
		cargocapListbox = Listbox(cargocapFrame, font=font, yscrollcommand=cargocapScrollbar.set)
		cargocapScrollbar.config(command=self.yview)
		cargocapListbox.bind('<Button-4>', self.onMouseWheel)
		cargocapListbox.bind('<Button-5>', self.onMouseWheel)
		for item in self.catalog.getAllOf('cargo capacity', order='model'): cargocapListbox.insert(END, item)
		cargocapListbox.pack(side=LEFT)
		cargocapScrollbar.pack(side=RIGHT, fill=Y)
		cargocapFrame.grid(column=3, row=0)
		
		# Max Crew Frame
		maxcrewFrame = Frame(root)
		maxcrewScrollbar = Scrollbar(maxcrewFrame, orient=VERTICAL)
		maxcrewListbox = Listbox(maxcrewFrame, font=font, yscrollcommand=maxcrewScrollbar.set)
		maxcrewScrollbar.config(command=self.yview)
		maxcrewListbox.bind('<Button-4>', self.onMouseWheel)
		maxcrewListbox.bind('<Button-5>', self.onMouseWheel)
		for item in self.catalog.getAllOf('max crew', order='model'): maxcrewListbox.insert(END, item)
		maxcrewListbox.pack(side=LEFT)
		maxcrewScrollbar.pack(side=RIGHT, fill=Y)
		maxcrewFrame.grid(column=4, row=0)

		self.listboxes = {
			'model' : modelListbox,
			'manufacturer' : mfrListbox,
			'production status' : prodstatListbox,
			'cargo capacity' : cargocapListbox,
			'max crew' : maxcrewListbox
		}

		# SortBy Label
		sortByLabel = Label(self.root, text='Sort By:', font=font)
		sortByLabel.grid(column=0, row=1, sticky=E)

		# SortBy OptionMenu
		sortOptions = ['Model', 'Manufacturer', 'Production Status', 'Cargo Capacity', 'Max Crew']
		self.sortOptionsVar = StringVar()
		self.sortOptionsVar.set(sortOptions[0])
		sortByMenu = OptionMenu(self.root, self.sortOptionsVar, *sortOptions, command=self.onSortByUpdate)
		sortByMenu.config(width=16, font=font)
		sortByMenu.grid(column=1, row=1)
		self.lastSelection = 'last'

		# More info Button
		moreInfoButton = Button(self.root, text='More Info', font=font, command=self.moreInfo)
		moreInfoButton.grid(column=2, row=1)

		self.root.mainloop()

	def yview(self, *args):
		for lb in self.listboxes.values():
			lb.yview(*args)

	def onMouseWheel(self, event):
		for lb in self.listboxes.values():
			lb.yview('scroll', event.delta, 'units')
		return "break"

	def onSortByUpdate(self, selection):
		if selection != self.lastSelection:
			for stat in self.listboxes.keys():
				self.listboxes[stat].delete(0, END)
				for item in self.catalog.getAllOf(stat, order=selection.lower()):
					self.listboxes[stat].insert(END, item)

	def moreInfo(self):
		index = 'no'
		for lb in self.listboxes.values():
			if lb.curselection():
				index = lb.curselection()[0]

		if index != 'no':
			sortBy = self.sortOptionsVar.get().lower()
			ship = list(self.catalog.allOrders[sortBy].values())[index]

			top = Toplevel()
			topApp = TopApp(top, ship)
			top.mainloop()

if __name__ == '__main__':
	root = Tk()
	mainApp = MainApp(root)
	root.mainloop()
