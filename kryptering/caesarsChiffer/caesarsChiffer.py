def read_file():    #leser fila og skriver ut de 5 første bokstavene.
    f = open("kryptert_1.txt", "r") 
    print(f.read(50)) 
    f.close

read_file()