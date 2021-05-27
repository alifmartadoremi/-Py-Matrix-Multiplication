__author__="kvda"

class myClass():
    def myFunc(self):
        print("Program penjumlahan/pengurangan dua buah Matriks")
        print("---")
        barisInp = input("Masukkan jumlah baris : ")
        kolomInp = input("Masukkan jumlah kolom : ")
        print("")

        matriks1 = []
        matriks2 = []

        offset = 0
        
        print("Matriks pertama")
        print("---")
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                Amatriks = input("Masukkan angka untuk baris {0} kolom {1} : ".format(offset+1,offset2+1))
                matriks1.append(Amatriks)
                offset2+=1
            offset+=1
        print("---")
        print("Matriks pertama : ")
        print("---")
        offset = 0
        offsetMatriks = 0
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                print(int(matriks1[offsetMatriks]),end=" ")
                offsetMatriks+=1
                offset2+=1
            print(" ")
            offset+=1
        print("---")
        print("")
        
        
        offset = 0
        print("Matriks kedua")
        print("---")
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                Amatriks = input("Masukkan angka untuk baris {0} kolom {1} : ".format(offset+1,offset2+1))
                matriks2.append(Amatriks)
                offset2+=1
            offset+=1
        print("---")
        print("Matriks kedua : ")
        print("---")
        offset = 0
        offsetMatriks = 0
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                print(int(matriks2[offsetMatriks]),end=" ")
                offsetMatriks+=1
                offset2+=1
            print(" ")
            offset+=1
        print("---")
        print("")
        
        print("Hasil dari perkalian matriks anda : ")
        print("---")
        print(" ")
        offset = 0
        offsetMatriks = 0
        while offset<int(barisInp):
            tumbal1 = int(matriks1[offsetMatriks])*int(matriks2[0])
            tumbal2 = int(matriks1[offsetMatriks+1])*int(matriks2[2])
            print(int(tumbal1)+int(tumbal2),end=" ")
            tumbal3 = int(matriks1[offsetMatriks])*int(matriks2[1])
            tumbal4 = int(matriks1[offsetMatriks+1])*int(matriks2[3])
            print(int(tumbal3)+int(tumbal4),end=" ")
            offsetMatriks+=2
            print(" ")
            offset+=1
         
if __name__ == '__main__':
    myClass().myFunc()