class Ar_bin:
    def Int_to_bin(self, Int):
        result = Int
        numero = result
        bin = ''
        while result != 1:
            result = numero//2
            resto = numero%2
            bin = str(resto) + bin
            numero = result
        return str(result) + bin
    
    def Bin_to_int(self, Bin):
        list_num = [int(Bin[i]) for i in range(len(Bin)-1, -1, -1)]
        Int = 0
        for i in range(len(list_num)):
            alg = int(list_num[i])
            pos = i
            op = alg*(2**pos)
            Int += op
        return Int

def main():
    arbin = Ar_bin()
    escolha = input('0 - Int to bin\n1 - Bin to Int\n> ')
    if escolha == '0':
        inteiro = int(input('\nInt > '))
        print('\n'+str(arbin.Int_to_bin(inteiro)))
    else:
        bin = input('\nBin > ')
        print('\n'+str(arbin.Bin_to_int(bin)))

if __name__ == '__main__':
    main()
