import sqlite3
import rospy
from std_msgs.msg import String




    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "pass1"
    database = "iReCHeCk"
)

counter = 0
def database():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('database', anonymous=True)

    # Initialize publishers/subscribers.
    pub = rospy.Publisher('chatter', String, queue_size=10)






    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():

        # read from database.
        # ...

        #connection = sqlite3.connect('/home/chili/Documents/iReCHeCk/Database/iReCHeCk/iReCheCk.db')
        cursor = connection.cursor()
        dynamico_table = """CREATE TABLE IF NOT EXISTS dynamico ( 
        id int NOT NULL AUTO_INCREMENT,
        fname TEXT,
        lname TEXT,
        gender TEXT, 
        age int NOT NULL,
        left_right-handed TEXT,
        country TEXT,
        city TEXT,
        game TEXT,
        level int NOT NULL,
        result TEXT);"""

        if counter%2 == 0
            sql_command = """INSERT INTO dynamico_table (fname, lname, gender, age,left_right-handed, country, city, game, level ,result) VALUES ("Dorsa", "Safaei", "f", 29, "r","iran", "tehran", "worm", 2, "w");"""
            rospy.sleep(10.)
        else
            sql_command = """INSERT INTO dynamico_table (fname, lname, gender, age,left_right-handed, country, city, game, level ,result) VALUES ("Dorsa", "Safaei", "f", 29, "r","iran", "tehran", "worm", 2, "f");"""
            rospy.sleep(10.)


        #sql_command = """select * from dynamico;"""
        #cursor.execute(sql_command)




        
        print("Fetching single row")
        #record = select *from dynamico ORDER BY id DESC LIMIT 1
        record = SELECT * FROM dynamico WHERE id=(SELECT MAX(id) FROM dynamico)
        #record = cursor.fetchone()
        print(record)
   
        
            row = cursor.fetchone()
            sfname = row[1]
            slname = row[2]
            sgender = row[3]
            sbirth_date = row[4]
            sleft_right_handed = row[4]
            sgame = row[6]
            slevel = row[7]
            sresult = row[8]
            
            
            message = '{} {} {} {} {} {} {} {} {} {} {}'.format(sfname, slname, sgender, sbirth_date, sleft_right_handed, scountry, scity, sgame, slevel, sresult)
            #message = "hello world %s" % rospy.get_time()

            rospy.loginfo(message)
            pub.publish(message)
            counter = counter + 1
            rospy.sleep(10.) # sleep for 10 seconds

        rate.sleep()

       
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if (connection):
            connection.close()
            print("The Sqlite connection is closed")

         


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    database()