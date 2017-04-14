import string
if __name__=="__main__":
    ascii=raw_input("cadena: ")
    i=0;
    inHex="";
    inHex2="0x";
    while(i<len(ascii)):
        inHex+=string.replace(str(hex(ord(ascii[i]))),'0x','\\x');
        inHex2+=string.replace(hex(ord(ascii[i])),'0x','');
        i+=1;
    print "hex: "+inHex;
    print "hex: "+inHex2;
    
