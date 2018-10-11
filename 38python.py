import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("vinayakakprasad@gmail.com", "6362620320")
 
msg = "Hello!"
server.sendmail("vinayakakprasad@gmail.com", "meghanaprasad2299@gmail.com", msg)
server.quit()

