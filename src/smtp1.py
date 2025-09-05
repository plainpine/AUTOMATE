import smtplib

smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("plainpinex828@gmail.com", "qQQ&@(%LLL520585")
smtpObj.sendmail(
    "plainpinex828@gmail.com",
    "plainpinex828@gmail.com",
    "Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob",
)
smtpObj.quit()
