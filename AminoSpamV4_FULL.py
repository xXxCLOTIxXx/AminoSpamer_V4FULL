import amino
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.DARK_GREEN_SEA + style.BOLD)
print("""Script by CLOTI(Xsarz)
Github : https://github.com/xXxCLOTIxXx""")
print(pyfiglet.figlet_format("AminoSpamV4 FULL", font="eftitalic"))
client = amino.Client()    
while True:
    email = input("Почта >> ")
    password = input("Пароль >> ")
    try:
        client.login(email=email, password=password)
        break
    except Exception as ex:
        print(f"\n\n\nНе удалось войти в аккаунт\n{ex}\n\n\n")
while True:
    try:
        chat = client.get_from_code(input("Чат для атаки>>")).json
        chatId = chat['extensions']['linkInfo']['objectId']
        comId = chat['extensions']['linkInfo']['ndcId']
        sub_client = amino.SubClient(comId=comId,profile=client.profile)
        print("\n\nДанные успешно получены!\n\n")
        break
    except:
        print("\n\nПроизошла ошибка!\n\n")



message = input("Сообщение >> ")
try:
    while True:
        print("Спамим...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
            _ = [

                executor.submit(
                    sub_client.send_message,
                    chatId,
                    message) for _ in range(100000)]
except Exception as ex:
    print(f"Произошла ошибка!\n\n{ex}")
            
            