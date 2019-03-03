# hashcode-2019 slideshow problem
Our team got into top 10% of the ranking with ~75% of maximum aciheved score. This is my own implementation 
for fun.

The solution was to join 
all pairs of vertical pics into horizontal ones right away and sort all the pics by the number of tags 
descending. Then the previous slide is taken, and the next N pics in the sorted list are tested on the 
score. Then pop the first pic/slide from the list, remember the selected slide as new previous, and repeat 
until the list is empty.

-- slideshow.py: the implementation, doesn't run too fast.
