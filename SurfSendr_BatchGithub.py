import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sqlite3
import sys
#sys.setdefaultencoding('utf8')

# select random msg

while True:
	try:
		conn = sqlite3.connect('SurfSend.db')
		cursor = conn.cursor()
		cur2 = cursor.execute("select surfmaster2.swellsizeft, surfmaster2.beach_name, surfmaster2.date_, ArtistMonitor.email from surfmaster2 join ArtistMonitor on SurfMaster2.beach_name = ArtistMonitor.DJName where SwellSizeFt = '  4';")
		info2 = cur2.fetchall()
		conn.commit()
		conn.close()
		conn.close()

		#swellsizeft
		for x in info2:
			j = x[0]
			#beachname
			k = x[1]
			#date
			l = x[2]
			#email
			m = x[3]

			# print(j + 'ft' ' @ ' + k + ' on ' + l)

			# select email addresses as list to send to
			conn5 = sqlite3.connect('SurfSend.db')
			cursor5 = conn5.cursor()
			cur5 = cursor5.execute('SELECT email FROM ArtistMonitor WHERE delivery = "EmailMsg"')
			info5 = cur5.fetchall()
			conn5.commit()
			conn5.close()
			conn5.close()

			newlist = [row[0] for row in info5]


			msg = MIMEMultipart()
			msg['From'] = 'mkramer265@gmail.com'
			msg['To'] = 'mkramer789@gmail.com'
			msg['Subject'] = 'Funny'
			message = j + 'ft' ' @ ' + k + ' on ' + l
			print(message)
			msg.attach(MIMEText(message))

			mailserver = smtplib.SMTP('smtp.gmail.com',587)
			# identify ourselves to smtp gmail client
			mailserver.ehlo()
			# secure our email with tls encryption
			mailserver.starttls()
			# re-identify ourselves as an encrypted connection
			mailserver.ehlo()
			mailserver.login('mkramer265@gmail.com', '')

			mailserver.sendmail('mkramer265@gmail.com',newlist,msg.as_string())

			mailserver.quit()

		# connx = sqlite3.connect('StriveDB2.db')
		# cursorx = connx.cursor()
		# curx = cursorx.execute("INSERT INTO RIDX VALUES (?)", (k,))
		# connx.commit()
		# cursorx.close()
		# connx.close()
		break

	except UnicodeEncodeError:
		pass
	
print('We broke outside of the loop. That means we must have succeeded')
