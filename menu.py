def title():
    print('''
                                                                                                                                                                                                               
   asswo   M                       rd                LI Pa   or     ag       e CLI                                                          sw      na     m                                                   
  mple C   P                       LI               erSimpl  CL     sw       agerSim                                                        e       ssw    Ma                                                  
  Ma                               rS               or   an  er     e        sw    M                                                        ag      le C I Pa                                                  
  Pa       M  agerSimple   I Pass  rd  anager       CL       or     ag       e     P   word   nagerS  ple CL   as    d M  agerSi  le C   Passw      na erSimp   CLI P   word M   gerSi  le CLI   ssword  anag  
   ple C   P  sw  d   na   Si  le  LI  as  or       er       CL     sw       agerSim      I   ss      an       pl    I P  sw  d   na e  im  e       ss  r  Ma      im    C   P      d   na  rS   le  LI  as w  
      ge  im  e   I   ss   d   na  rS  ple CL       or       er     e        sword     gerSi  le CL   asswo    an ge Sim  e   I   ss     M  ag      le     Pa   ord M   ge  im    CLI   ss  rd   nagerS  pl    
      wo   M  ag  Si  le   I   ss  rd  anage        CL       or     ag       e        sword    agerS   le CL   assword M  ag  Si  le     P  sw      na    imp   CLI P   wo   M  agerSi  le  LI   sswor   an    
       C   P  sw  d   na   Si  le  LI  as           er  mpl  CL     sw       ag       e   I       rd      er   ple  LI P  sw  d   na    im  e       ss     Ma  ge  im    C   P  sw  d   na  rS   le      as    
  Manag   im  e   I   ss   d Man   rS   le CL        rd Ma   erSim  e        sw        gerSi  le CL   asswo     n    Si     CLI   ss     Mana       le     Pa   ord M   ge  im    CLI    sword    agerS  pl    
                           I                                                                                                                                                                LI                 
                           Si                                                                                                                                                           nagerS                 
                                                                                                                                                                                                               
                                                                                                                                                                                                               ''')


#Main Menu
def menu():
    print("1. Add New Account.")
    print('2. Find Existing Account.')
    print('3. Update Existing Account.')
    print('4. Deleting Existing Account.')
    print('5. Show All Accounts. ')
    while True:
        try:
            c = int(input('Enter Your Choice......  '))
        except:
            print("Please Enter a numeric value")
            continue
        break
    return c

#testing
#title()
#menu()