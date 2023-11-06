'''

inv={
    'gold': 500,
    'pouch': ["flint","twine","gemstone"],
    'backpack': ["xplophone","dagger","bedroll","bread loaf"]
}
print(inv)
print("==========================================================================")

#inserting more elements
inv["pocket"]="seashell","strange berry","lint"
inv["gold"]=500,30,25,18,37
print("After inserting more elements:\n",inv)

#delecting element from inv dictionary
#inv.pop()


'''


dic={'Alice':'April 1','Bob':'December 12','Carol':'March 4'}
print(dic)
while True:
    print("\nEnter your name: ")
    name=input()
    if name=='':
        break

    if name in dic:
        print(dic[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information of ' + name)
        print('What is their birthday?')
        dicinput=input()
        dic[name]=dicinput
        print('Birthday database updated.')


# 'Alice' in dic.keys()