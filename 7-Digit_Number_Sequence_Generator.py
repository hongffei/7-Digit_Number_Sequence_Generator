import tkinter as tk
import tkinter.scrolledtext as tkst


# 全局变量
variable_letters_first = None
variable_letters_second = None
variable_letters_third = None

ascii1_text = None
ascii2_text = None
ascii3_text = None
decimal_Waypoint_type_text = None
Waypoint_type_text = None


def generate_sequence():
    # 获取选择的字母
    letter1 = variable_letters_first.get()
    letter2 = variable_letters_second.get()
    letter3 = variable_letters_third.get()

    # 计算每个字母的十六进制ASCII码，并转换为大写
    ascii1 = hex(ord(letter1)).upper()[2:]
    ascii2 = hex(ord(letter2)).upper()[2:]
    ascii3 = hex(ord(letter3)).upper()[2:]

    # 更新显示的ASCII码
    ascii1_text.set(ascii1)
    ascii2_text.set(ascii2)
    ascii3_text.set(ascii3)

    # 将ASCII码按照倒序排列
    ascii_list = [ascii3, ascii2, ascii1]
    # 将十六进制ASCII码转换为十进制数字序列
    decimal_sequence = int(''.join(ascii_list), 16)

    # 更新转换结果显示
    decimal_Waypoint_type_text.set(str(decimal_sequence))


def update_ascii1(*args):
    letter = variable_letters_first.get()
    ascii_value = hex(ord(letter)).upper()[2:]  # Get the correct hexadecimal ASCII representation
    ascii1_text.set(ascii_value)


def update_ascii2(*args):
    letter = variable_letters_second.get()
    ascii_value = hex(ord(letter)).upper()[2:]  # Get the correct hexadecimal ASCII representation
    ascii2_text.set(ascii_value)


def update_ascii3(*args):
    letter = variable_letters_third.get()
    ascii_value = hex(ord(letter)).upper()[2:]  # Get the correct hexadecimal ASCII representation
    ascii3_text.set(ascii_value)


def decimal_to_hexadecimal(decimal_number):
    hex_number = hex(decimal_number)
    return hex_number[2:].upper()  # 将字母变为大写


def query_sequence():
    global Waypoint_type_text  # 声明为全局变量
    decimal_sequence = entry_decimal_Waypoint_type_1.get()

    # Convert decimal sequence to integer
    decimal_number = int(decimal_sequence)

    # Convert the decimal number to hexadecimal with leading zeros
    hex_sequence = decimal_to_hexadecimal(decimal_number)

    # Split the hex_sequence into three parts
    hex_parts = [hex_sequence[i:i+2] for i in range(0, len(hex_sequence), 2)]

    # Update text variables for each part
    for i in range(3):
        hex_part_texts[i].set(hex_parts[i])

    # Update the Waypoint_type_text
    Waypoint_type_text.set(hex_sequence)


def show_info_dialog():
    # 创建弹窗
    info_window = tk.Toplevel(window)
    info_window.title("Information")

    # 设置弹窗宽度
    info_window.geometry("800x520+100+100")  # 设置宽度为 800 像素，高度为 520 像素

    # 设置文本框显示信息
    info_text = tkst.ScrolledText(info_window, width=110, height=34, wrap=tk.WORD)  # 设置文本框宽度为 110 个字符
    info_text.grid(row=0, column=0, padx=10, pady=10)
    info_content = """ENROUTE AND TERMINAL WAYPOINTS
ARC Center Fix:                                                      A(41)  NUL(20)  NUL(20)  Use: PC
Combined Named Intersection and/or named DME Fix and RNAV Waypoint:  C(43)                    Use: EA,PC
Unnamed, Charted Intersection and/or Unnamed DME Fix:                I(49)                    Use: EA,PC
Middle or Inner Marker as Waypoint:                                  M(4D)                    Use: PC
NDB or Terminal NDB Navaid as Waypoint:                              N(4E)  NUL(20)  NUL(20)  Use: EA,PC
Outer or Back Marker as Waypoint:                                    O(4F)                    Use: PC 
Named Intersection and/or Named DME Fix:                             R(52)                    Use: EA,PC
Uncharted Airway Intersection:                                       U(55)                    Use: EA 
VFR Waypoint:                                                        V(56)                    Use: EA,PC
Named RNAV Waypoint:                                                 W(57)                    Use: EA,PC                              
Final Approach Fix (FAF):                                                   A(41)             Use: EA,PC
Initial Approach Fix and Final Approach Fix（IAF & FAF）:                   B(42)             Use: EA,PC
Final Approach Course Fix（FACF）:                                          C(43)             Use: EA,PC
Intermediate Approach Fix（IF）:                                            D(44)             Use: EA,PC
Initial Approach Fix（IAF）:                                                I(49)             Use: EA,PC
Final Approach Course Fix and Initial Approach Fix（FACF & IAF）:           K(4B)             Use: EA,PC
Final Approach Course Fix and Intermediate Approach Fix（FACF & IF）:       L(4C)             Use: EA,PC
Missed Approach Fix（MAP）:                                                 M(4D)             Use: EA,PC
Initial  Approach Fix and Missed Approach Fix （IAF & MAP）:                N(4E)             Use: EA,PC
Unnamed  Step down Fix（SDF）:                                              P(50)             Use: PC
RF Leg Fix Not at Procedure Fix:                                            R(52)             Use: PC
Named Step down Fix（SDF）:                                                 S(53)             Use: PC
Oceanic Gateway Fix:                                                        O(4F)             Use: EA
Off-Route Intersection and/or Off Route DME Fix:                            F(46)             Use: EA
FIR/UIR or Controlled Airspace Intersection:                                U(55)             Use: EA
Latitude/Longitude Fix, Full Degree of Latitude:                            V(56)             Use: EA
Latitude/Longitude Fix, Half Degree of Latitude:                            W(57)             Use: EA
Published for Use in SID:                                                            D(44)    Use: EA,PC 
Published for Use in STAR:                                                           E(45)    Use: EA,PC
Published for Use in Approach Procedures:                                            F(46)    Use: EA,PC
Published for Use in Multiple Terminal Procedure Types:                              Z(5A)    Use: EA,PC
Source Provided Enroute Waypoint:                                                    G(47)               """
    info_text.insert(tk.END, info_content)
    info_text.config(state='disabled')  # 使文本框不可编辑

    # 设置关闭按钮
    close_button = tk.Button(info_window, text="Close", command=info_window.destroy)
    close_button.grid(row=1, column=0, pady=10)


