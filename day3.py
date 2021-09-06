  
def fun1(a,b=0,*args,**kwargs):
    print("a=",a,"\nb=",b,"\nargs=",args,"\nkwargs=",kwargs)

fun1(10,20,20,30,40,50,brand="hp",generation="5th")