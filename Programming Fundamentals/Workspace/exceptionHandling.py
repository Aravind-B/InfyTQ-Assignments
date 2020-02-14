#PF-Exer-30

def find_average(mark_list):
    total=0
    try:
        for i in range(0, len(mark_list)):
            total+=mark_list[i]
        marks_avg=total/len(mark_list)
        return marks_avg
    except IndexError:
        print("Index Error occured")
    except TypeError:
        print("Type Error occured")
    except NameError:
        print("Name error occured")


#m_list=[1,2,3,4]

m_list=["1",2,3,4]
try:
    mark1="A"
    mark1=int("A")
    m_list=[mark1,2,3,4]
    print("Average marks:", find_average(m_list))
except ValueError:
    print("Value error occured")
except:
    print("Some error!")