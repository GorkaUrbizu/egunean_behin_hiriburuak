import random

def readQuery(file): #CSV fitxategitik hiriburuen datuak irakurri

    with open(file,"r") as f:
        next(f)
        queries = []
        uniqCap = []

        for line in f:
            q = line.strip("\n").split(",")
            query = [q[3],q[1],float(q[5]),float(q[6]),q[2]] #capitalLabel,countryLabel,lon,lat,capital soilik erauzi.
            print(query)

            if q[3] not in uniqCap :
                uniqCap.append(q[3])
                queries.append(query)

        print(len(uniqCap))
        return queries

def getAnswer(Nor, H1, H2, H3): #Erantzun zuzena topatu

    if Nor == "iparralde": #Iparralderago dagoena 5º ko marginarekin lehenengo jarri
        if H1[3] > H2[3]+5 and H1[3] > H3[3]+5:
            return [Nor, H1, H2, H3]
        elif H2[3] > H1[3]+5 and H2[3] > H3[3]+5:
            return [Nor, H2, H1, H3]
        elif H3[3] > H1[3]+5 and H3[3] > H2[3]+5:
            return [Nor, H3, H1, H2]

    elif Nor == "hegoalde": #Hegoalderago dagoena 5º ko marginarekin lehenengo jarri
        if H1[3] < H2[3]-5 and H1[3] < H3[3]-5:
            return [Nor, H1, H2, H3]
        elif H2[3] < H1[3]-5 and H2[3] < H3[3]-5:
            return [Nor, H2, H1, H3]
        elif H3[3] < H1[3]-5 and H3[3] < H2[3]-5:
            return [Nor, H3, H1, H2]

    elif Nor == "ekialde": #Ekialderago dagoena 5º ko marginarekin lehenengo jarri

        if H1[3] > H2[2]+5 and H1[2] > H3[2]+5:
            return [Nor, H1, H2, H3]
        elif H2[3] > H1[2]+5 and H2[2] > H3[2]+5:
            return [Nor, H2, H1, H3]
        elif H3[3] > H1[2]+5 and H3[2] > H2[2]+5:
            return [Nor, H3, H1, H2]

    elif Nor == "mendebalde": #Mendebalderago dagoena 5º ko marginarekin lehenengo jarri
        if H1[3] < H2[2]-5 and H1[2] < H3[2]-5:
            return [Nor, H1, H2, H3]
        elif H2[3] < H1[2]-5 and H2[2] < H3[2]-5:
            return [Nor, H2, H1, H3]
        elif H3[3] < H1[2]-5 and H3[2] < H2[2]-5:
            return [Nor, H3, H1, H2]
            
    return 0

def generateGalderak(queries,n):

    noranzkoak = ["iparralde","hegoalde","ekialde","mendebalde"]
    galderak = []
    i = 0
    qlen = len(queries)
    while i < n:
        Nor = noranzkoak[random.randint(0, 3)]
        H1 = queries[random.randint(0, qlen-1)]
        H2 = queries[random.randint(0, qlen-1)]
        H3 = queries[random.randint(0, qlen-1)]

        if H1[1] != H2[1] and H2[1] != H3[1] and H1[1] !=H3[1] : #herrialde ezberdinetakoak badira (badaude hiriburu bat baino gehiagoko herrialdeak)
            galdera = getAnswer(Nor, H1, H2, H3)

            if galdera:
                galderak.append(galdera)
                i+=1


    return galderak

def writeGalderak(galderak, outfile):

    with open(outfile, "w") as out:
        out.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % ('Mota','Galdera','Irudia','Zuzena','Oker1','Oker2','Jatorria','Esteka','Egilea','\n')) #csv fitxategian idatzi goiburua
        
        for galdera in galderak:
            noranzkoa = galdera[0]
            Zuzena = galdera[1][0]+"("+galdera[1][1]+")"
            Oker1 = galdera[2][0]+"("+galdera[2][1]+")"
            Oker2 = galdera[3][0]+"("+galdera[3][1]+")"
            url = galdera[1][4]
            out.write(f"Hiriburuak non?;Zein hiriburu dago {noranzkoa}rago?;{Zuzena};{Oker1};{Oker2};Wikipedia;{url};Gorka Urbizu Garmendia;\n") #csv fitxategian idatzi galderak




queryfile = "query.csv"
outfile = "galderak.csv"
n = 100000 #galdera kopurua [max ~= 6M galdera ezberdin (4 norazko * 1,3M (200 hiriren arteko konbinatoria) ]

queries = readQuery(queryfile)
galderak = generateGalderak(queries, n)
writeGalderak(galderak, outfile)