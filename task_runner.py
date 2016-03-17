from tasks import add


for i in range(10000):
    add.delay(i^2, i)
