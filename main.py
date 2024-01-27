import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import os

from install_tab import *

def dirdialog_clicked(IDirEntry):
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    IDirEntry.insert(tk.END, iDirPath)

def main():
    ## 全体の構成
    root = tk.Tk()
    root.title("OradAS")
    # root.geometry("300x100")

    nb = ttk.Notebook(root)

    ##タブの作成
    install_tab = tk.Frame(nb, bg='white')
    pass_tab = tk.Frame(nb, bg='white')
    mesh_tab = tk.Frame(nb, bg='white')
    calc_tab = tk.Frame(nb, bg='white')
    post_tab = tk.Frame(nb, bg='white')

    nb.add(install_tab, text="インストール", underline=0)
    nb.add(pass_tab, text="パス入力")
    nb.add(mesh_tab, text="メッシュ作成")
    nb.add(calc_tab, text="計算実行")
    nb.add(post_tab, text="結果処理")

    # 部品の配置
    ## installタブ
    install_tab_link1 = tk.Label(install_tab,text="OpenRadiossのインストール",
                               fg="blue",cursor="hand1")
    install_tab_link2 = tk.Label(install_tab,text="Gmshのインストール",
                               fg="blue",cursor="hand1")
    install_tab_link3 = tk.Label(install_tab,text="ParaViewのインストール",
                               fg="blue",cursor="hand1")

    ## パスタブ
    # OpenRadiossのタブ
    IDirLabel1 = ttk.Label(pass_tab, text="OpenRadiossのフォルダパス")
    entry1 = tk.StringVar()
    IDirEntry1 = ttk.Entry(pass_tab, textvariable=entry1, width=30)
    IDirButton1 = ttk.Button(pass_tab, text="参照", command=lambda:dirdialog_clicked(IDirEntry1))
    
    IDirLabel2 = ttk.Label(pass_tab, text="Gmshのフォルダパス")
    entry2 = tk.StringVar()
    IDirEntry2 = ttk.Entry(pass_tab, textvariable=entry2, width=30)
    IDirButton2 = ttk.Button(pass_tab, text="参照", command=lambda:dirdialog_clicked(IDirEntry2))
    
    IDirLabel3 = ttk.Label(pass_tab, text="ParaViewのフォルダパス")
    entry3 = tk.StringVar()
    IDirEntry3 = ttk.Entry(pass_tab, textvariable=entry3, width=30)
    IDirButton3 = ttk.Button(pass_tab, text="参照", command=lambda:dirdialog_clicked(IDirEntry3))

    ## メッシュタブ
    mesh_tab_IDirLabel1 = ttk.Label(mesh_tab, text="工事中")

    ## カルクタブ
    calc_tab_IDirLabel1 = ttk.Label(calc_tab, text="工事中")

    ## ポストタブ
    post_tab_IDirLabel1 = ttk.Label(post_tab, text="工事中")

    # パック
    nb.pack(expand=True, fill='both', padx=10, pady=10)

    ## インストールタブ
    install_tab_link1.pack()
    install_tab_link1.bind("<Button-1>",lambda e:link_click("https://github.com/OpenRadioss/OpenRadioss/releases"))
    install_tab_link2.pack()
    install_tab_link2.bind("<Button-1>",lambda e:link_click("https://gmsh.info/"))
    install_tab_link3.pack()
    install_tab_link3.bind("<Button-1>",lambda e:link_click("https://www.paraview.org/download/"))
    
    ## パスタブ
    IDirLabel1.grid(row=0,column=0)
    IDirEntry1.grid(row=0,column=1)
    IDirButton1.grid(row=0,column=2)

    IDirLabel2.grid(row=1,column=0)
    IDirEntry2.grid(row=1,column=1)
    IDirButton2.grid(row=1,column=2)

    IDirLabel3.grid(row=2,column=0)
    IDirEntry3.grid(row=2,column=1)
    IDirButton3.grid(row=2,column=2)

    ## メッシュタブ
    mesh_tab_IDirLabel1.grid(row=0,column=0)

    ## カルクタブ
    calc_tab_IDirLabel1.grid(row=0,column=0)

    ## ポストタブ
    post_tab_IDirLabel1.grid(row=0,column=0)

    ## コンバートタブ

    root.mainloop()

if __name__=="__main__":
    main()