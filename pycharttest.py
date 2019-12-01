#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from pychart import chart

chart1 = chart(2, 2, "zhexian")
chart1.figure(10, 10, 100)

chart1.bar([1,2,3,4,5], [1,4,9,16, 25], 0.5)
chart1.xticks([0, 1, 2, 3, 4, 5, 6])

chart1.pie([1,2,3,4,5], ["a", "b", "c", "d", "e"])

chart1.plot("test3", [1,2,3,4,5], [1,4,9,16, 25], "test3 x", "test3 y")
chart1.xticks([0, 1, 2, 3, 4, 5, 6])
chart1.legend2()

chart1.plot("test4", [1,2,3,4,5], [1,4,9,16, 25], "test4 x", "test4 y")
chart1.scatter(3, 9)
chart1.xticks([0, 1, 2, 3, 4, 5, 6])
chart1.legend("best")
chart1.annotate("middle",(1, 15), (3,9))
chart1.grid()

chart1.text(2, 18, "must be english")


chart1.save("chart1.jpg")
chart1.save("chart1.png")
chart1.save("chart1.pdf")

chart1.show()

