Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> deck = [6,7,8,9,10,2,3,4,11]*4#колода карт
import random
z=random.sample(deck,(1))#вибирає рандомом одну карту
count= 0 #
while True:
    
    choice= input ('здати карту?')
    if choice == 'y':
        
        print('Ваша карта дорівнює %s очкам, сума попередніх очків %s' %(z,count))
        
        z=deck.pop()#видаляє елемент рандому
        count=count + z # додає до суми очків кількість очків карти що вибрав рандом
        if count >21:
            print ('you louse')
            break
        
        elif count ==21:
            print ('Win')
        
    if choice == 'n':
        print('У вас %s очкі і гра завершена.' %(count))
        break

    
   

print('Гудбай лузар')
