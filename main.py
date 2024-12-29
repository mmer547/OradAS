import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import os
import subprocess as sp
import json
import shutil

from install_tab import *

def dirdialog_clicked(IDirEntry):
    
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    IDirEntry.delete(0, "end")
    IDirEntry.insert(tk.END, iDirPath)
    return


def filedialog_clicked(IFileEntry):
    iFile = os.path.abspath(os.path.dirname(IFileEntry.get()))
    iFilePath = filedialog.askopenfilename(initialdir = iFile)
    IFileEntry.delete(0, "end")
    IFileEntry.insert(tk.END, iFilePath)
    return


def run_vscode(vscode_path, input_tab_workdir_entry, input_tab_load_sample_var):
    if input_tab_load_sample_var.get() == True:
        sample_path = os.path.join(os.path.dirname(__file__),"sample","impact_0000.rad")
        shutil.copy2(sample_path, input_tab_workdir_entry.get())
        sample_path = os.path.join(os.path.dirname(__file__),"sample","impact_0001.rad")
        shutil.copy2(sample_path, input_tab_workdir_entry.get())
        sample_path = os.path.join(os.path.dirname(__file__),"sample","impact_mesh.rad")
        shutil.copy2(sample_path, input_tab_workdir_entry.get())
    print(vscode_path + " " + input_tab_workdir_entry.get())
    sp.call(vscode_path + " " + input_tab_workdir_entry.get())
    return


