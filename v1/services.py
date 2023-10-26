
from django.core.mail import send_mail


def send_message_email(email,  inviter_email, token, code):
    url = f"http://127.0.0.1:8000/home/?token={token}"
    sarlovha = "Yaxshiyam borsan"
    xabar = f"Sizni {inviter_email} foydalanuvchi  chaqirmoqda"\
        f" Tasdiqlash uchun bitta jonli laykcha quloqchani pasidan busin   "\
            f" Va   bir og'iz  shirin  so'ziyiz {code} marta  yaxshi kuraman  seni"
            
    send_mail(sarlovha, xabar, inviter_email, [email])





    
