# Imported numpy
import numpy as np

# Imported pandas
import pandas as pd

# Imported csv
import csv

# Import matplotlib pyplot
import matplotlib.pyplot as plt


# Imported plotly express
import plotly.express as px

# Imported plotly graph objects
import plotly.graph_objects as go

# Imported subplots
from plotly.subplots import make_subplots

# Imported seaborn
import seaborn as sns

# Imported plotlyio
import plotly.io as pio
#imported tabulate
from tabulate import tabulate
#imported sklearn
import sklearn 

from math import pi


#to set deafult renders as browsers
pio.renderers.default = "browser"

#to set seaborn background for presentation
sns.set_style("dark")



#creating a dataframe from the csv file
soft_df = pd.read_csv (r"E:\School Project\Phone comparator\phone_data.csv")
display_df = soft_df.groupby(["Sno", "Name", "Processor"])[["Ram", "Performance", "Battery Capacity"]].sum().reset_index()

compare_df = soft_df.groupby(["Sno", "Name","Processor"])[["Performance","Battery Capacity","Front Camera","Back Camera","Screen Size"]].sum().reset_index()
print(tabulate(display_df, headers='keys', tablefmt='fancy_grid'))
#classifying them as seperate brands for better comparison
apple = soft_df[(soft_df["Cno"]==123)]
samsung = soft_df[(soft_df["Cno"]==223)]
oneplus = soft_df[(soft_df["Cno"]==323)]
google = soft_df[(soft_df["Cno"]==423)]

#created a function  to compare by antutu score 
def filterbyantutuscore():
    #to group the data 
    antutu_filter_comp_df = soft_df.groupby(["Sno", "Name"])["Performance"].sum().reset_index() 
    print(tabulate(antutu_filter_comp_df, headers='keys', tablefmt='fancy_grid'))
    #to set seaborn background for presentation
    sns.set_style("darkgrid")
    #plotting the graph
    plt.bar (x = soft_df['Name'],height = soft_df['Performance'] )
    plt.title("Antutu Score Comparison")
    plt.xlabel("Name")
    plt.ylabel("Performance")
    plt.xticks(rotation=90)
    plt.style.use("seaborn-dark")

    #to display the plot
    plt.show()
    
#created a function  to compare by battery score 
def filterbyBattery():
    #to group the data 
    Battery_filter_comp_df = soft_df.groupby(["Sno", "Name"])["Battery Capacity"].sum().reset_index()
    print(tabulate(Battery_filter_comp_df, headers='keys', tablefmt=''))
    #to set seaborn background for presentation
    sns.set_style("darkgrid")
    plt.bar(x = soft_df['Name'],height = soft_df['Battery Capacity'])
    plt.title("Battery Capacity Comparison")
    plt.xlabel("Name")
    plt.ylabel("Battery(mAh)")
    plt.xticks(rotation=90)

    #to display the plot
    plt.show()
