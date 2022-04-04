import csv
import random
import tkinter as tk
from tkinter import filedialog

def readfile():
    file_type = [("CSVファイル", "*.csv")]
    def_dir = "C:\\Users"
    file = filedialog.askopenfilenames(filetypes = file_type, initialdir = def_dir)
    input_box.configure(state='normal')
    input_box.delete(0,tk.END)
    input_box.insert(tk.END, file)
    input_box.configure(state='readonly')

def make_block():
    member = [[]*i for i in range(20)]
    number = 0
    leageue_name = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    leagues = []

    file_type = [("CSVファイル", "*.csv")]
    def_dir = "C:\\Users"

    file = input_box.get()

    # 大学ごとに参加者をリストにしたリスト（member）
    with open(file) as f:
        rows = csv.reader(f)
        for row in rows:
            code = int(row[3])
            member[code].append(row)
            number += 1

    # リーグ数を計算
    n = 4
    quotient = number//n
    remainder = number%n
    turtle = quotient - n + 1 + remainder
    crane = n - remainder
    big_league = turtle + crane//n * (n-1)
    small_league = crane%n

    # 大学コードと参加人数の2次元配列のリスト（univ_num）
    univ_num = []
    for univ in member:
        univ_code = member.index(univ)
        univ_num.append([univ_code, len(univ)])

    # 大きいリーグの振り分け処理
    for i in range(big_league):
        check = univ_num
        name = (leageue_name.pop(0) + "リーグ")
        league = [name]
        for j in range(n):
            check = sorted(check, reverse=True, key=lambda x: x[1])
            # 人数が最大である大学コードのリスト（max_univ）
            max_univ = []
            max_value = 1
            for k in range(len(check)):
                if check[k][1] >= max_value:
                    max_value = check[k][1]
                    max_univ.append([check[k][0],k])
                else:
                    break
            choice = random.choice(max_univ)
            choice_code = choice[0]
            choice_num = choice[1]
            univ_num[choice_code][1] -= 1
            person = member[choice_code].pop(random.randint(0,len(member[choice_code])-1))
            pick = person[1]+"("+person[0]+person[2]+")"
            league.append(pick)
            del check[choice_num]
        leagues.append(league)

    # 小さいリーグの振り分け処理
    for i in range(small_league):
        check = univ_num
        name = (leageue_name.pop(0) + "リーグ")
        league = [name]
        for j in range(n-1):
            check = sorted(check, reverse=True, key=lambda x: x[1])
            # 人数が最大である大学コードのリスト（max_univ）
            max_univ = []
            max_value = 1
            for k in range(len(check)):
                if check[k][1] >= max_value:
                    max_value = check[k][1]
                    max_univ.append([check[k][0],k])
                else:
                    break
            choice = random.choice(max_univ)
            choice_code = choice[0]
            choice_num = choice[1]
            univ_num[choice_code][1] -= 1
            person = member[choice_code].pop(random.randint(0,len(member[choice_code])-1))
            pick = person[1]+"("+person[0]+person[2]+")"
            league.append(pick)
            del check[choice_num]
        league.append("")
        leagues.append(league)

    out_file = filedialog.asksaveasfilename(filetypes = file_type, initialdir = def_dir, defaultextension = "csv")

    league_num = len(leagues)
    double = league_num//2
    single = league_num%2

    with open(out_file, "w", newline="") as f:
        write = csv.writer(f)
        for i in range(double):
            write.writerow([leagues[2*i][0]," "," "," "," "," "," ",leagues[2*i+1][0]])
            write.writerow([" ",leagues[2*i][1],leagues[2*i][2],leagues[2*i][3],leagues[2*i][4]," "," "," ",leagues[2*i+1][1],leagues[2*i+1][2],leagues[2*i+1][3],leagues[2*i+1][4]])
            write.writerow([leagues[2*i][1]," "," "," "," "," "," ",leagues[2*i+1][1]])
            write.writerow([leagues[2*i][2]," "," "," "," "," "," ",leagues[2*i+1][2]])
            write.writerow([leagues[2*i][3]," "," "," "," "," "," ",leagues[2*i+1][3]])
            write.writerow([leagues[2*i][4]," "," "," "," "," "," ",leagues[2*i+1][4]])
            write.writerow([" "])

        if single == 1:
            write.writerow([leagues[-1][0]])
            write.writerow([" ",leagues[-1][1],leagues[-1][2],leagues[-1][3],leagues[-1][4]])
            write.writerow([leagues[-1][1]])
            write.writerow([leagues[-1][2]])
            write.writerow([leagues[-1][3]])
            write.writerow([leagues[-1][4]])

root = tk.Tk()
root.title("ブロック予選作成")
root.geometry("500x300+500+300")
input_box = tk.Entry(width=40, font=("MSゴシック", "18"))
input_box.configure(state='readonly')
input_box.place(x=10, y=70)
input_label = tk.Label(text="入力ファイル", font=("MSゴシック", "20"))
input_label.place(x=10, y=30)
button1 = tk.Button(text="ファイル選択", font=("MSゴシック", "15", "bold"), command=readfile)
button1.place(x=320, y=120)
button2 = tk.Button(text="ファイル出力", font=("MSゴシック", "30", "bold"), command=make_block)
button2.place(x=110, y=200)
root.mainloop()