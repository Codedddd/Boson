import os
import pystyle
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class createCLIMenu:

    global create_MPL_graph

    def create_MPL_graph(x_axis_points , y_axis_points , x_minimum , x_maximum , y_maximum , x_axis_title , y_axis_title , graph_title):
        dataFrame = pd.DataFrame({"x" : x_axis_points,
                                  "y" : y_axis_points})
        
        plt.scatter(dataFrame.x , dataFrame.y)
        model = np.poly1d(np.polyfit(dataFrame.x , dataFrame.y , 5))
        polyline = np.linspace(x_minimum , x_maximum , y_maximum)
        plt.plot(polyline , model(polyline) , color = "purple")
        plt.xlabel(x_axis_title)
        plt.ylabel(y_axis_title)
        plt.title(graph_title)
        plt.gcf().canvas.manager.set_window_title(graph_title)
        plt.grid(True)
        plt.show()

    def __init__(self):

        def help():
            command_list = ["help" , "graph", "dictionary", "constants"]
            command_list_descriptions = ["This command" , "Create a graph with a set of data" , "A dictionary of equations" , "Constants in both Maths and Physics"]
            for index , command in enumerate(command_list):
                max_length = 54
                #pystyle.Write.Print(pystyle.Center.XCenter(f"\n[ {index + 1} ] {command} : {command_list_deccriptions[index]}") , color = pystyle.Colors.purple , interval = 0)
                line = f"\n[ {index + 1} ] {command} : {command_list_descriptions[index]}"
                extra_chars = max_length - len(line)
                fill = '‎' * extra_chars if extra_chars > 0 else ''
                formatted_line = f"{line}{fill}"
                pystyle.Write.Print(pystyle.Center.XCenter(formatted_line) , color = pystyle.Colors.purple , interval = 0)

        ## Variables for the console will be defined here. Why? Why the fuck not lol.

        BANNER = """‎____\n| __ )  ___  ___  ___  _ __\n|  _ \ / _ \/ __|/ _ \| '_ \ \n| |_) | (_) \__ \ (_) | | | |\n|____/ \___/|___/\___/|_| |_|\n"""
        BOX_ART = """\n┌────────────────────────────────────────────┐\n│                                            │\n│   Github  : https://github.com/codedddd    │\n│   Website : https://ariez.xyz              │\n│                                            │\n└────────────────────────────────────────────┘\n"""
        
        os.system("cls")
        os.system("title Boson │ Select a command")
        pystyle.Write.Print(pystyle.Center.XCenter(f"{BANNER}\n\n") , color = pystyle.Colors.cyan , interval = 0)
        pystyle.Write.Print(pystyle.Center.XCenter(BOX_ART) , color = pystyle.Colors.cyan , interval = 0)
        while True:
            command_chosen = pystyle.Write.Input(pystyle.Center.XCenter("\n\nPlease input a command to run\n\n> ") , color = pystyle.Colors.purple , interval = 0)
            match command_chosen:
                case "help":
                    help()
                case "graph":
                    x_axis_data_points = []
                    y_axis_data_points = []
                    x = x_axis_data_points
                    y = y_axis_data_points

                    def get_data():
                        user_cords_input = entry.get()
                        if "," in user_cords_input:
                            coordinates = user_cords_input.split(",")
                            if len(coordinates) == 2:
                                try:
                                    x , y = map(int , coordinates)
                                    label.config(text = f"Co-ordinates inputted: \"({x} , {y})\"")
                                    x_axis_data_points.append(x)
                                    y_axis_data_points.append(y)
                                except ValueError:
                                    label.config(text = f"{user_cords_input} is not a valid co-ordinate,\n please enter co-ordinates\n in the form \"x\" , \"y\" and try again!")
                            else:
                                label.config(text = f"{user_cords_input} is not a valid co-ordinate,\n please enter co-ordinates\n in the form \"x\" , \"y\" and try again!")
                        else:
                                label.config(text = f"{user_cords_input} is not a valid co-ordinate,\n please enter co-ordinates\n in the form \"x\" , \"y\" and try again!")
                    def close_window():
                        root1.destroy()
                    root1 = tk.Tk()
                    root1.iconbitmap("Python\images\demon_lord.ico")
                    root1.title("Input Co-Ordinates")
                    root1.geometry("300x175")
                    root1.resizable(False , False)
                    entry = tk.Entry(root1)
                    entry.grid(row = 0 , column = 1 , pady = 10)
                    label = tk.Label(root1 , text = "")
                    label.grid(row = 1 , column = 1)
                    tk.Button(root1 , text = "Enter" , command = get_data).grid(row = 2 , column =  1 , padx = 125 , pady = 10)
                    tk.Button(root1 , text = "Finish" , command = close_window).grid(row = 3 , column = 1)
                    root1.mainloop()

                    x_axis_title = pystyle.Write.Input(pystyle.Center.XCenter("\n\nPlease input a title for the x axis\n\n> ") , color = pystyle.Colors.purple , interval = 0)
                    y_axis_title = pystyle.Write.Input(pystyle.Center.XCenter("\n\nPlease input a title for the y axis\n\n> ") , color = pystyle.Colors.purple , interval = 0)
                    graph_title = pystyle.Write.Input(pystyle.Center.XCenter("\n\nPlease input a title graph\n\n> ") , color = pystyle.Colors.purple , interval = 0)

                    x.sort()
                    x_minimum_value = min(x)-2
                    x_maximum_value = max(x)+2
                    y_minimum_value = min(y)-2 # We don't actually use this but I'll keep it here incase of a future update lol.
                    y_maximum_value = max(y)+2

                    print(x_minimum_value , x_maximum_value)
                    print(y_minimum_value , y_maximum_value)

                    create_MPL_graph(x_axis_data_points , y_axis_data_points , x_minimum_value , x_maximum_value , y_maximum_value , x_axis_title , y_axis_title , graph_title)

if __name__ == "__main__":
    createCLIMenu()