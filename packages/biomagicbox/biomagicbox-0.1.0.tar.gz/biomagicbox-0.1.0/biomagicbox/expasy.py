import requests
import re,os,sqlite3
import threading

class ProtParam():
    def __init__(self,dbname,tablename):
        self.dbname=dbname
        self.tablename=tablename
        self.finish_num=0
        self.url='https://web.expasy.org/cgi-bin/protparam/protparam'
        self.headers={'Content-Type':'application/x-www-form-urlencoded'}
        self.create_db()
    def load_gene(self,filename):
        with open(filename,encoding='utf-8') as f:
            data=f.read().split('\n')

        header=data[0].split(',')
        exited_gene=self.view_db()
        gene_ls=[]
        for i in data[1:]:
            if i!='':
                temp=i.split(',')
                if temp[0] not in exited_gene:
                    gene_ls.append((temp[0],temp[1]))
        self.gene_ls=gene_ls


    def create_db(self):
        if not os.path.exists(self.dbname):
            conn = sqlite3.connect(self.dbname)
            conn.execute("CREATE TABLE "+self.tablename+"(GeneID TEXT,aa REAL, weight REAL, pI REAL, Instability REAL, Aliphatic REAL, GRAVY REAL, negatively REAL, positively REAL, Formula TEXT)")
            conn.close()

    def view_db(self):
        conn = sqlite3.connect(self.dbname)
        r=conn.execute("select GeneID from "+self.tablename)
        ls=[i[0] for i in r.fetchall()]
        return ls

    def save_db(self,s):
        conn=sqlite3.connect(self.dbname)
        conn.execute("INSERT INTO "+self.tablename+" VALUES ("+s+")")
        conn.commit()
        conn.close()


    def process_ls(self,geneid,ls):
        return "'"+geneid+"',"+ls[2]+","+ls[3]+","+ls[4]+","+ls[5]+","+ls[0]+","+ls[1]+","+ls[6]+","+ls[7]+",'"+ls[8]+"'"


    def get_expasy(self,geneid,seq,session):
        seq=seq.replace('*','').replace(' ','').replace('\n','').replace('\t','').replace('\r','')
        data={'sequence':seq}
        while True:
            try:
                r=session.post(self.url,headers=self.headers,data=data)
                break
            except:
                print('{} retry...'.format(geneid))
        ls=self.get_params(r.text)
        self.save_db(self.process_ls(geneid,ls))

    def get_params(self,s):
        pattern=re.compile('<B>Aliphatic index:</B> (.*)')
        p1=pattern.findall(s)[0]
        pattern=re.compile('<B>Grand average of hydropathicity \(GRAVY\):</B> (.*)')
        p2=pattern.findall(s)[0]
        pattern=re.compile('<B>Number of amino acids:</B> (.*)')
        p3=pattern.findall(s)[0]
        pattern=re.compile('<B>Molecular weight:</B> (.*)')
        p4=pattern.findall(s)[0]
        pattern=re.compile('<B>Theoretical pI:</B> (.*)')
        p5=pattern.findall(s)[0]
        pattern=re.compile(' is computed to be (.*)')  #  Instability index
        p6=pattern.findall(s)[0]
        pattern=re.compile('<B>Total number of negatively charged residues \(Asp \+ Glu\):</B> (.*)')
        p7=pattern.findall(s)[0]
        pattern=re.compile('<B>Total number of positively charged residues \(Arg \+ Lys\):</B> (.*)')
        p8=pattern.findall(s)[0]
        pattern=re.compile('<B>Formula:</B> (.*)')
        p9=pattern.findall(s)[0].replace('<SUB>','').replace('</SUB>','')
        return [p1,p2,p3,p4,p5,p6,p7,p8,p9]

    def run_process(self,startpoint,endpoint):
        session = requests.Session()
        for i in self.gene_ls[startpoint:endpoint]:
            self.get_expasy(i[0],i[1],session)
        self.finish_num+=1
        if self.finish_num==self.num_process:
            print('Done!')

    def run(self,num_process):
        self.num_process=num_process
        numtotal=len(self.gene_ls)
        for i in range(self.num_process):
            startpoint=i*int(numtotal/self.num_process)
            if i==self.num_process-1:
                endpoint=numtotal
            else:
                endpoint=(i+1)*int(numtotal/self.num_process)
            threading.Thread(target=self.run_process,args=(startpoint,endpoint)).start()


def write_table(self,filename):
    conn = sqlite3.connect(self.dbname)
    r=conn.execute("select * from "+self.tablename)
    s='Gene ID,Num of aa,Molecular weight,Theoretical pI,Instability index,Aliphatic index,GRAVY,Number of negatively charged residues,Number of positively charged residues,Formula\n'
    for i in r.fetchall():
        for j in i:
            try:
                s+=j+','
            except:
                s+=str(j)+','
        s=s[:-1]+'\n'
    with open(filename,'w+') as f:
        f.write(s)



if __name__=='__main__':

    c=ProtParam('test.db','expasy')
    c.load_gene('test.csv')
    c.run(17)
