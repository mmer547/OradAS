## 日本語 Readme

## OradASについて

OradASは"OpenRadioss Assistant System"の略語です。ORadASではOpenRadiossの利用に当たり必要となるツールのインストールから使用方法までを手助けすることを目的に作成されています。

通常、OpenRadiossはコマンドで実行しないといけないですが、ORadASのGUIでは数回のクリックだけで実行できます。

OradASはPythonの標準ライブラリだけで作成されています。サードパーティのライブラリを大量にインストールする必要はありません。

OradASは英語の苦手な人でも使えるように日本語で構成されています。英語対応は将来的な機能追加で実施します。

OradAS開発中の機能についてはissueをご覧ください。

## バージョン履歴

2024/03/30 : Version 1.0 release.基本的な機能を実装。

2024/03/30 : Version 1.1 release.結果処理タブの誤字修正。

2024/03/30 : Version 1.2 release.並列計算CPU数の指定機能追加。

2024/12/28 : Version 1.3 release.OpenRadiossインストールパスが固定になっていた問題の解消。

2024/12/28 : Version 1.4 release.Cドライブ以外で計算が実行できない問題の解消。

2024/12/28 : Version 1.5 release.倍精度、単精のソルバを変更できる機能の追加。

2024/12/28 : Version 1.6 release.Tファイルをcsvファイルに自動で変換する処理を追加。

2024/12/29 : Version 1.7 release.StackSizeを変更できる機能を追加。

## 起動要件

Python (>=3.10)

## 使用方法

次のコマンドで起動できます。

`python main.py`

使い方はGUI内にドキュメントとして埋め込んでいます。

![image-20240330143446024](./assets/image-20240330143446024.png)

![image-20240330143523924](./assets/image-20240330143523924.png)

## 初期設定

まずはインストールタブのドキュメントから各種ソフトウェア、VSCodeエクステンションのインストールをお願いします。

![2024-05-25-14-42-37](./assets/2024-05-25-14-42-37.png)

次にパス入力タブからソフトウェアのフォルダパスを設定すれば使用準備完了です。

![Alt text](./assets/image.png)

2024/6/24追記　OpenRadiossのパス設定でうまくいかない場合があるようで、その場合はドキュメントと同じパスにOpenRadiossを置いてお試しください。次バージョンで修正予定です。

## ライセンス

OradASはMIT licenseを採用しています。

# English Readme

## About OradAS

OradAS stands for "OpenRadioss Assistant System" and was created to help you install and use the tools you need to use OpenRadioss.

Normally, OpenRadioss has to be run with commands, but with the ORadAS GUI it can be done with just a few clicks.

OradAS was created using only the standard Python library. There is no need to install a lot of third-party libraries.

OradAS is written in Japanese so that even people who are not good at English can use it. English support will be added in the future.

For more information about features under development in OradAS, please see the issue.

## Version up log

2024/03/30 : Version 1.0 release. Has a basic function.

2024/03/30 : Version 1.1 release. Correction of typographical errors in the results processing tab.

2024/03/30 : Version 1.2 release. Additional functionality for specifying the number of parallel calculation CPUs.

2024/12/28 : Version 1.3 release.Fixed problem with fixed OpenRadioss installation path.

2024/12/28 : Version 1.4 release.Solves a problem where calculations cannot be executed outside the C drive.

28/12/2024 : Version 1.5 release.Added the ability to change double precision and single precision solvers.

28/12/2024 : Version 1.6 release.Added automatic conversion of T files to csv files.

29/12/2024 : Version 1.7 release.Added the ability to change the StackSize.

## requirement

Python (>=3.10)

## usage rules

It can be started with the following command

`python main.py`

The usage is embedded as documentation in the GUI.

![image-20240330143446024](./assets/image-20240330143446024.png)

![image-20240330143523924](./assets/image-20240330143523924.png)

## initialisation

First, please install the various software and add-ins from the documents in the Installation tab. 

![2024-05-25-14-42-37](./assets/2024-05-25-14-42-37.png)

Next, set the software folder path from the Path input tab and you are ready to use the software. 

![Alt text](./assets/image.png)

Added on 6/24/2024: It seems that the OpenRadioss path setting may not work, in that case, please try placing OpenRadioss in the same path as the document.This will be fixed in the next version.

## License

OradAS is MIT licensed.
