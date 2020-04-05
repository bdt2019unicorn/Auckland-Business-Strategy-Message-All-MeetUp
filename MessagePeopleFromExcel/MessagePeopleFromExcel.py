from openpyxl import load_workbook
from openpyxl.styles import Color, PatternFill, Font, Border
import openpyxl.styles
import ContactLink


ContactLink.ColdMessage()



#filename = "auckland bussiness strategies.xlsx"
#contact_number = 10 

#mark_contacted_fill_yellow = PatternFill("solid", openpyxl.styles.colors.YELLOW)
#mark_contacted_fill_blue = PatternFill("solid", openpyxl.styles.colors.BLUE)

#workbook = load_workbook(filename)
#worksheet = workbook.active 

#def firstnoncontactcell(): 
#    count = 2 
#    while True: 
#        cell_fill = worksheet["a"+str(count)].fill
#        cell_value = worksheet["a"+str(count)].value.strip()
#        if(cell_fill.fgColor.rgb == openpyxl.styles.colors.BLACK) or (not isinstance(cell_fill.fgColor.rgb,str)) or (cell_value==""): 
#            break
#        count+=1
#    return count 

#count = firstnoncontactcell()
#ContactLink.LoginMeetUp()

#end_of_loop = count+contact_number
#while(count<end_of_loop) and (worksheet["A"+str(count)].value.strip()!=""): 
#    cell_value = worksheet["A"+str(count)].value.strip()
#    print(cell_value)
#    ContactLink.MessagePeople(cell_value)
#    count+=1














#worksheet["A2"].fill = mark_contacted_fill_yellow
#workbook.save(filename)



#redFill = PatternFill("solid", openpyxl.styles.colors.BLUE)

#worksheet['A2'].fill = redFill
#workbook.save(filename)

#value = worksheet["A2"].value 


##print(value)
#print("*****************************************************")
#print(fill_a2)
#print("*******************************************************")
#print("------------------------------------------------------")
#if(fill_a2.fgColor.rgb == openpyxl.styles.colors.GREEN): 
#    print("This is the blue color")
#print("------------------------------------------------------")

#print(fill_a3)

#if(fill_a3.fgColor.rgb == openpyxl.styles.colors.BLACK): 
#    print("I HAVE NO COLOR")
#excel_file = pandas.read_excel("Auckland Bussiness Strategies.xlsx")

#print(excel_file)
