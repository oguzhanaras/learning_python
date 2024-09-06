import db_setup
import auth
import flights


def my_app():
    while True:
        print("""***************
        Uçuş rezervasyon sistemine hoşgeldiniz
        1- Kayıt ol
        2- Giriş yap
        3- Uçuşları ara
        4- Rezervasyon yap
        5- Rezervasyon geçmişini gör
        6- Çıkış yap
        7- Programı sonlandır
        ****************""")
        choose = input("Yapmak istediğiniz işlemi girin: ")

        if choose == "7":
            print("Program sonlanıyor...")
            break

        elif choose == "1":
            username = input("Bir kullanıcı adı girin: ")
            password = input("Bir şifre girin (en az 8 karakter): ")
            if len(password) < 8:
                print("Şifre en az 8 karakter olmalı.")
            else:
                auth.register(username, password)

        elif choose == "2":
            if auth.current_user is None:
                username = input("Kullanıcı adını girin: ")
                password = input("Şifrenizi girin: ")
                auth.login(username, password)
            else:
                print("Giriş yapmadan önce mevcut hesabınızdan çıkış yapın.")

        elif choose == "3":
            from_where = input("Nereden uçmak istiyorsunuz: ")
            where = input("Nereye uçmak istiyorsunuz: ")
            flights_res = flights.show_flights(from_where, where)

            if flights_res:
                for fly_id, airline, d_city, a_city, d_time, a_time, price in flights_res:
                    print(f"""
                    Uçuş numarası: {fly_id}
                    Hava yolu: {airline}
                    Kalkış: {d_city}, Varış: {a_city}
                    Kalkış saati: {d_time}, Varış saati: {a_time}
                    Fiyat: {price}
                    """)

        elif choose == "4":
            if auth.current_user:
                pick_fly = input("Rezervasyon yapmak istediğiniz uçuş numarasını girin: ")
                flights.reservation(pick_fly)
            else:
                print("Lütfen önce giriş yapın.")

        elif choose == "5":
            if auth.current_user:
                reservations = flights.show_reservation()
                if reservations:
                    for res_id, user_id, flight_id, res_date in reservations:
                        print(f"Rezervasyon ID: {res_id}, Uçuş ID: {flight_id}, Tarih: {res_date}")
                else:
                    print("Rezervasyon bulunamadı.")
            else:
                print("Lütfen giriş yapın.")

        elif choose == "6":
            if auth.current_user:
                auth.logout()
            else:
                print("Mevcut giriş yapmış hesabınız yok.")


if __name__ == '__main__':
    db_setup.create_tables()
    my_app()