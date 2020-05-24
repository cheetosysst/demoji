# demoji
適用於 i3, bspwm 等 tiling WM 環境，使用 dmenu 建立的 emoji 選擇器

這個表情符號選擇器是在看到 [Luke Smith](https://github.com/lukesmithxyz) 的影片 [dmenu tips: Emojis and more](https://youtu.be/UCEXY46t3OA) 後複製出的類似作品，如果你喜歡這個表情符號選擇器，請去訂閱支持最先創作出這個概念的人。

## 使用
### 選擇器
請先下載安裝 dmenu，我個人用的是 [Endeavour OS](https://endeavouros.com/) 預裝的，詳細安裝不綴述。

準備好後可以先執行測試。
``` bash
sh demoji.sh
```
執行成功的，你會看到以下畫面
~~待補~~

搜尋想要的表情符號按下 Enter，這時會顯示通知已經將表情符號複製到剪貼簿，打開任何文字編輯器 ctrl+c 後就能貼上選定表情符號。有的發行版預設無法正常顯示表情符號，你可以透過更改系統字體或安裝 Cairo 後重新開機，建議後者。

若測試正常可進入下一步，若你用的是 i3wm 或 i3-gaps，可以直接在 config 最後加入以下指令。注意 demoji.sh 必須和 emoji_list 存在同一路徑，才能正常取得表情符號列表。
``` bash
bindsym $mod+e exec "sh /path/to/your/demoji.sh"
```
其中 $mod+e 可以換成你慣用的快捷鍵組合，路徑也請自行設定，相關語法請參考 [i3 文件](https://i3wm.org/docs/userguide.html#configuring)。在這之後請重新載入設定檔或是重新登入，沒噴錯的話按下 Mod+E 就可以叫出選擇器了（註：Mod 鍵一般都是設定為 Super 鍵，也就是俗稱 Windows 鍵）。

在 bspwm 應該大同小異，請自行測試，其他桌面環境也請自行摸索。

### 清單生成器
清單生成器使用前請下載 Python3，用 pip 下載 bs4 和 requests。

``` bash
pip install bs4 requests
```

若表情符號標準有變動，且 Wikipedia 有把改動部份更新到網站上，請執行這個腳本更新清單。
``` bash
python process.py
# 因 python2 已經停止維護，這裡假設你已經安裝好 python3m，且了解當中的差異。
```

執行完成請檢查 emoji_list 內容是否正確
