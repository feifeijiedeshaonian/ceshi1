# 发送邮件
import smtplib
# 邮件格式
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import dingtalkchatbot.chatbot as cb


def send_email(text):
    username = 'zhangkai@tjmeiteng.com'
    password = '960811kai'
    sender = 'zhangkai@tjmeiteng.com'
    receiver = ['wanghui01@tjmeiteng.com']
    msg = MIMEMultipart('mixed')
    # 邮件标题
    msg['Subject'] = Header("接口自动化测试报告", 'utf-8')
    msg['From'] = 'zhangkai@tjmeiteng.com<zhangkai@tjmeiteng.com>'
    msg['To'] = ";".join(receiver)
    # 邮件内容
    # text = "接口自动化测试完成"
    # 邮件内容的格式
    text_plain = MIMEText(text, 'plain', 'utf-8')    
    msg.attach(text_plain)
    # 固定的格式
    smtp = smtplib.SMTP()    
    smtp.connect('smtp.tjmeiteng.com')
    smtp.login(username, password)    
    smtp.sendmail(sender, receiver, msg.as_string())    
    smtp.quit()


def send_ding(text):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=df7b27f80294c7d4f543c1e576999b014b4da9a207f3a5e22291c065451e06b7'
    ding = cb.DingtalkChatbot(webhook)
    ding.send_text(msg=text, is_at_all=True)


def send_main(pass_list, fail_list):
    pass_num = float(len(pass_list))
    fail_num = float(len(fail_list))
    count_num = pass_num + fail_num
    pass_result = "%.2f%%" % (pass_num/count_num*100)
    fail_result = "%.2f%%" % (fail_num/count_num*100)
    text = "接口自动化测试完成，此次一共运行接口%d个，测试通过%d个，失败%d个，通过率为%s，失败率为%s" % (count_num, pass_num, fail_num, pass_result, fail_result)
    send_email(text)
    send_ding(text)



if __name__ == "__main__":   
    send_main([1,2,3], [1,2])