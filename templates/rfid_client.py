# -*- coding: utf-8 -*-
import requests
import keyboard

URL = "https://xinxigaosu.onrender.com/rfid"
buf = ""
print("=== 中文RFID读卡客户端 ===")
print("等待刷卡...（刷卡后自动上传并播报）")

while True:
    e = keyboard.read_event()
    if e.event_type == keyboard.KEY_DOWN:
        k = e.name
        if k == "enter":
            if len(buf) > 4:
                try:
                    res = requests.post(URL, data={"rfid": buf})
                    print("✅ 上传成功：", res.json())
                except Exception as err:
                    print("❌ 上传失败：", err)
            buf = ""
        else:
            buf += k
