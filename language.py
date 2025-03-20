def choose_lang(lang):
    if lang == 'ja':
        lang_set = {
            "w_install_tab_title" : "インストール",
            "w_pass_tab_title" : "パス入力",
            "w_mesh_tab_title" : "メッシュ作成",
            "w_input_tab_title" : "インプット作成",
            "w_calc_tab_title" : "計算実行",
            "w_post_tab_title" : "結果処理",
            'w_precision1' : '単精度',
            'w_precision2' : '倍精度',
        }
        return lang_set
    elif lang == 'en':
        lang_set = {
            "w_install_tab_title" : "install",
            "w_pass_tab_title" : "path entry",
            "w_mesh_tab_title" : "Mesh Creation",
            "w_input_tab_title" : "input creation",
            "w_calc_tab_title" : "computation run",
            "w_post_tab_title" : "result processing",
            'w_precision1' : 'single-precision',
            'w_precision2' : 'double precision',
        }
        return lang_set