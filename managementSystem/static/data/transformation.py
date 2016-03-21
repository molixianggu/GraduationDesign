from win32com import client as wc
import os

def wordsToHtml(fileName):#批量把文件夹的word文档转换成html文件
    word = wc.Dispatch('word.Application')
    doc = word.Documents.Open(os.path.join(os.getcwd(), fileName))
#    wordFile2 = unicode(wordFile, "gbk")
    doc.SaveAs(os.path.join(os.getcwd(), 't.html'), 8)
    doc.Close()
    word.Quit()
def excelToHtml(fileName):
    excel = wc.Dispatch('Excel.Application')
    doc = excel.Workbooks.Open(os.path.join(os.getcwd(), fileName))
#    wordFile2 = unicode(wordFile, "gbk")
    doc.SaveAs(os.path.join(os.getcwd(), 't2.html'), 44)
#   
    doc.Close()
    excel.Quit()
#    print(excel)

#    for path, subdirs, files in os.walk(dir):
#        for wordFile in files:
#            wordFullName = os.path.join(path, wordFile)
#            #print "word:" + wordFullName
#            doc = word.Documents.Open(wordFullName)
# 
#            wordFile2 = unicode(wordFile, "gbk")
#            dotIndex = wordFile2.rfind(".")
#            if(dotIndex == -1):
#                print '********************ERROR: 未取得后缀名！'
# 
#            fileSuffix = wordFile2[(dotIndex + 1) : ]
#            if(fileSuffix == "doc" or fileSuffix == "docx"):
#                fileName = wordFile2[ : dotIndex]
#                htmlName = fileName + ".html"
#                htmlFullName = os.path.join(unicode(path, "gbk"), htmlName)
#                # htmlFullName = unicode(path, "gbk") + "\\" + htmlName
#                print u'生成了html文件：' + htmlFullName
#                doc.SaveAs(htmlFullName, 8)
#                doc.Close()
 

excelToHtml('t.xls')