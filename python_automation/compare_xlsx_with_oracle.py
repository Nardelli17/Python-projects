import pandas as pd
import cx_Oracle

def MainAutomation():
    try:
        #READ XLSX
        df = pd.read_excel('mock.xlsx', index_col=0)
        l1 = list(df.index.values)

        #PRINT XLSX VALUES
        print("Xlsx list is: ", l1)
        
        conn = cx_Oracle.connect(user=user, password=pswd, dsn=dsn,encoding="UTF-8")
        sqlQuery = """select * from table"""
        cursor = conn.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
         
        #Declare a list to obtain oracle data
        l2 = []   
        
        for reg in records :
            vData = str(reg[0])
            l2.append(vData)
        
        #convert string list to int
        res = [eval(i) for i in l2]
        print("Oracle list is: ", res)
        
        #convert list to set
        a = set(l1)
        b = set(res)
        
        #shows difference
        print("Missing registers: ", a.difference(b))
        
        #close oracle connection
        conn.close    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("Begin")
    try:
        MainAutomation()
        print("End without error")
    except:
        print("End with error")