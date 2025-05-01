import json

# 将你的 credentials.json 内容完整粘贴到下面（注意保持格式，\n 必须保留）
credentials_data = {
  "type": "service_account",
  "project_id": "cosmic-surface-458502-k2",
  "private_key_id": "2cbb043b9ec42778a90db3b254d31f8739556432",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDOBVauG4csgWS4\\n40FZJilEj9UJHN0U8Gdnw5bRjfO0AMg+ROWTYBddDPwh0BXLkFHcWgxniw1zU6wr\\neQdkdCJMDFu9vKH4jLadVC3vr21U6RZ704wkwH7XT657J+acLdERzUYcnfOZXgKN\\ntNR8qfmM7psxgYzIf1Dj7nqriK82BakuEfatHZ+vR7XEnb+bqad19/FPIdyo70u9\\nlqjOWBFWJ9hyMs5aHOrTff/4UbgBYVlR0fhf21trlzG3MPi6NCiH3yjOv20DzR4h\\nz/gzW3zdM6gjgo+07EBzsE11HBGbHTV2AjKqGL5JEsxt2rcWeOXX5U97GBWBNp5I\\nEUETBRBPAgMBAAECggEAPDJJInQ+qd1g3bjhJjhFRJg2KgR6AJ1ByYrXrYEpnQXB\\nfJhK8CXajcC2hvay95jConzZNQPnOTRQkR867roUL15JDAZq2SHcVdn71hXO/0lf\\n3WxxfWeVaDoLBEcjVaz5cpclDkWEoOJcIqWclJRhqzEovW1aAldY/lB3HVnBwCme\\ncRfG1hsUN9HzBrTeQzcVbfDQRPcHrJ84A9wKRPXyg9j+m7qFXGu0OAnToSUQJOch\\nyRfoi17t7kGds+N/8USNVHITjaU3WzvMtAyFjj5+3k5QbxMbnoWm2mmnnRzqGPO3\\ni8q6F4s1w0bzckZ6MNbLVtY4x8QAlfe9avrkdcX7eQKBgQD88QFW2mPd/qHHUZzu\\njLVvksrXjHStQz40oJifg43OrfXLdmueY3vBuPQlrE4/6niRHQp/VeInFV6n5rI5\\nsfzH54P0l83Vmks8dzDjW5kLiFSe9dkAjgc4/xqBpoCDwLFmJpvyU5S8O/gAkQF2\\nXyCTPeUyvSNl6s1ucX+Ocy0zmwKBgQDQgxaIxt5bLdhcW+4S7PPPAize3DvV5cDb\\nZMFrlHMTZqC9GFGe29ZmbhRs3CWtFYPnqPjPBgzQAEq/S+MHNq4IBIl1zk8Q/upc\\nIIuDxGoFCH4aEkaUkj4q5TX7M+V0SzQD1Fy/ZE7qjjz4hmSybWbyH6C+enx0hj5c\\nfmyX5CODXQKBgQCtNCcznzZVlICZaSRqIYY4Ua9+rFpVLr+Q8Auy5zWaunqeiYem\\nHP9op0rf5T5r/BX1YIqIqXnEQ5jeplWStnOfO8SbH7w+MXqlfATJGzcQs5kmhLjE\\n7Xy6pc0zzJ0iGzge9/8/j8ZAo1vun1z9/qPiz7Z76RItPvzPTP8Iv4vLUwKBgQDQ\\nV+uQR4WufaSOxJyh9Hm5AmdrV4vCMov9rDNIF1DUtdsulroXjXoxZxSpoV9UDwd5\\n1nCmC1mKDICjnGQAtTY3dLEVMUv3o37xBuPgicWVueKmklRL58SOf/DsS/KdvPcA\\nTJVP+B6SaAWsHj1Hu+D9VXT8Xs80b16odPp02tRRUQKBgHrfusMZkz3nuKLO6fud\\nOunB4XhwOY1n/I27WEwNJLbmUcJl6Sd2v/O/pJERap9AC4F07Ni37op9wqhp1h6e\\n42FjEAGtscVcWpxpSzpHP54AfKc0/PIULThcxH5kx5NVulOhGRdfm2uR187BArTY\\nY8MoiHUkWpNsqKc//SoQ14Am\\n-----END PRIVATE KEY-----\\n",
  "client_email": "for-lunarcrush-uploader-projec@cosmic-surface-458502-k2.iam.gserviceaccount.com",
  "client_id": "118384732657974491732",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/for-lunarcrush-uploader-projec%40cosmic-surface-458502-k2.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

with open("credentials.json", "w", encoding="utf-8") as f:
    json.dump(credentials_data, f, indent=2)

print("✅ 已成功写入 credentials.json")