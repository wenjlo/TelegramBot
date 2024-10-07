FROM python:3.11.9
# 在container環境內，創建一個stock並移動到stock file裡
WORKDIR /send_tg
# 將當前目錄資料加入到container內的stock資料夾
ADD . /send_tg
# pip 安裝requirements.txt內的套件
RUN python3 -m pip install -r requirements.txt

ENV botserver http://telegram-bot-api:8081
## 最後執行main這個程式，但是我想用另一種方法執行，所以略過
CMD python main.py