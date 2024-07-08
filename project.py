from getcolor import colors
from pickle import FALSE, TRUE
import tkinter as tk


root = tk.Tk()
root.title("calculator")
root.geometry("210x293+500+350")
root.configure(bg=colors["rootColor"]) 
root.resizable(False,False)


buff = 0
op = '' 
t = FALSE


 #avelacnum e mutqagrvac tivy
def app (ch):

    global op
    global buff

    #ete naxkinum unecel enq ardyunq apa jnjel da ev grel nory
    if op == '='  and ch != '<':
        ntr['text'] = ''
        ntr["text"] += ch

    elif ch == '<':

        if len(ntr.cget('text') ) == 1:
            ntr['text'] = ''
            output['text'] = ''

        else:
            ntr['text'] = ntr.cget('text')[:-1]
      
    else :
        ntr["text"] += ch
   
    #stugel ete naxkinum gorcoxutyun chi katarvel chkatari tvabanakan gorcoxutyun
    if type (buff) is float and (ntr.cget('text') != '' or ntr.cget('text') == '-') :

        if op == '+': 
            output['text'] = str (float (ntr.cget('text')) + buff) #naxord unecac arjeqin avelacnel nor mutqagrvac tivy

        if op == '-': 
            output['text'] = str ( buff - float (ntr.cget('text')))
        
        if op == '*': 
            output['text'] = str (float (ntr.cget('text')) * buff)

        if op == '/': 
            output['text'] = str ( buff / float(ntr.cget('text')))
          

def istrue (opp):
    global t                
    global buff
    global op
    op = opp    

    if opp == '=' and len (output.cget('text') ) > 0 and len (ntr.cget('text') ) > 0 : 
        ntr['text'] = output.cget('text')
        output['text'] = ''

        t = FALSE

        return
    
    elif opp == '-' and ntr['text'] == '':
      
        ntr['text'] = '-'
      
    if t == TRUE:
        buff = float (output.cget('text'))
    elif ntr.cget('text') != '':
        buff = float(ntr.cget('text'))
        t = TRUE
    
    ntr['text'] = ''
  

def AC ():
    global buff
    global op
    global t
    ntr['text'] = ''
    output['text'] = ''
    buff = 0
    op = '' 
    t = FALSE


ntr = tk.Label(root , bg= colors["labelColor"],
                width = 23,height = 1,
                font= 30
                )

output = tk.Label(root , bg = colors["labelColor"],
                width =30,height = 2,
                )

cln = tk.Button(root, bg = colors["popColor"],
                text = 'AC',
                height= 3, width=5,
                command = lambda :AC()
                )

pop = tk.Button(
                root, bg = colors["popColor"],
                text = '<',
                height= 3, width=5 ,
                command = lambda :app('<')
    )

btnH = tk.Button(root,bg = colors["actionColor"],
                 text = '=',
                 height= 3, width=10, 
                 command= lambda :istrue('=')                 
                 )

btnHN = tk.Button(root, bg = colors["actionColor"],
                 text = '-',
                 height= 3, width=5,
                 command= lambda :istrue('-')                 
                 )

btnS = tk.Button(root, bg = colors["actionColor"],
                 text = '+',
                 height= 3, width=5,
                 command = lambda: istrue('+')
               
                 )

btnB = tk.Button(root, bg = colors["actionColor"],
                 text = '/',
                 height= 3, width=5,
                 command= lambda :istrue('/')
                 )

btnBB = tk.Button(root, bg = colors["actionColor"],
                 text = '*',
                 height= 3, width=5,
                 command= lambda : istrue('*')
                 )

btn1 = tk.Button(root, bg = colors["numberColor"],
                 text = '1',
                 height= 3, width=4,
                 command = lambda :app('1')
                  )

btn2 = tk.Button(root, bg = colors["numberColor"],
                 text = '2',
                 height= 3, width=4,
                 command = lambda :app('2')
                 )

btn3 = tk.Button(root, bg = colors["numberColor"],
                 text = '3',
                 height= 3, width=4,
                 command = lambda :app('3')
                 )

btn4 = tk.Button(root, bg = colors["numberColor"],
                 text = '4',
                 height= 3, width=4,
                 command = lambda :app('4')
                 )

btn5 = tk.Button(root, bg = colors["numberColor"],
                 text = '5',
                 height= 3, width=4,
                 command = lambda :app('5')
                 )

btn6 = tk.Button(root, bg = colors["numberColor"],
                 text = '6',
                 height= 3, width=4,
                 command = lambda :app('6')
                 )

btn7 = tk.Button(root, bg = colors["numberColor"],
                 text = '7',
                 height= 3, width=4,
                 command = lambda :app('7')
                 )

btn8 = tk.Button(root, bg = colors["numberColor"],
                 text = '8',
                 height= 3, width=4,
                 command = lambda :app('8')
                 )

btn9 = tk.Button(root, bg = colors["numberColor"],
                 text = '9',
                 height= 3, width=4,
                 command = lambda :app('9')
                 )

btn0 = tk.Button(root, bg = colors["numberColor"],
                 text = '0',
                 height= 3, width=4,
                 command = lambda :app('0')
                 )


cln.place   (x=166, y=178)
pop.place   (x=166, y=237)
ntr.place   (x=0  , y=0  )
output.place(x=0  , y=24 )
btn1.place  (x=0  , y=178)
btn2.place  (x=40 , y=178)
btn3.place  (x=80 , y=178)
btn4.place  (x=0  , y=119)
btn5.place  (x=40 , y=119)
btn6.place  (x=80 , y=119)
btn7.place  (x=0  , y=61 )
btn8.place  (x=40 , y=61 )
btn9.place  (x=80 , y=61 )
btn0.place  (x=0  , y=237)
btnH.place  (x=40 , y=237)
btnHN.place (x=120, y=237)
btnS.place  (x=120, y=178)
btnB.place  (x=120, y=119)
btnBB.place (x=120, y=61 )


root.mainloop()