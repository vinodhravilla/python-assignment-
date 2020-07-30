riginal_Tuple = [(1,2,3) , [1,2] , ['a' , 'hit' , 'less']]

out = [x[0] for x in original_Tuple]

out1 = [i[1] for i in original_Tuple]

out2 = [j[-1] for j in original_Tuple]

new_List = out + out1 + out2

print(new_List)