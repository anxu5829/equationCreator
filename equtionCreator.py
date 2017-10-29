def equationCreator1(paraMatrix,F):

    numofF = paraMatrix.shape[0]
    F+=" "
    F=F*numofF
    F = [j+"_"+str(i) for i,j in enumerate(F.split(" ")) if j != ""]
    s = "\\[\\begin{array}{c} \t"
    for  i in range(numofF):
        s+= "{{"+F[i]+"} = "
        for j in range(paraMatrix.shape[1]):
            s= s + str(paraMatrix[i,j]) + "{\\rm{x_" + str(j) +"}"
            if j == (paraMatrix.shape[1] -1):
               s = s + "} }  "
            else:
                if paraMatrix[i,j]>0:
                    s =  s + "} + "
                else:
                    s = s + "}  "
        if i!=(paraMatrix.shape[0]-1):
            s+="\\\\ \t"
        else:
            s += "\\end{array}\\]"
    return s




if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    import os
    os.chdir("F:\\普通作业\\多元统计")
    paraMatrix = pd.read_csv("an.txt", sep='\t')
    paraMatrix = np.matrix(paraMatrix)
    paraMatrix = paraMatrix.transpose()
    #paraMatrix = np.matrix([[1,2],[3,3]])
    s= equationCreator1(paraMatrix,"F")
    f=open("output.txt","w")
    f.write(s)
    f.close()