def run_calc(IDirEntry1, file0000Path, file0001Path, parallel_nums,
             calc_tab_precision_value, calc_tab_stack_size):
    run_folder_path = os.path.dirname(file0000Path.get(),)

    with open(os.path.join(run_folder_path, "run.bat"), "w") as f:
        f.write("cd /d {0}\n".format(run_folder_path))
        f.write("set OPENRADIOSS_PATH=" + IDirEntry1.get() + "\n")
        f.write("set RAD_CFG_PATH=%OPENRADIOSS_PATH%\hm_cfg_files" + "\n")
        f.write("set RAD_H3D_PATH=%OPENRADIOSS_PATH%\extlib\h3d\lib\win64" + "\n")
        f.write("set KMP_STACKSIZE=" + calc_tab_stack_size.get() + "\n")
        f.write("set PATH=%OPENRADIOSS_PATH%\extlib\hm_reader\win64;%PATH%" + "\n")
        f.write("set PATH=%OPENRADIOSS_PATH%\extlib\intelOneAPI_runtime\win64;%PATH%" + "\n")
        if calc_tab_precision_value.get() == "単精度":
            precision_flag = "_sp"
        else:
            precision_flag = ""
        if int(parallel_nums.get())<=1:
                f.write("call {0} -i {1}\n".format(os.path.join(IDirEntry1.get(), "exec", "starter_win64"+precision_flag+".exe"), os.path.basename(file0000Path.get())))
                f.write("call {0} -i {1}\n".format(os.path.join(IDirEntry1.get(), "exec", "engine_win64"+precision_flag+".exe"), os.path.basename(file0001Path.get())))
        else:
            f.write("call {0}\n".format('"C:\Program Files (x86)\Intel\oneAPI\setvars.bat"'))
            f.write("call {0} -i {1} -np {2}\n".format(os.path.join(IDirEntry1.get(), "exec", "starter_win64"+precision_flag+".exe"), os.path.basename(file0000Path.get()),parallel_nums.get()))
            f.write("call mpiexec -delegate -n {2} {0} -i {1}\n".format(os.path.join(IDirEntry1.get(), "exec", "engine_win64_impi"+precision_flag+".exe"), os.path.basename(file0001Path.get()),parallel_nums.get()))
        f.write("call convert.bat")

    file_name = os.path.splitext(os.path.basename(file0000Path.get()))[0]
    print(file_name)
    with open(os.path.join(run_folder_path, "convert.bat"), "w") as f:
        f.write("cd {0}\n".format(run_folder_path))
        f.write("@setlocal enabledelayedexpansion\n")
        f.write("set num=1\n")
        f.write("set chk={0}A\n".format(file_name[0:file_name.rfind("_0000")]))
        f.write("for %%i in (*) do (\n")
        f.write('    echo %%i | find "%chk%" >NUL\n')
        f.write("    if not ERRORLEVEL 1 (\n")
        f.write('        echo %%i | find ".vtk" >NUL\n')
        f.write("        if ERRORLEVEL 1 (\n")
        f.write("            call\n")
        f.write("{0} %%i > %%i.vtk 2>&1\n".format(os.path.join(IDirEntry1.get(), "exec", "anim_to_vtk_win64.exe")))
        f.write("        )\n")
        f.write("    )\n")
        f.write(")\n")
        f.write("set chk={0}T\n".format(file_name[0:file_name.rfind("_0000")]))
        f.write("for %%i in (*) do (\n")
        f.write('    echo %%i | find "%chk%" >NUL\n')
        f.write("    if not ERRORLEVEL 1 (\n")
        f.write('        echo %%i | find ".vtk" >NUL\n')
        f.write("        if ERRORLEVEL 1 (\n")
        f.write("            call\n")
        f.write("{0} %%i\n".format(os.path.join(IDirEntry1.get(), "exec", "th_to_csv_win64.exe")))
        f.write("        )\n")
        f.write("    )\n")
        f.write(")\n")

    sp.call(["start", os.path.join(run_folder_path,"run.bat")], shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    return


def dump_settings(settings, key, value):
    settings[key] = value
    with open('settings.json', 'w') as f:
        json.dump(settings, f)


def main():
    ## 全体の構成
    root = tk.Tk()
    root.title("OradAS")
    # root.geometry("300x100")

    nb = ttk.Notebook(root)

    ##jsonファイルからの設定の読み込み
    with open('settings.json', 'r') as f:
        settings = json.load(f)

    ##タブの作成
    install_tab = tk.Frame(nb, bg='white')
    pass_tab = tk.Frame(nb, bg='white')
    mesh_tab = tk.Frame(nb, bg='white')
    input_tab = tk.Frame(nb, bg='white')
    calc_tab = tk.Frame(nb, bg='white')
    post_tab = tk.Frame(nb, bg='white')

    nb.add(install_tab, text="インストール", underline=0)
    nb.add(pass_tab, text="パス入力")
    nb.add(mesh_tab, text="メッシュ作成")
    nb.add(input_tab, text="インプット作成")
    nb.add(calc_tab, text="計算実行")
    nb.add(post_tab, text="結果処理")

    # パック
    nb.pack(expand=True, fill='both', padx=10, pady=10)

    # 部品の配置
    ## installタブ
    install_tab_link1 = tk.Label(install_tab,text="OpenRadiossのインストール",
                               fg="blue",cursor="hand1")
    install_tab_link2 = tk.Label(install_tab,text="Gmshのインストール",
                               fg="blue",cursor="hand1")
    install_tab_link3 = tk.Label(install_tab,text="VSCodeのインストール",
                               fg="blue",cursor="hand1")
    install_tab_link4 = tk.Label(install_tab,text="ParaViewのインストール",
                               fg="blue",cursor="hand1")

    ## インストールタブ
    install_tab_link1.pack(pady=10)
    install_tab_link1.bind("<Button-1>",lambda e:link_click(os.path.join(os.path.dirname(__file__),"doc", "openradioss_install_win.html")))
    install_tab_link2.pack(pady=10)
    install_tab_link2.bind("<Button-1>",lambda e:link_click(os.path.join(os.path.dirname(__file__),"doc", "gmsh_install_win.html")))
    install_tab_link3.pack(pady=10)
    install_tab_link3.bind("<Button-1>",lambda e:link_click(os.path.join(os.path.dirname(__file__),"doc", "vscode_install_win.html")))
    install_tab_link4.pack(pady=10)
    install_tab_link4.bind("<Button-1>",lambda e:link_click(os.path.join(os.path.dirname(__file__),"doc", "paraview_install_win.html")))

    ## パスタブ
    passDocLabel1 = tk.Label(pass_tab,text="パスタブの設定について",
                               fg="blue",cursor="hand1")
    passDocLabel1.bind("<Button-1>",lambda e:link_click(os.path.join(os.path.dirname(__file__),"doc", "path_setting_win.html")))
    
    IDirLabel1 = ttk.Label(pass_tab, text="OpenRadiossのフォルダパス")
    entry1 = tk.StringVar()
    IDirEntry1 = ttk.Entry(pass_tab, textvariable=entry1, width=60)
    IDirButton1 = ttk.Button(pass_tab, text="参照", command=lambda:dirdialog_clicked(IDirEntry1))
    IDirEntry1.insert(0, settings["default_path_openradioss"])

    IDirLabel2 = ttk.Label(pass_tab, text="Gmshのフォルダパス")
    entry2 = tk.StringVar()
    IDirEntry2 = ttk.Entry(pass_tab, textvariable=entry2, width=60)
    IDirButton2 = ttk.Button(pass_tab, text="参照", command=lambda:dirdialog_clicked(IDirEntry2))
    IDirEntry2.insert(0, settings["default_path_gmsh"])
    
    IDirLabel3 = ttk.Label(pass_tab, text="VScodeのフォルダパス")
    entry3 = tk.StringVar()
    IDirEntry3 = ttk.Entry(pass_tab, textvariable=entry3, width=60)
    IDirButton3 = ttk.Button(pass_tab, text="参照", command=lambda:dirdialog_clicked(IDirEntry3))
    IDirEntry3.insert(0, settings["default_path_vscode"])

    IDirLabel4 = ttk.Label(pass_tab, text="ParaViewのフォルダパス")
    entry4 = tk.StringVar()
    IDirEntry4 = ttk.Entry(pass_tab, textvariable=entry4, width=60)
    IDirButton4 = ttk.Button(pass_tab, text="参照", command=lambda:dirdialog_clicked(IDirEntry4))
    IDirEntry4.insert(0, settings["default_path_paraview"])

    ### パスタブ
    passDocLabel1.grid(row=0,column=0,padx=10,pady=10)

    IDirLabel1.grid(row=1,column=0,padx=10)
    IDirEntry1.grid(row=1,column=1,padx=10)
    IDirEntry1.bind("<Enter>",lambda event: dump_settings(settings, "default_path_openradioss", IDirEntry1.get()))
    IDirButton1.grid(row=1,column=2,padx=10)

    IDirLabel2.grid(row=2,column=0,padx=10)
    IDirEntry2.grid(row=2,column=1,padx=10)
    IDirEntry2.bind("<Enter>",lambda event: dump_settings(settings, "default_path_gmsh", IDirEntry2.get()))
    IDirButton2.grid(row=2,column=2,padx=10)

    IDirLabel3.grid(row=3,column=0,padx=10)
    IDirEntry3.grid(row=3,column=1,padx=10)
    IDirEntry3.bind("<Enter>",lambda event: dump_settings(settings, "default_path_vscode", IDirEntry3.get()))
    IDirButton3.grid(row=3,column=2,padx=10)

    IDirLabel4.grid(row=4,column=0,padx=10)
    IDirEntry4.grid(row=4,column=1,padx=10)
    IDirEntry4.bind("<Enter>",lambda event: dump_settings(settings, "default_path_paraview", IDirEntry4.get()))
    IDirButton4.grid(row=4,column=2,padx=10)

    ## メッシュタブ
    meshDocLabel1 = tk.Label(mesh_tab,text="メッシュタブの操作について",
                               fg="blue",cursor="hand1")
    meshDocLabel1.bind("<Button-1>",lambda e:link_click(os.path.join(os.path.dirname(__file__),"doc", "mesh_tab_win.html")))
    mesh_tab_IDirLabel1 = ttk.Label(mesh_tab, text="Gmshの起動")
    gmsh_path = os.path.join(IDirEntry2.get(),"gmsh.exe")
    mesh_tab_IDirButton3 = ttk.Button(mesh_tab, text="Gmsh起動", command=lambda:sp.call(gmsh_path))
    
    ### パック 
    meshDocLabel1.grid(row=0,column=0,padx=10,pady=10)
    mesh_tab_IDirLabel1.grid(row=1,column=0,padx=10)
    mesh_tab_IDirButton3.grid(row=1,column=1,padx=10)

    ### インプット作成タブ部品
    input_tab_workdir_label = ttk.Label(input_tab, text="作業フォルダのパス")
    input_tab_workdir_entry_var = tk.StringVar()
    input_tab_workdir_entry = ttk.Entry(input_tab, textvariable=input_tab_workdir_entry_var, width=60)
    input_tab_workdir_button = ttk.Button(input_tab, text="参照", command=lambda:dirdialog_clicked(input_tab_workdir_entry))
    input_tab_workdir_entry.insert(0, settings["current_workdir"])

    input_tab_load_sample_label = ttk.Label(input_tab, text="サンプルファイルのロード")
    input_tab_load_sample_var = tk.BooleanVar()
    input_tab_load_sample_chk = ttk.Checkbutton(input_tab, variable=input_tab_load_sample_var)

    input_tab_Label1 = tk.Label(input_tab,text="インプット入力タブの操作について",
                               fg="blue",cursor="hand1")
    input_tab_Label1.bind("<Button-1>",lambda e:link_click(os.path.join(os.path.dirname(__file__),"doc", "input_tab_win.html")))
    input_tab_IDirLabel1 = ttk.Label(input_tab, text="VSCodeの起動")
    vscode_path = os.path.join(IDirEntry3.get(),"Code.exe --new-window")
    # input_tab_IDirButton1 = ttk.Button(input_tab, text="VSCode起動", command=lambda:sp.call(vscode_path))
    input_tab_IDirButton1 = ttk.Button(input_tab, text="VSCode起動", command=lambda:run_vscode(vscode_path, input_tab_workdir_entry, input_tab_load_sample_var))

    ### インプット作成タブパック
    input_tab_Label1.grid(row=0,column=0,padx=10,pady=10)

    input_tab_workdir_label.grid(row=1,column=0,padx=10)
    input_tab_workdir_entry.grid(row=1,column=1,padx=10)
    input_tab_workdir_entry.bind("<Enter>",lambda event: dump_settings(settings, "current_workdir", input_tab_workdir_entry.get()))
    input_tab_workdir_button.grid(row=1,column=2,padx=10)

    input_tab_load_sample_label.grid(row=2,column=0,padx=10)
    input_tab_load_sample_chk.grid(row=2,column=2,padx=10)

    input_tab_IDirLabel1.grid(row=3,column=0,padx=10)
    input_tab_IDirButton1.grid(row=3,column=2,padx=10)

    ## カルクタブ
    calcDocLabel1 = tk.Label(calc_tab,text="計算実行タブの操作について",
                               fg="blue",cursor="hand1")
    calcDocLabel1.bind("<Button-1>",lambda e:link_click(os.path.join(os.path.dirname(__file__),"doc", "calc_tab_win.html")))
    calc_tab_IFileLabel1 = ttk.Label(calc_tab, text="0000ファイルの指定")
    calc_tab_entry1 = tk.StringVar()
    calc_tab_IFileEntry1 = ttk.Entry(calc_tab, textvariable=calc_tab_entry1, width=60)
    calc_tab_IFileEntry1.insert(0, settings["before_input_0000file"])
    calc_tab_IFileButton1 = ttk.Button(calc_tab, text="参照", command=lambda:filedialog_clicked(calc_tab_IFileEntry1))

    calc_tab_IFileLabel2 = ttk.Label(calc_tab, text="0001ファイルの指定")
    calc_tab_entry2 = tk.StringVar()
    calc_tab_IFileEntry2 = ttk.Entry(calc_tab, textvariable=calc_tab_entry2, width=60)
    calc_tab_IFileEntry2.insert(0, settings["before_input_0001file"])
    calc_tab_IFileButton2 = ttk.Button(calc_tab, text="参照", command=lambda:filedialog_clicked(calc_tab_IFileEntry2))
    
    calc_tab_parallel_cpus_label = ttk.Label(calc_tab, text="並列CPU数")
    parallel_nums = [i + 1 for i in range(os.cpu_count())]
    calc_tab_parallel_cpus_value = ttk.Combobox(calc_tab, value=parallel_nums, width=5)    
    calc_tab_parallel_cpus_value.set(1)

    calc_tab_precision_label = ttk.Label(calc_tab, text="精度選択")
    precision_values = ["倍精度","単精度"]
    calc_tab_precision_value = ttk.Combobox(calc_tab, value=precision_values, width=10)
    calc_tab_precision_value.set("倍精度")

    calc_tab_stack_size_label = ttk.Label(calc_tab, text="スタックサイズ")
    calc_tab_stack_size = tk.StringVar()
    calc_tab_stack_size = ttk.Entry(calc_tab, textvariable=calc_tab_stack_size, width=10)
    calc_tab_stack_size.insert(0, "400m")

    calc_tab_IFileLabel3 = ttk.Label(calc_tab, text="OpenRadiossの実行")
    calc_tab_IFileButton3 = ttk.Button(calc_tab, text="計算実行", command=lambda:run_calc(IDirEntry1, calc_tab_IFileEntry1, calc_tab_IFileEntry2,calc_tab_parallel_cpus_value,
                                                                                         calc_tab_precision_value, calc_tab_stack_size))

    ### パック
    #### ドキュメントのリンク
    calcDocLabel1.grid(row=0,column=0,padx=10,pady=10)
    #### 0000ファイルの指定
    calc_tab_IFileLabel1.grid(row=1,column=0,padx=10)
    calc_tab_IFileEntry1.grid(row=1,column=1,padx=10)
    calc_tab_IFileEntry1.bind("<Enter>",lambda event: dump_settings(settings, "before_input_0000file", calc_tab_IFileEntry1.get()))
    calc_tab_IFileButton1.grid(row=1,column=2,padx=10)
    #### 0001ファイルの指定
    calc_tab_IFileLabel2.grid(row=3,column=0,padx=10)
    calc_tab_IFileEntry2.grid(row=3,column=1,padx=10)
    calc_tab_IFileEntry2.bind("<Enter>",lambda event: dump_settings(settings, "before_input_0001file", calc_tab_IFileEntry2.get()))
    calc_tab_IFileButton2.grid(row=3,column=2,padx=10)
    #### 並列計算
    calc_tab_parallel_cpus_label.grid(row=5,column=0,padx=10)
    calc_tab_parallel_cpus_value.grid(row=5,column=2,padx=10)
    #### 計算精度
    calc_tab_precision_label.grid(row=6,column=0,padx=10)
    calc_tab_precision_value.grid(row=6,column=2,padx=10)
    #### スタックサイズ
    calc_tab_stack_size_label.grid(row=7,column=0,padx=10)
    calc_tab_stack_size.grid(row=7,column=2,padx=10)
    #### 計算実行ボタン
    calc_tab_IFileLabel3.grid(row=8,column=0,padx=10)
    calc_tab_IFileButton3.grid(row=8,column=2,padx=10)

    ## ポストタブの部品
    postDocLabel1 = tk.Label(post_tab,text="結果処理タブの操作について",
                               fg="blue",cursor="hand1")
    postDocLabel1.bind("<Button-1>",lambda e:link_click(os.path.join(os.path.dirname(__file__),"doc", "post_tab_win.html")))
    post_tab_IDirLabel2 = ttk.Label(post_tab, text="ParaViewの起動")
    paraview_path = os.path.join(IDirEntry4.get(),"bin","paraview.exe")
    post_tab_IDirButton2 = ttk.Button(post_tab, text="ParaView起動", command=lambda:sp.call(paraview_path))
    ### ポストタブの配置
    postDocLabel1.grid(row=0,column=0,padx=10,pady=10)
    post_tab_IDirLabel2.grid(row=1,column=0,padx=10)
    post_tab_IDirButton2.grid(row=1,column=1,padx=10)

    root.mainloop()

if __name__=="__main__":
    main()