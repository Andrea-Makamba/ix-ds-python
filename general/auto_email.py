import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
def send(name, short, desc):
    fromaddr = "seanwademail@gmail.com"
    toaddr = "{}@adobe.com".format(short)
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Research Internship"

    first_name = name.split(" ")[0]
    
    body = """ 
Hi {},

My name is Sean and I am a new graduate student at BYU researching in computer science and machine learning. Specifically, I have done work in computer vision, deep learning, and reinforcement learning. Chris Spencer works with one of my professors and told me about your research at Adobe in {}. I find this really interesting and I think that my background could be well suited for this.

I applied through research at Adobe, but I was particularly interested in your work and wanted to reach out ot you personally so you know who I am. Attached is a copy of my resume and you can see more at my personal site seanwade.com. Let me know if you have any questions or would like to talk.

Thanks,

Sean Wade
""".format(first_name, desc)
    
    msg.attach(MIMEText(body, 'plain'))
    
    filename = "Sean Wade Resume"
    attachment = open("/Users/seanwade/Downloads/sean_wade_resume.pdf", "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "PASSWORD")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("sent: {}".format(short))

names = [
    'Jovan Popović',
    'Oliver Wang',
    'Stephen DiVerdi',
    'Geoffrey Oxholm',
    'Jon Brandt',
    'Hung Bui',
    'Walter Chang',
    'Chen Fang',
    'Tom Jacobs',
    'Yasin Abbasi Yadkori',
    'Sungchul Kim',
    'Branislav Kveton',
    'Georgios Theocharous',
    'Zheng Wen'
]

short_name = [
    'jovan',
    'owang',
    'diverdi',
    'oxholm',
    'jbrandt',
    'hubui',
    'wachang',
    'cfang',
    'jacobs',
    'abbasiya',
    'sukim',
    'kveton',
    'theochar',
    'zwen'
]

desc = [
    'learning and control',
    'machine learning and vision',
    'virtual reality and painting',
    'computer vision and machine learning',
    'visual search and machine learning',
    'probabilistic inference and deep learning',
    'NLP and dialog systems',
    'recognition and computer vision',
    'big data systems and IOT',
    'online and reinforcement learning',
    'data mining and predictive analytics',
    'online leanring and artificial intelligence',
    'reinforcement learning',
    'online learning'
]

if __name__ == '__main__':
    for i in range(len(names)):
        send(names[i], short_name[i], desc[i])
