import zmail
import dingtalkchatbot.chatbot as cb


def send_email(text):
    mail = {
        # 邮件主题
        'subject': '接口自动化测试报告',
        # 邮件内容
        'content_text': text,
        # 邮件中附件
        # 'attachments': [r'F:/3.png'],
    }
    server = zmail.server("zhangkai@tjmeiteng.com", "960811kai")
    server.send_mail("wanghui01@tjmeiteng.com", mail)


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
    # send_ding(text)


if __name__ == "__main__": 

    send_main([1, 2, 3], [1, 2])