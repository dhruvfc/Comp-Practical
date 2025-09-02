import csv
def create(n):
    with open('transaction_log.csv','a',newline='') as f:
        writer=csv.writer(f)
        for i in range(n):
            cid=int(input('enter customer id:'))
            cname=input('enter customer name:')
            bal=float(input('enter balance:'))
            L=[cid,cname,bal]
            writer.writerow(L)
        return 'records added succesfully'

def delete(r):
    with open('transaction_log.csv','r+',newline='') as f:
        writer=csv.writer(f)
        reader=csv.reader(f)
        Updated=[]
        for record in reader:
            if record[1].lower()==r.lower():
                print('record deleted successfully')
                continue
            else:
                Updated.append(record)
        f.seek(0)
        f.truncate()
        writer.writerows(Updated)
        print(Updated)

def update(x,y):
     with open('transaction_log.csv','r+',newline='') as f:
        writer=csv.writer(f)
        reader=csv.reader(f)
        Updated=[]
        found=False
        for record in reader:
            if record[1].lower()==x.lower():
                bal=float(record[2])
                bal+=y
                record.append(str(bal))
                found=True
            Updated.append(record)
        if found==True:
            print('updated succesfully')
        else:
            print('no record found')
        f.seek(0)
        f.truncate()
        writer.writerows(Updated)
        print(Updated)
ans='yes'
while ans.lower() in ['yes','y']:
    print('what would you like to do?\n1.add records\n2.deleterecord\n3.update record')
    ch=int(input('enter a choice(1/2/3):'))
    if ch==1:
        n=int(input('enter number of records:'))
        print(create(n))
    elif ch==2:
        name=input('enter customer name whose record to be deleted:')
        delete(name)
    elif ch==3:
        name=input('enter customer name whose record to be updated:')
        bal=float(input('enter amount to be incremented:'))
        update(name,bal)
    else:
        print('invalid choice')
    ans=input('do you want to continue(yes/y):')
