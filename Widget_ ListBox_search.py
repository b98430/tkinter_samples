"""

"""
from tkinter import *

main_window = Tk()

actual_screen_width = main_window.winfo_screenwidth()
actual_screen_height = main_window.winfo_screenheight()

minimum_screen_width = 1200
minimum_screen_height = 600

x_position = int((actual_screen_width/2)-(minimum_screen_width/2))
y_position = int((actual_screen_height/2)-(minimum_screen_height/2))-10

main_window.geometry("{}x{}+{}+{}".format(minimum_screen_width,minimum_screen_height,x_position,y_position))
main_window.resizable(0,0)

frame_top = Frame(main_window,bg="white").pack(fill= BOTH,expand=1)

label_search = Label(frame_top,text="Search Word :",bg= "white",fg="black",font=("caliber",10,"bold"))\
			   .place(x=10,y=10)
search_var = StringVar()
entry_search = Entry(frame_top,textvariable = search_var,width = 30,relief="groove",bd=2,\
	               font=("caliber",12,"bold"),fg = "red")
entry_search.place(x=105,y=10)
entry_search.focus_set()

label_listbox_master = Label(frame_top,text="Master List Box",bg="white",fg="blue",font=("caliber",10,"bold"))\
					   .place(x=10,y=40)
listbox_master = Listbox(frame_top,width = 45, height =10,relief="groove",bd=2,selectmode="single")
listbox_master.place(x=10,y=60)

scrollbar = Scrollbar(listbox_master,orient="vertical")
scrollbar.config(command=listbox_master.yview)
scrollbar.place(bordermode=INSIDE,relheight = 1.0,x=253)
listbox_master.config(yscrollcommand=scrollbar.set)

label_listbox_start = Label(frame_top,text="Items Starts With",bg="white",fg="green",font=("caliber",10,"bold"))\
					  .place(x=300,y=40)
listbox_starts = Listbox(frame_top,width=45,height=30,relief="groove",bd=2,selectmode="single")
listbox_starts.place(x=300,y=60)

label_listbox_ends = Label(frame_top,text="Items Ends With",bg="white",fg="red",font=("caliber",10,"bold"))\
					 .place(x=590,y=40)
listbox_ends= Listbox(frame_top,width=45,height=30,relief="groove",bd=2,selectmode="single")
listbox_ends.place(x=590,y=60)

label_listbox_contains = Label(frame_top,text="Items contains anywhere",bg="white",fg="black",\
						 font=("caliber",10,"bold")).place(x=880,y=40)
listbox_contains = Listbox(frame_top,width=45,height=30,relief="groove",bd=2,selectmode="single")
listbox_contains.place(x=880,y=60)

lst_items = ['Balaji','Balamurugan','Aruthra','Arumugam','SaiRithika','Saravanan','balaji_001',
                    'Balaji_002','Balaji_150','Balaji_200','Balaji_210','Balaji_220','zebra','x-ray']

for i in lst_items:
	listbox_master.insert(END,i)

def filter_listbox(*args):
	search_var.set(search_var.get().capitalize())
	search_item = (search_var.get())
	search_item_length = len(search_item)
	
	listbox_starts.delete(0,"end")
	listbox_ends.delete(0,"end")
	listbox_contains.delete(0,"end")

	for item_in_listbox in listbox_master.get(0,"end"):
		if search_item.lower() == item_in_listbox[:search_item_length].lower():
			for j in item_in_listbox:
				listbox_starts.insert(END,item_in_listbox)
				if search_item_length==0:
					listbox_starts.delete(0,"end")
				break
	
		if search_item.lower() == item_in_listbox[(-search_item_length):].lower():
			for j in item_in_listbox:
				listbox_ends.insert(END,item_in_listbox)
				if search_item_length==0:
					listbox_ends.delete(0,"End")
				break

		if search_item_length != 0 :
			temp_var = item_in_listbox.lower().find(search_item.lower(),0,(len(item_in_listbox)))
			if temp_var != -1:
				for j in item_in_listbox:
					listbox_contains.insert(END,item_in_listbox)
					if search_item_length==0:
						listbox_contains.delete(0,"End")
					break
	 
search_var.trace("w",filter_listbox)

main_window.mainloop()
