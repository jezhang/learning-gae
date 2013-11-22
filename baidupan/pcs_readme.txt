应用名称:jezhang.info 
应用ID:1469382
API Key:4XetgNeZqQrY22EHow2ZlWFn
Secret Key:MMLgf5i2efa4tDS7OxVaO0aKv9O8qfNR
=====================================================================================================
获取ACCESS TOKEN(client_id=Your API KEY, 30天有效)
https://openapi.baidu.com/oauth/2.0/authorize?response_type=token&client_id=4XetgNeZqQrY22EHow2ZlWFn&redirect_uri=oob&scope=netdisk
=====================================================================================================
获取Authorization Code(每一个Authorization Code的有效期为10分钟，并且只能使用一次，再次使用将无效。)
https://openapi.baidu.com/oauth/2.0/authorize?response_type=code&client_id=4XetgNeZqQrY22EHow2ZlWFn&redirect_uri=http%3A%2F%2Fa.jezhang.info%2Foauth_redirect/&scope=&display=popup
=====================================================================================================
通过Authorization Code获取Access Token & Refresh Token
https://openapi.baidu.com/oauth/2.0/token?grant_type=authorization_code&code=09f59f95fb9ded67e66fbadf888ea08e&client_id=4XetgNeZqQrY22EHow2ZlWFn&client_secret=MMLgf5i2efa4tDS7OxVaO0aKv9O8qfNR&redirect_uri=http%3A%2F%2Fa.jezhang.info%2Foauth_redirect/

{"expires_in":2592000,"refresh_token":"4.ca506f29350926edad520b09ad29fd03.315360000.1700463039.1144098186-1469382","access_token":"3.8f277604e2ddfcdadb2e8d5c2509ce53.2592000.1387695039.1144098186-1469382","session_secret":"b814232d5991fa23564899f4e5de3034","session_key":"94rryYsQqVmtBW29zJfBjf\/voF+ync98b8iIUFQ44pSgu7nCgW2+Tepw2UGsM6MSmaPIjECQrgE3A1A9jLs0KJZ179Wrckam","scope":"basic super_msg netdisk"}
=====================================================================================================
https://openapi.baidu.com/oauth/2.0/token?grant_type=refresh_token&refresh_token=4.ca506f29350926edad520b09ad29fd03.315360000.1700463039.1144098186-1469382&client_id=4XetgNeZqQrY22EHow2ZlWFn&client_secret=MMLgf5i2efa4tDS7OxVaO0aKv9O8qfNR&scope=
=====================================================================================================
https://pcs.baidu.com/rest/2.0/pcs/quota?method=info&access_token=3.25d37692ff117451e7ad712a53524b7b.2592000.1387692742.1144098186-1469382