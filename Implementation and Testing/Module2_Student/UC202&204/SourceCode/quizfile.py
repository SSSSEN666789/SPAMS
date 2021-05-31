def txt_qize(num):
    fnum = 1
    filename = "quiz%d.txt" % (fnum)
    f= open(filename,'w')
    print("Write down your answer: ")
    for i in range(0,num):
        a = input()
        f.write(a)
        f.write('\n')
    fnum += 1
    f.close()

    return filename
