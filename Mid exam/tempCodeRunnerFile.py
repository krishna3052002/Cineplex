class Star_Cinema:
   hall_list=[]
   def __init__(self):
      pass 
   def entry_hall(self,*hall):
       self.hall_list.append(hall)
 
class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no

    def entry_show(self,id,movie_name,time):
        show=(id,movie_name,time)
        self.show_list.append(show)
        arr = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id]=arr
    def book_seats(self,id,selected_seats):
        for item in selected_seats:
            r=item[0]
            c=item[1]
            if self.seats[id][r][c]==0:
                self.seats[id][r][c]=1
                print(f'{r,c}Seat booked successfully')
            else:
                print(f'{r,c}Seat is not available')
    def view_show_list(self):
        if self.show_list :
            for item in self.show_list:
                print(item)
    def view_available_seats(self,id):
        print(self.seats[id])
     
    
hall1=Hall(5,5,1)
hall2=Hall(6,6,2)
hall3=Hall(8,8,3)
hall4=Hall(5,5,4)
hall5=Hall(6,6,5)

hall1.entry_show(20251,"The Way Down","05:10pm")
hall1.entry_show(20252,"Tenet","08:10pm")
hall1.entry_show(20251,"The Way Down","11:10am")

hall2.entry_show(10251,"Lucky Vashkar","05:10pm")
hall2.entry_show(10252,"Pirates","08:10pm")
hall2.entry_show(10251,"The Way Down","11:10am")

hall3.entry_show(30251,"The Way Down","05:10pm")
hall3.entry_show(30252,"Tenet","08:10pm")
hall3.entry_show(30251,"The Way Down","11:10am")

hall4.entry_show(40251,"The Way Down","05:10pm")
hall4.entry_show(40252,"Tenet","08:10pm")
hall4.entry_show(40251,"The Way Down","11:10am")

hall5.entry_show(50251,"The Way Down","05:10pm")
hall5.entry_show(50252,"Tenet","08:10pm")
hall5.entry_show(50251,"The Way Down","11:10am")

star_cinema=Star_Cinema()
star_cinema.entry_hall(hall1,hall2,hall3,hall4,hall5)
print(star_cinema.hall_list)