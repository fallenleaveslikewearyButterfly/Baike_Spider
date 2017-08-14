__author__ = "Liang"
__Date__ = 2017 / 8 / 13
#-*- coding:utf-8 –*-

class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=open("output.html","w",encoding="utf-8")
        fout.write(" <!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' ' \
                ''http://www.w3.org/ TR/xhtml1/DTD/xhtml1-transitional.dtd'>");
        fout.write("<html><head><meta http-equiv='Content-Type' content='text/html; charset=UTF-8'></head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'])
            fout.write("<td>%s</td>"%data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()