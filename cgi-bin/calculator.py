#!/bin/env python
import cgi
from basiccal import check,operate
header = 'Content-Type: text/html\n\n'
formhtml = '''<HTML><HEAD><TITLE>
Calculator Demo (static screen)
</TITLE></HEAD>
<BODY><H3>Input your numbers:</H3>
<FORM ACTION="/cgi-bin/calculator.py">
<INPUT TYPE=hidden NAME=action VALUE=edit>
<B>Enter your first value:</B>
<INPUT TYPE=text NAME=num1 VALUE="0" SIZE=15><br>
<B>Enter your second value:</B>
<INPUT TYPE=text NAME=num2 VALUE="0" SIZE=15><br>
<P><B>Operation:</B>
%s
<P><INPUT TYPE=submit></FORM></BODY></HTML>'''


fradio = '<INPUT TYPE=radio NAME=op VALUE="%s" %s> %s\n'

def showForm():
 convertop = {'plus':'+', 'minus':'-', 'multiply':'*', 'divide':'/'}
 operations = []
 for i in convertop:
  operations.append(fradio % (i,'',convertop[i]))
 print(('%s%s' % (header, formhtml % ''.join(operations))))

reshtml = '''<HTML><BODY><H3>Your results: <I>%s</I></H3>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''


errorhtml = '''<HTML><BODY><H3>There was an error: <I>%s</I></H3>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''

def process():

 form = cgi.FieldStorage()
 if 'num1' in form:
  num11 = form['num1'].value
 if 'num2' in form:
  num22 = form['num2'].value
 if 'op' in form:
  op = form['op'].value
 else:
  op = 'plus'

 if 'action' in form:
  num1=check(num11)
  num2=check(num22)
  if num1 is not 'nonfloat' and num2 is not 'nonfloat':
   num=operate(num1,num2,op)
   print((header + reshtml % (str(num))))
  else:
   print((header + errorhtml % ('PLEASE ENTER A VALID NUMBER')))
 else:
  showForm()

if __name__ == '__main__':
 process()
                                                                                                                   
