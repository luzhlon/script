
def Get22(n):
    i = 0
    while n > 1:
        n /= 2
        i+=1
    return i

def main():
    fip = open('ip.txt', 'r')
    fff = open('ip2.txt', 'w')
    while True:
        line = fip.readline()
        if line:
            #print line
            ss = line.split('|')
            if len(ss) < 4:
                continue
            if ss[1]=='KR' and ss[2]=='ipv4':
                bits = Get22(int(ss[4]))
                ll = ss[3] + '/' + str(bits) + '\n' 
                fff.write(ll)
        else:
            break
    pass

if __name__=='__main__':
    main()
