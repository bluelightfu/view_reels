# 使用指南

請依照以下步驟進行操作：

1. **安裝 EditThisCookie 插件**
   - 前往 Chrome 擴展商店安裝 [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie) 插件，以便獲取 Instagram 的 cookies。

2. **登入 Instagram**
   - 使用您希望用來執行流程的 Instagram 帳號登入您的瀏覽器。

3. **複製 Cookies**
   - 在 Instagram 畫面上，點擊瀏覽器上的 EditThisCookie 插件，然後選擇「匯出」。這會將您的 cookie 複製到剪貼簿。

4. **儲存 Cookies**
   - 請自行建立一個名為 `cookie_ig_original.json` 的文件，將剛剛複製的內容貼上到該文件中。

5. **處理 Cookies**
   - 執行 `cookie_parser.py` 腳本來處理您的 `cookie_ig_original.json` 資料，我們只需要 domain 和 name 的數值。執行後會產生一個名為 `cookie_ig.json` 的文件。

6. **修改 URL 進行測試**
   - 打開 `view_ig_reels.py`，修改您希望測試的 URL 來檢查效果。