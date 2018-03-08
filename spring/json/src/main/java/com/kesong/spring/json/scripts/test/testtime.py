from time import ctime, sleep, time, localtime, strftime

def music():
    for i in range(2):
        print "I was listening to music. %s" %ctime()
        sleep(1)

def move():
    for i in range(2):
        print "I was at the movies! %s" %ctime()
        sleep(5)

print __name__
for e in localtime():
    print e
print strftime("%Y-%m-%d", localtime())
if __name__ == '__main__':
    start_time = time()
    music()
    move()
    print "all over %s" % ctime()
    end_time = time()
    total_time = end_time - start_time
    print total_time
