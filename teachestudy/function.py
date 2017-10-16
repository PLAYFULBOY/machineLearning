def test(a,b,c = 1):
    a = 3
    b = 2
    print("hhhh")
    print(a,b,c)

def multi(fpara, *num, **words):
    print("fpara : " + str(fpara))
    print("*num :" + str(num))
    print("**word : " + str(words))
    
multi("hello",1, 2, 3, 4,word = "python",a_word = "hhhh")