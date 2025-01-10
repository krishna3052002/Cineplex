class Star_Cinema:
   hall_list=[]
   def __init__(self):
      pass 
   def entry_hall(self,hall):
       self.hall_list.append(hall)
 
class Hall:
    def __init__(self,rows,cols,hall_no):
        self.__seats={}
        self.show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.hall_no=hall_no

    def entry_show(self,id,movie_name,time):
        show=(id,movie_name,time)
        self.show_list.append(show)
        arr = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id]=arr
    def book_seats(self,id,selected_seats):
        for item in selected_seats:
            r=item[0]
            c=item[1]
            try:
                 if self.__seats[id][r][c]==0:
                     self.__seats[id][r][c]=1
                     print(f'{r,c}Seat booked successfully')
                 else:
                     print(f'{r,c}Seat is not available')
            except:
                print("invalid index")
    def view_show_list(self):
        if self.show_list :
            for item in self.show_list:
                print(f'Id:{item[0]} Movie Name:{item[1]} Time:{item[2]}')
                

    def view_available_seats(self,id):
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(f'{self.__seats[id][i][j]}',end=" ")
            print()
     
    
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
star_cinema.entry_hall(hall1)
star_cinema.entry_hall(hall2)
star_cinema.entry_hall(hall3)
star_cinema.entry_hall(hall4)
star_cinema.entry_hall(hall5)


while True:       
     print(f'1. VIEW ALL SHOW')
     print(f'2. VIEW AVAILABLE SEATS')
     print(f'3. BOOK TICKET')
     print(f'4. EXIT')
     print(f'ENTER OPTION:',end=" ")
     choice=int(input())

 # print(type(choice))
     if choice == 1:
       print(f'All Show List Today:')
       for hall in star_cinema.hall_list:
           hall.view_show_list()
           print("-" * 45) 
        
     elif choice==2:
        print(f'Please Enter Show ID:',end=" ")
        id=int(input())
        flag=False
        for hall in star_cinema.hall_list:
            for show in hall.show_list:
                 if show[0]==id:
                     print(f'Available seats(where 0):')
                     hall.view_available_seats(id)
                     flag=True
                     break
        if flag==False:
            print(f'Invalid ID') 
     elif choice==3:
         print(f'Enter ID:',end=" ")
         id=int(input())
         print(f'Number of tickets:',end=" ")
         t_quantity=int(input())
         seat_list=[]
         flag=False
         for i in range(t_quantity):
             print(f'Enter seat row:',end=" ")
             row=int(input())
             print(f'Enter seat column:',end=" ")
             col=int(input())
             seat_list.append((row,col))
        
         for hall in star_cinema.hall_list:
            for show in hall.show_list:
                if show[0]==id:
                    hall.book_seats(id,seat_list)
                    flag=True
                    break
         if flag==False:
            print("Invalid ID")
     elif choice==4:
         break
    

    
