def login(fname):
    import json
    import sqlite3
    conn=sqlite3.connect('database.sqlite')
    cur=conn.cursor()
    data=open(fname).read()
    info=json.loads(data)
    for entry in info:
        email=entry["email"]
        pswd=entry["pswd"]
        cur.execute('''Select Password from USER where email=?''',(email,))
        ps=cur.fetchone()

        if ps[0]==pswd:
            print("Authorised")
        else:
            print("Invalid Password")

fname=input()
login(fname)