#created a function  to compare company wise
def companywise():
    # to get the input of the user
    brand = input("Enter the company name which you want to compare : ")
    
    #if condition if the user wants to compare apple phones
    if (brand == "apple") :
        #to group the data
        apple_filter_comp_df = apple.groupby(["Name","Processor","Performance"])[["Ram","Front Camera","Back Camera","Screen Size","Battery Capacity"]].sum().reset_index()
        print(tabulate(apple_filter_comp_df, headers='keys', tablefmt='fancy_grid'))
        apple_num_cols = apple_filter_comp_df.select_dtypes(exclude=[object]).columns
        apple_df = apple.groupby(["Name"])[apple_num_cols].sum().round(1).reset_index()
        i = j = 1
        #to create empty subplots
        fig = make_subplots(rows=4, cols=4,
                            shared_xaxes=False,
                            vertical_spacing=0.1,
                            subplot_titles=apple_num_cols)
        #to create bar plots
        for col in apple_num_cols:
             fig.add_trace(go.Bar(x=apple_df["Name"],
                                 y=apple_df[col],
                                 text=apple_df[col],
                                 textposition="inside",
                                 
                                 name=col), 
                        row=i, col=j)
                        
                        
             j += 1
             if j > 4:
                 j = 1
                 i += 1
             if i > 4:
                 i = 1
        fig.update_layout(height=800)

        #to display the plot
        fig.show()

        
        
     #if condition if the user wants to compare samsung
    elif (brand=="samsung"):
        #to group the data
         samsung_filter_comp_df = samsung.groupby(["Sno", "Name","Processor","Performance"])[["Ram","Front Camera","Back Camera","Screen Size","Battery Capacity"]].sum().reset_index()
         print(tabulate(samsung_filter_comp_df, headers='keys', tablefmt='fancy_grid'))
         samsung_num_cols = samsung_filter_comp_df.select_dtypes(exclude=[object]).columns
         samsung_df = samsung.groupby(["Name"])[samsung_num_cols].sum().round(1).reset_index()
         i = j = 1
         #to create empty subplots
         fig = make_subplots(rows=4, cols=4,
                            shared_xaxes=False,
                            vertical_spacing=0.1,
                            subplot_titles=samsung_num_cols)
          #to create bar plots
         for col in samsung_num_cols:
             fig.add_trace(go.Bar(x=samsung_df["Name"],
                                 y=samsung_df[col],
                                 text=samsung_df[col],
                                 textposition="inside",
                                 
                                 name=col), 
                        row=i, col=j)
                        
                        
             j += 1
             if j > 4:
                 j = 1
                 i += 1
             if i > 4:
                 i = 1
         fig.update_layout(height=800)

         #to display the plot
         fig.show()

         
    #if condition if the user wants to compare one plus
    elif (brand=="one plus"):
        
        #to group the data
        oneplus_filter_comp_df = oneplus.groupby(["Name","Processor","Performance"])[["Ram","Front Camera","Back Camera","Screen Size","Battery Capacity"]].sum().reset_index()
        print(tabulate(oneplus_filter_comp_df, headers='keys', tablefmt='fancy_grid'))
        oneplus_num_cols = oneplus_filter_comp_df.select_dtypes(exclude=[object]).columns
        oneplus_df = oneplus.groupby(["Name"])[oneplus_num_cols].sum().round(1).reset_index()
        i = j = 1
        #to create empty subplots
        fig = make_subplots(rows=4, cols=4,
                            shared_xaxes=False,
                            vertical_spacing=0.1,
                            subplot_titles=oneplus_num_cols)
        #to create bar plots
        for col in oneplus_num_cols:
             fig.add_trace(go.Bar(x=oneplus_df["Name"],
                                 y=oneplus_df[col],
                                 text=oneplus_df[col],
                                 textposition="inside",
                                 
                                 name=col), 
                        row=i, col=j)
                        
                        
             j += 1
             if j > 4:
                 j = 1
                 i += 1
             if i > 4:
                 i = 1
        fig.update_layout(height=800)

        #to display the plot
        fig.show()
 #if condition if the user wants to compare google
    elif (brand=="google"):
        
        #to group the data
        google_filter_comp_df = google.groupby(["Name","Processor","Performance"])[["Ram","Front Camera","Back Camera","Screen Size","Battery Capacity"]].sum().reset_index()
        print(tabulate(google_filter_comp_df, headers='keys', tablefmt='fancy_grid'))
        google_num_cols = google_filter_comp_df.select_dtypes(exclude=[object]).columns
        google_df = google.groupby(["Name"])[google_num_cols].sum().round(1).reset_index()
        i = j = 1
        #to create empty subplots
        fig = make_subplots(rows=4, cols=4,
                            shared_xaxes=False,
                            vertical_spacing=0.1,
                            subplot_titles=google_num_cols)
        #to create bar plots
        for col in google_num_cols:
             fig.add_trace(go.Bar(x=google_df["Name"],
                                 y=google_df[col],
                                 text=google_df[col],
                                 textposition="inside",
                                 
                                 name=col), 
                        row=i, col=j)
                        
                        
             j += 1
             if j > 4:
                 j = 1
                 i += 1
             if i > 4:
                 i = 1
        fig.update_layout(height=800)

        #to display the plot
        fig.show()

    
    #else condition if the user entered wrong company name or unavailable 
    else:
        print('Unavailable')

        
