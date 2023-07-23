# AsiaYo Demo Project
- [AsiaYo Demo Project](#asiayo-demo-project)
  - [專案說明](#專案說明)
  - [版本](#版本)
  - [Git Clone Porject](#git-clone-porject)
  - [Docker 部署](#docker-部署)
  - [Local 啟動](#local-啟動)
  - [單元測試](#單元測試)
  - [API使用方式](#api使用方式)
  
## 專案說明
```
    1. 使用python - Django Framework建立一支換率轉換API，可透過登入系統進入Swagger API文件並且測試，
    因為登入系統的緣，這裡選用較輕便的sqlite作為資料庫使用。

    2. 啟動方式可透過Docker(部署) / Runserver(開發)來啟動。

    3. 本專案僅針對function做單元測試，未針對API進行測試。
```

## 版本
```
Python：3.9.17
Django：4.0.4
DB: Sqllite
```

## Git Clone Porject
```
    >> cd <PATH>/
    >> git clone https://github.com/Neil0406/asiayo-demo.git
```

## Docker 部署
Add env file
```
    >> cd <PATH>/asiayo-demo/
    >> touch .env (參考.env.example檔案輸入帳號 / 密碼)
```
Start Docker
```
    >> docker-compose up --build
```
Swagger Login
```
    1. 開啟瀏覽器
    2. 網址： http://localhost:8000/__hiddenswagger/
    3. [.env]帳號密碼
```

## Local 啟動
Install 
```
    >> cd <PATH>/asiayo-demo/asiayo-demo/
    >> pip3 install -r requirements.txt (Mac可能無法安裝uWSGI，須先將uWSGI移除)
```
Create DB
```
    >> cd <PATH>/asiayo-demo/asiayo-demo/
    >> python manage.py makemigrations 
    >> python manage.py migrate
    >> python manage.py collectstatic
```
Create Superuser
```
    >> python manage.py createsuperuser
```

Start Server
```
    >> python manage.py runserver
```

Swagger Login
```
    1. 開啟瀏覽器
    2. 網址： http://localhost:8000/__hiddenswagger/
    3. [Create Superuser]帳號密碼
```

## 單元測試
```
    1. 測試位置：
        - <PATH>/asiayo-demo/asiayo-demo/main_app/test.py

    2. 開始測試：
        >> cd <PATH>/asiayo-demo/asiayo-demo/
        >> python3 manage.py test
```

## API使用方式
```
    1. Swagger 
        - 參考Docker部署 / Local啟動的[Swagger Login]

    2. Postman 
        - 取得access token 
            [Post]：http://localhost:8000/token
            [Content-Type]：application/json
            [Body]：{"email": "asiayo@gmail.com","password": ""}

        - 取得匯率轉換（範例）：
            [Get]：http://localhost:8000/api/convert_currency?source=USD&target=JPY&amount=$1,525
            [Content-Type]：application/json
            [Header]：{"Authorization": "Bearer <access token>"}
```


