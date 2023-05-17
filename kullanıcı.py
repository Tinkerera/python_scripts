def giris():
    username = input("Kullanıcı Adı: ")
    password = input("Şifre: ")

    with open("kullanici_bilgileri.txt", "r") as dosya:
        for satir in dosya:
            user, password_ = satir.strip().split(",")
            if user == username and password_ == password:
                print("Giriş yapıldı")
                return

    print("Kullanıcı adı veya parola yanlış")
    print(username,password)
giris()
