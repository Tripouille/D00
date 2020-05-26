from time import sleep, time


def ft_progress(li):
    for i in li:
        yield(i / len(li) * 100)


it = time()
listy = range(1000)
ret = 0
eta = 0.0
for elem in ft_progress(listy):
    et = (time() - it)
    if elem:
        eta = (et / elem * 100) - et
    bar = "=" * int(elem / 10) + ">"
    print("\rETA: {:5.2f}s [{:.2f}%][{:10}] {}/{} | elapsed time {:.2f}s"
          .format(eta, elem, bar, int(len(listy) * elem / 100),
                  len(listy), et), end='')
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
