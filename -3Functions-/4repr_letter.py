def represent(letter):
    '''
    Function that takes a letter and returns the representation of the letter in
    upper-case format
    '''
    patterns = {1:'   *   ',2:'*     *',3:'*******',4:'***   ',5:'*    **',6:'*   * ',7:' *   *',8:'**    ',9:'* *   ',
                'a':' *    ','b':'*     ','c':'  *****','d':'****  ','e':'      *','f':'*   ***','g':' ***** ','h':' *    *',
                'i':'   ****','j':'*  *  ','k':'**    ','l':'**  **','m':'* ** *','n':'*  *  *','o':'**    *','p':'* *   *'
                ,'q':'*  *  *','r':'*   * *','s':'*    **','t':'  ***  ','u':' *   * ','v':'   ** ','w':'     *','x':'  * *  ',
               'y':'   **  ','z':'    * '}

    alphabet = {'A':[1,7,2,3,2,2,2],'B':[4,6,2,6,4,6,2,6,4],'C':['c','b','b','b','b','b','b','c'],'D':[4,6,6,6,6,6,6,4],
                'E':[3,'b','b',4,'b','b',3],'F':[3,'b','b',4,'b','b','b'],'G':['c','b','b','b','f',2,'c','e'],
                'H':[2,2,2,3,2,2,2],'I':['g',1,1,1,1,1,1,'g'],'J':['c','e','e','e','e',2,'h','i'],'K':[2,6,'j',9,'k',9,'j',6,2],
                'L':['b','b','b','b','b','b','b',3],'M':[2,'l','m','n',2,2,2,2],'N':[2,'o','p','q','r','s',2],
                'O':['t','u',2,2,2,2,'u','t'],'P':[4,6,2,6,4,'b','b','b'],'Q':['t','u',2,2,2,'u','t',1,'v'],
                'R':[4,6,2,6,4,8,9,'j',6,2],'S':['g','b','b','g','w','w','g'],'T':['3,1,1,1,1,1,1,1'],'U':[2,2,2,2,2,2,'g'],
                'V':[2,2,'u','u','x',1],'W':[2,2,2,'n','n','n','l'],'X':[2,'u','x','y',1,'y','x','u',2],'Y':[2,'u','x','y',1,1,1,1],
                'Z':[3,'e','z',1,'a','b',3]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])