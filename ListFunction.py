l=["kowshik",3,4,5,"sai",9]
l1=[3,5,433,5,6]

print(len(l)) # length of the list
print(max(l1)) # max number in the list
print(min(l1)) # min number in the list
print(sum(l1)) # add the list
k=sorted(l1)
print(k)# sorted order
print(list("avreikit"))# convert into a list

l1.append(10) #add at the end
print(l1)

l1.extend(l) # we can add to list join two list at the end
print(l1)

l1.insert(3,20)
print(l1) # we can add elemets in thr prefered indexes

l1.remove(3)
print(l1) # removes the first occurence of this item 

l1.append(3)
print(l1)

l1.remove(3)
print(l1)

l1.pop(2)
print(l1)

l1.append(2)
print(l1)

l1.insert(4,2)
print(l1)

l1.pop(2) # remove the prefred index from the list
print(l1)

print(l1.count(10)) # counts the oocurence of the element

l1.reverse()
print(l1)

l1.copy()
print(l1)