# 创建GUI窗口
window = tk.Tk()
window.title("X-Plane Waypoint Type 7-Digit Number Sequence Generator V2.0")
window.geometry("580x300+900+100")

# 创建标签
label_Waypoint_type = tk.Label(window, text="Waypoint Type：")
label_Waypoint_type.grid(row=0, column=0, padx=10, pady=10)

variable_letters_first = tk.StringVar(window)
variable_letters_first.set("A")
dropdown_letters_first = tk.OptionMenu(window, variable_letters_first, "A", "C", "I", "M", "N", "O", "R", "U", "V", "W", command=update_ascii1)
dropdown_letters_first.grid(row=0, column=1, padx=5, pady=10)
ascii1_text = tk.StringVar()
label_ascii1_display = tk.Entry(window, width=5, textvariable=ascii1_text, state='readonly')
label_ascii1_display.grid(row=0, column=2, padx=5, pady=10)

variable_letters_second = tk.StringVar(window)
variable_letters_second.set("A")
dropdown_letters_second = tk.OptionMenu(window, variable_letters_second, "A", "B", "C", "D", "F", "I", "K", "L", "M", "N","O", "P", "R", "S", "U", "V", "W", " ", command=update_ascii2)
dropdown_letters_second.grid(row=0, column=3, padx=5, pady=10)
ascii2_text = tk.StringVar()
label_ascii2_display = tk.Entry(window, width=5, textvariable=ascii2_text, state='readonly')
label_ascii2_display.grid(row=0, column=4, padx=5, pady=10)

variable_letters_third = tk.StringVar(window)
variable_letters_third.set("D")
dropdown_letters_third = tk.OptionMenu(window, variable_letters_third, "D", "E", "F", "Z", "G", " ", command=update_ascii3)
dropdown_letters_third.grid(row=0, column=5, padx=5, pady=10)
ascii3_text = tk.StringVar()
label_ascii3_display = tk.Entry(window, width=5, textvariable=ascii3_text, state='readonly')
label_ascii3_display.grid(row=0, column=6, padx=5, pady=10)

# 创建标签和转换结果（输出部分）
label_decimal_Waypoint_type = tk.Label(window, text="7-Digit Number Sequence：")
label_decimal_Waypoint_type.grid(row=1, column=0, padx=10, pady=10)
decimal_Waypoint_type_text = tk.StringVar()
label_decimal_Waypoint_type_result = tk.Entry(window, width=8, textvariable=decimal_Waypoint_type_text, state='readonly')
label_decimal_Waypoint_type_result.grid(row=1, column=1, padx=10, pady=10)

# 创建按钮并绑定事件
convert_button = tk.Button(window, text="Conversion", command=generate_sequence)
convert_button.grid(row=2, column=0, columnspan=8, padx=10, pady=10)


# 创建弹窗按钮
info_button = tk.Button(window, text="Show Information", command=show_info_dialog)
info_button.grid(row=2, column=0, padx=10, pady=10)


# 创建标签、输入框（Query_waypoint_type）
label_Query_waypoint_type = tk.Label(window, text="Query waypoint type：")
label_Query_waypoint_type.grid(row=3, column=0, padx=10, pady=10)

label_decimal_Waypoint_type_1 = tk.Label(window, text="7-Digit Number Sequence：")
label_decimal_Waypoint_type_1.grid(row=4, column=0, padx=20, pady=10)
entry_decimal_Waypoint_type_1 = tk.Entry(window, width=8)
entry_decimal_Waypoint_type_1.grid(row=4, column=1, padx=10, pady=10)

# 创建标签和查询结果（输出部分）
label_Waypoint_type = tk.Label(window, text="waypoint_type：")
label_Waypoint_type.grid(row=5, column=0, padx=10, pady=10)

# Entries to display individual parts of hex sequence
hex_part_texts = [tk.StringVar() for _ in range(3)]
entry_hex_parts = []
for i in range(3):
    entry_hex_part = tk.Entry(window, width=3, textvariable=hex_part_texts[i], state='readonly')
    entry_hex_part.grid(row=5, column=4-i, padx=5, pady=5)
    entry_hex_parts.append(entry_hex_part)

# 创建按钮并绑定事件
Query_button = tk.Button(window, text="Query", command=query_sequence)  # 修改这里的命令为 query_sequence
Query_button.grid(row=5, column=1, padx=10, pady=10)

# 运行GUI窗口
window.mainloop()