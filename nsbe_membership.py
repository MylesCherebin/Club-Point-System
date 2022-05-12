import sqlite3
con = sqlite3.connect('C:/Users/myles/Desktop/NSBE/membership.db')
cur = con.cursor()


event_type = {"pic": "5","social": "5", "gbody":"10", "corporate":"15","community":"20"}

if __name__ == "__main__":

    # determine points based on type of event
    name = ''
    print("Event type:")
    type = input()
    points = event_type[type]


    while name != "done":
        print("Enter your first name")
        name = input()

        if name == "done":
            pass
            con.close()
        else:
            print("Enter your NetId (all lowercase, ex: abc123)")
            netid = input()

            cur.execute("SELECT Points FROM Members where NetId = '%s' " % (netid))
            if cur.fetchone():
                cur.execute('''UPDATE Members SET Points=Points+'%s' WHERE NetId = '%s' ''' % (points,netid))
            else:
                print("member added")
                cur.execute("INSERT INTO Members (Name,NetId,Points) VALUES (?, ?, ?)",(name,netid,points))

            con.commit()
            print("Thanks for attending! \n \n")
