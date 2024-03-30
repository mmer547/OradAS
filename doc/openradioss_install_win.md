# OpenRadiossのインストール

OpenRadiossのインストール手順について示します。ここではWindows版のインストール方法を示します。

## インストーラのダウンロード

OpenRadiossのパッケージを[GithubのReleaseページ](https://github.com/OpenRadioss/OpenRadioss/releases )からダウンロードします。

最新版をダウンロードするようにしてください。

![image-20240329172740193](.\assets\image-20240329172740193.png)

ダウンロードしたファイルを解凍してください。

![image-20240330093016627](.\assets\image-20240330093016627.png)

## Intel MPI Libraryのインストール

並列計算のためにIntel MPI Libraryのインストールが必要になります。[Intel MPI Libraryのページ](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html#mpi)にアクセスします。Windowsのインストーラをクリックしダウンロードします。このドキュメントではOnline版をダウンロードしています。

![image-20240330103511375](./assets/image-20240330103511375.png)

ダウンロードされたインストーラを起動します。

![image-20240330105507580](./assets/image-20240330105507580.png)

起動したらシステムのチェックが始まるので、Continueをクリックします。

![image-20240330105533445](./assets/image-20240330105533445.png)

チェックが終わるとインストール設定画面が表示されるので、I accept the term of the license agreementにチェックを入れて、Continueをクリックします。

![image-20240330105708821](./assets/image-20240330105708821.png)

インテルのソフトウェア改良プログラムに参加するかどうか聞いてくる画面が表示されますので、好きな方を選んでInstallをクリックします。

![image-20240330105903045](./assets/image-20240330105903045.png)

しばらく待ちます。

![image-20240330105929981](./assets/image-20240330105929981.png)

インストールが終わったら小さなウィンドウが表示されるので、Finishをクリックして終了します。
![image-20240330105956555](./assets/image-20240330105956555.png)

これでインストールは終了です。