#function for comparing phones individually
def comparephones():
    
    ask=input("How many phones do you want to compare(Min-1 Max-5) \nEnter The Number of phones to be compared(enter the number in words) : ")
    if(ask=="one"):
        user_phone_one=int(input("Enter the Sno of the Phone u want to compare : "))
        col =["Performance","Battery Capacity","Front Camera","Back Camera","Screen Size"]  
        
        
      
       
        tocompareone=(compare_df.loc[(compare_df["Sno"] == user_phone_one)])
    
        cols_for_radar = tocompareone[col]
        print(tabulate(tocompareone, headers='keys', tablefmt='fancy_grid')+" - Red")
        compare_one = {'Performance':(tocompareone["Performance"])/10000,'Battery Capacity':(tocompareone["Battery Capacity"])/100,'Front Camera':(tocompareone["Front Camera"]),'Back Camera':(tocompareone["Back Camera"]),'Screen Size':(tocompareone["Screen Size"])}
        data = pd.DataFrame([compare_one], index = [tocompareone["Name"]])
        

                               
        Attributes =list(data)
        AttNo = len(Attributes)
        values = data.iloc[0].tolist()

        values += values [:1]
        
        angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles += angles [:1]
        ax = plt.subplot(111, polar=True)
        #Add the attribute labels to our axes
        plt.xticks(angles[:-1],Attributes)

#Plot the line around the outside of the filled area, using the angles and values calculated before
        ax.plot(angles,values)

#Fill in the area plotted in the last line
        ax.fill(angles, values, 'red', alpha=0.1)
        #Give the plot a title and show it
        ax.set_title("Phone Comparator")
        plt.show()
    elif(ask=="two"):
        user_phone_two_one=int(input("Enter the Sno of the Phone u want to compare : "))
        user_phone_two_two=int(input("Enter the Sno of the Phone u want to compare : "))
        col =["Performance","Battery Capacity","Front Camera","Back Camera","Screen Size"]        
        tocomparetwo_one=(compare_df.loc[(compare_df["Sno"] == user_phone_two_one)])
        tocomparetwo_two=(compare_df.loc[(compare_df["Sno"] == user_phone_two_two)])
        dispdata = pd.concat([tocomparetwo_one, tocomparetwo_two], ignore_index=True)

        
        compare_two_one = {'Performance':(tocomparetwo_one["Performance"])/10000,'Battery Capacity':(tocomparetwo_one["Battery Capacity"])/100,'Front Camera':(tocomparetwo_one["Front Camera"]),'Back Camera':(tocomparetwo_one["Back Camera"]),'Screen Size':(tocomparetwo_one["Screen Size"])}
        compare_two_two = {'Performance':(tocomparetwo_two["Performance"])/10000,'Battery Capacity':(tocomparetwo_two["Battery Capacity"])/100,'Front Camera':(tocomparetwo_two["Front Camera"]),'Back Camera':(tocomparetwo_two["Back Camera"]),'Screen Size':(tocomparetwo_two["Screen Size"])}
        data_2 = pd.DataFrame([compare_two_one,compare_two_two])

        cols_for_radar = tocomparetwo_one[col]
        print(tabulate(dispdata, headers='keys', tablefmt='fancy_grid'))
        
        #Find the values and angles for plotting the graph
        Attributes =list(data_2)
        AttNo = len(Attributes)
        values = data_2.iloc[0].tolist()
        values += values [:1]
         
        values2 = data_2.iloc[1].tolist()
        values2 += values2 [:1]
        angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles += angles [:1]
        angles2 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles2 += angles2 [:1]
        #plotting the graph with the given values
        ax = plt.subplot(111, polar=True)
        plt.xticks(angles[:-1],Attributes)
        ax.plot(angles,values)
        ax.fill(angles, values, 'teal', alpha=0.1)
        ax.plot(angles2,values2)
        ax.fill(angles2, values2, 'red', alpha=0.1)
        #Rather than use a title, individual text points are added
        plt.figtext(0.2,0.9,' ',color="red")
        plt.figtext(0.2,0.85,"Vs")
        plt.figtext(0.2,0.8,' ',color="teal")
        plt.show()
        


    
    elif(ask=="three"):
        user_phone_three_one=int(input("Enter the Sno of the Phone u want to compare : "))
        user_phone_three_two=int(input("Enter the Sno of the Phone u want to compare : "))
        user_phone_three_three=int(input("Enter the Sno of the Phone u want to compare : "))
        
        col =["Performance","Battery Capacity","Front Camera","Back Camera","Screen Size"]        
        tocomparethree_one=(compare_df.loc[(compare_df["Sno"] == user_phone_three_one)])
        tocomparethree_two=(compare_df.loc[(compare_df["Sno"] == user_phone_three_two)])
        tocomparethree_three=(compare_df.loc[(compare_df["Sno"] == user_phone_three_three)])
        dispdata = pd.concat([tocomparethree_one, tocomparethree_two, tocomparethree_three], ignore_index=True)
        dispdata = pd.concat([dispdata, tocomparethree_three], ignore_index=True)

        
        compare_three_one = {'Performance':(tocomparethree_one["Performance"])/10000,'Battery Capacity':(tocomparethree_one["Battery Capacity"])/100,'Front Camera':(tocomparethree_one["Front Camera"]),'Back Camera':(tocomparethree_one["Back Camera"]),'Screen Size':(tocomparethree_one["Screen Size"])}
        compare_three_two = {'Performance':(tocomparethree_two["Performance"])/10000,'Battery Capacity':(tocomparethree_two["Battery Capacity"])/100,'Front Camera':(tocomparethree_two["Front Camera"]),'Back Camera':(tocomparethree_two["Back Camera"]),'Screen Size':(tocomparethree_two["Screen Size"])}
        compare_three_three = {'Performance':(tocomparethree_three["Performance"])/10000,'Battery Capacity':(tocomparethree_three["Battery Capacity"])/100,'Front Camera':(tocomparethree_three["Front Camera"]),'Back Camera':(tocomparethree_three["Back Camera"]),'Screen Size':(tocomparethree_three["Screen Size"])}
        data_3 = pd.DataFrame([compare_three_one,compare_three_two,compare_three_three])
        

        cols_for_radar = tocomparethree_one[col]
        print(tabulate(dispdata, headers='keys', tablefmt='fancy_grid'))

        #Find the values and angles for plotting the graph
        Attributes =list(data_3)
        AttNo = len(Attributes)
        values = data_3.iloc[0].tolist()
        values += values [:1]

        values2 = data_3.iloc[1].tolist()
        values2 += values2 [:1]
        angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles += angles [:1]
        angles2 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles2 += angles2 [:1]
        values3 = data_3.iloc[2].tolist()
        values3 += values3 [:1]
        angles3 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles3 += angles [:1]
        #plotting the graph with the given values
        
        ax = plt.subplot(111, polar=True)
        plt.xticks(angles[:-1],Attributes)
        ax.plot(angles,values)
        ax.fill(angles, values, 'teal', alpha=0.1)
        ax.plot(angles2,values2)
        ax.fill(angles2, values2, 'red', alpha=0.1)
        ax.plot(angles3,values3)
        ax.fill(angles3, values3, 'green', alpha=0.1)
        #Rather than use a title, individual text points are added
        plt.figtext(0.2,0.9,' ',color="red")
        plt.figtext(0.2,0.85,"Vs")
        plt.figtext(0.2,0.8,' ',color="teal")
        plt.show()

        
        
    elif(ask=="four"):
        user_phone_four_one=int(input("Enter the Sno of the Phone u want to compare : "))
        user_phone_four_two=int(input("Enter the Sno of the Phone u want to compare : "))
        user_phone_four_three=int(input("Enter the Sno of the Phone u want to compare : "))
        user_phone_four_four=int(input("Enter the Sno of the Phone u want to compare : "))
        
        col =["Performance","Battery Capacity","Front Camera","Back Camera","Screen Size"]        
        tocomparefour_one=(compare_df.loc[(compare_df["Sno"] == user_phone_four_one)])
        tocomparefour_two=(compare_df.loc[(compare_df["Sno"] == user_phone_four_two)])
        tocomparefour_three=(compare_df.loc[(compare_df["Sno"] == user_phone_four_three)])
        tocomparefour_four=(compare_df.loc[(compare_df["Sno"] == user_phone_four_four)])
        dispdata = pd.concat([tocomparefour_one, tocomparefour_two, tocomparefour_three, tocomparefour_four], ignore_index=True)

        
        compare_four_one = {'Performance':(tocomparefour_one["Performance"])/10000,'Battery Capacity':(tocomparefour_one["Battery Capacity"])/100,'Front Camera':(tocomparefour_one["Front Camera"]),'Back Camera':(tocomparefour_one["Back Camera"]),'Screen Size':(tocomparefour_one["Screen Size"])}
        compare_four_two = {'Performance':(tocomparefour_two["Performance"])/10000,'Battery Capacity':(tocomparefour_two["Battery Capacity"])/100,'Front Camera':(tocomparefour_two["Front Camera"]),'Back Camera':(tocomparefour_two["Back Camera"]),'Screen Size':(tocomparefour_two["Screen Size"])}
        compare_four_three = {'Performance':(tocomparefour_three["Performance"])/10000,'Battery Capacity':(tocomparefour_three["Battery Capacity"])/100,'Front Camera':(tocomparefour_three["Front Camera"]),'Back Camera':(tocomparefour_three["Back Camera"]),'Screen Size':(tocomparefour_three["Screen Size"])}
        compare_four_four = {'Performance':(tocomparefour_four["Performance"])/10000,'Battery Capacity':(tocomparefour_four["Battery Capacity"])/100,'Front Camera':(tocomparefour_four["Front Camera"]),'Back Camera':(tocomparefour_four["Back Camera"]),'Screen Size':(tocomparefour_four["Screen Size"])}

        data_4 = pd.DataFrame([compare_four_one,compare_four_two,compare_four_three,compare_four_four])
        

        cols_for_radar = tocomparefour_one[col]
        print(tabulate(dispdata, headers='keys', tablefmt='fancy_grid'))

        #Find the values and angles for plotting the graph
        Attributes =list(data_4)
        AttNo = len(Attributes)
        values = data_4.iloc[0].tolist()
        values += values [:1]
        values2 = data_4.iloc[1].tolist()
        values2 += values2 [:1]
        angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles += angles [:1]
        angles2 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles2 += angles2 [:1]
        values3 = data_4.iloc[2].tolist()
        values3 += values3 [:1]
        angles3 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles3 += angles [:1]
        values4 = data_4.iloc[3].tolist()
        values4 += values4 [:1]
        angles4 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles4 += angles [:1]
        #plotting the graph with the given values
        
        ax = plt.subplot(111, polar=True)
        plt.xticks(angles[:-1],Attributes)
        ax.plot(angles,values)
        ax.fill(angles, values, 'teal', alpha=0.1)
        ax.plot(angles2,values2)
        ax.fill(angles2, values2, 'red', alpha=0.1)
        ax.plot(angles3,values3)
        ax.fill(angles3, values3, 'green', alpha=0.1)
        ax.plot(angles4,values4)
        ax.fill(angles4, values4, 'blue', alpha=0.1)
        #Rather than use a title, individual text points are added
        plt.figtext(0.2,0.9,' ',color="red")
        plt.figtext(0.2,0.85,"Vs")
        plt.figtext(0.2,0.9,' ',color="teal")
        plt.show()

        
    elif(ask=="five"):
        user_phone_five_one=int(input("Enter the Sno of the Phone u want to compare : "))
        user_phone_five_two=int(input("Enter the Sno of the Phone u want to compare : "))
        user_phone_five_three=int(input("Enter the Sno of the Phone u want to compare : "))
        user_phone_five_four=int(input("Enter the Sno of the Phone u want to compare : "))
        user_phone_five_five=int(input("Enter the Sno of the Phone u want to compare : "))
        col =["Performance","Battery Capacity","Front Camera","Back Camera","Screen Size"]        
        tocomparefive_one=(compare_df.loc[(compare_df["Sno"] == user_phone_five_one)])
        tocomparefive_two=(compare_df.loc[(compare_df["Sno"] == user_phone_five_two)])
        tocomparefive_three=(compare_df.loc[(compare_df["Sno"] == user_phone_five_three)])
        tocomparefive_four=(compare_df.loc[(compare_df["Sno"] == user_phone_five_four)])
        tocomparefive_five=(compare_df.loc[(compare_df["Sno"] == user_phone_five_five)])
        dispdata = pd.concat([tocomparefive_one, tocomparefive_two, tocomparefive_three, tocomparefive_four, tocomparefive_five], ignore_index=True)

        compare_five_one = {'Performance':(tocomparefive_one["Performance"])/10000,'Battery Capacity':(tocomparefive_one["Battery Capacity"])/100,'Front Camera':(tocomparefive_one["Front Camera"]),'Back Camera':(tocomparefive_one["Back Camera"]),'Screen Size':(tocomparefive_one["Screen Size"])}
        compare_five_two = {'Performance':(tocomparefive_two["Performance"])/10000,'Battery Capacity':(tocomparefive_two["Battery Capacity"])/100,'Front Camera':(tocomparefive_two["Front Camera"]),'Back Camera':(tocomparefive_two["Back Camera"]),'Screen Size':(tocomparefive_two["Screen Size"])}
        compare_five_three = {'Performance':(tocomparefive_three["Performance"])/10000,'Battery Capacity':(tocomparefive_three["Battery Capacity"])/100,'Front Camera':(tocomparefive_three["Front Camera"]),'Back Camera':(tocomparefive_three["Back Camera"]),'Screen Size':(tocomparefive_three["Screen Size"])}
        compare_five_four = {'Performance':(tocomparefive_four["Performance"])/10000,'Battery Capacity':(tocomparefive_four["Battery Capacity"])/100,'Front Camera':(tocomparefive_four["Front Camera"]),'Back Camera':(tocomparefive_four["Back Camera"]),'Screen Size':(tocomparefive_four["Screen Size"])}
        compare_five_five = {'Performance':(tocomparefive_five["Performance"])/10000,'Battery Capacity':(tocomparefive_five["Battery Capacity"])/100,'Front Camera':(tocomparefive_five["Front Camera"]),'Back Camera':(tocomparefive_five["Back Camera"]),'Screen Size':(tocomparefive_five["Screen Size"])}
        data_5 = pd.DataFrame([compare_five_one,compare_five_two,compare_five_three,compare_five_four,compare_five_five])
        

        cols_for_radar = tocomparefive_one[col]
        print(tabulate(dispdata, headers='keys', tablefmt='fancy_grid'))


        #Find the values and angles for plotting the graph
        Attributes =list(data_5)
        AttNo = len(Attributes)
        values = data_5.iloc[0].tolist()
        values += values [:1]
        values2 = data_5.iloc[1].tolist()
        values2 += values2 [:1]
        angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles += angles [:1]
        angles2 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles2 += angles2 [:1]
        values3 = data_5.iloc[2].tolist()
        values3 += values3 [:1]
        angles3 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles3 += angles [:1]
        values4 = data_5.iloc[3].tolist()
        values4 += values4 [:1]
        angles4 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles4 += angles [:1]
        values5 = data_5.iloc[4].tolist()
        values5 += values4 [:1]
        angles5 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
        angles5 += angles [:1]
        #plotting the graph with the given values
        
        ax = plt.subplot(111, polar=True)
        plt.xticks(angles[:-1],Attributes)
        ax.plot(angles,values)
        ax.fill(angles, values, 'teal', alpha=0.1)
        ax.plot(angles2,values2)
        ax.fill(angles2, values2, 'red', alpha=0.1)
        ax.plot(angles3,values3)
        ax.fill(angles3, values3, 'green', alpha=0.1)
        ax.plot(angles4,values4)
        ax.fill(angles4, values4, 'blue', alpha=0.1)
        ax.plot(angles5,values5)
        ax.fill(angles5, values5, 'yellow', alpha=0.1)
        #Rather than use a title, individual text points are added
        plt.figtext(0.2,0.9,' ',color="red")
        plt.figtext(0.2,0.85,"Vs")
        plt.figtext(0.2,0.9,' ',color="teal")
        plt.show()



#to get the input from user        
ch=0
while ch!=4:
    ch= int(input('To filter the phones by antutu score press 1\nTo filter the phones by Battery Capacity press 2 \nTo filter phones by company press 3\nTo compare phones press 4 \nEnter the number : '))
# to call the function filterbyantutuscore() if the user wants to compare phones by antutu score
    if ch==1:
        filterbyantutuscore()
# to call the function filterbyBattery() if the user wants to compare phones by battery capacity
    elif ch==2:
        filterbyBattery()
# to call the function companywise() if the user wants to see the best phone in each company
    elif ch==3:
        companywise()
# to call the function comparephones() if the user wants to compare phones individually
    elif ch==4:
        comparephones()

        

    
        


