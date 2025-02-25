#created 11/23/24, by Antony Bagreyser
'''
log
11/23/24 created int_limited, int_unlimited, int array_unlimited, str_limited, str_unlimited, float_unlimited, float_array_unlimited, debugger
12/7/24 added int_minRange_infPositive_unlimited, int_maxRange_infNegative_unlimited
1/28/25 added float_min_range_infpositive_unlimited, and float_maxRange_infNegative_unlimited'''
def int_limited(question, input_range, esc_stroke): #used for limited amount of choices and the choices are int's
    while True:
        try:
            user_input = input(question)
            user_input = int(user_input)
        except:
            if esc_stroke!="" and esc_stroke == user_input: return user_input
            else: print("Invalid input.")
        else:
            if user_input in input_range: return user_input
            else: print("Invalid input.")

def int_unlimted(question, esc_stroke): #used to get int's than can be anything EX: such as amount of something
    while True:
        try:
            user_input = input(question)
            user_input = int(user_input)
            return user_input
        except:
            if esc_stroke!="" and esc_stroke == user_input: return user_input
            else: print("Invalid input.")

def int_minRange_infPositive_unlimited(question, esc_stroke, min_range): #used for getting an int's in range of min_range(inclusive) to positive infinity
    while True:
        try:
            user_input = input(question)
            user_input = int(user_input)
            if user_input>=min_range: return user_input
            print("Invalid input.")
        except:
            if esc_stroke != "" and esc_stroke == user_input: return user_input
            else: print("Invalid input.")

def int_maxRange_infNegative_unlimited(question, esc_stroke, max_range): # used for getting ints in range of max_range(inclusive) to negative infinity 
    while True:
        try:
            user_input = input(question)
            user_input = int(user_input)
            if user_input<=max_range: return user_input
            print("Invalid input.")
        except:
            if esc_stroke != "" and esc_stroke == user_input: return user_input
            print("Invalid input.")
            
def int_array_unlimited(question, esc_stroke, finished_stroke): # used for getting a list of int's
    return_array = []
    while True:
        try:
            user_input = input(question)
            return_array.append(int(user_input))
        except:
            if finished_stroke == user_input: return return_array
            elif esc_stroke !="" and esc_stroke == user_input: return user_input
            else: print("Invalid input.")

def str_limited(question, input_range, esc_stroke): # used for limited answer choice when its a word or letter
    while True:
        user_input = input(question)
        if user_input in input_range: return user_input
        elif esc_stroke !="" and esc_stroke == user_input: return user_input
        else : print("Invalid input.")

def str_unlimited(question, esc_stroke): #used for getting strings that can be anything such as names
    while True:
        user_input = input(question)
        if esc_stroke!="" and esc_stroke == user_input and int_limited("is this your answer or do you want to quit, 1 = quit, 2 = answer",(1,2),"")==1: return(False)
        else: return user_input

def float_unlimited(question, esc_stroke): #to get things with a decimal value
    while True:
        try:
            user_input = input(question)
            user_input = float(user_input)
            return user_input
        except:
            if esc_stroke != "" and esc_stroke == user_input: return user_input
            else: print("Invalid input.")
def float_minRange_infPositive_unlimited(question, esc_stroke, min_range): #used for getting an int's in range of min_range(inclusive) to positive infinity
    while True:
        try:
            user_input = input(question)
            user_input = float(user_input)
            if user_input>=min_range: return user_input
            print("Invalid input.")
        except:
            if esc_stroke != "" and esc_stroke == user_input: return user_input
            else: print("Invalid input.")

def float_maxRange_infNegative_unlimited(question, esc_stroke, max_range): # used for getting ints in range of max_range(inclusive) to negative infinity 
    while True:
        try:
            user_input = input(question)
            user_input = float(user_input)
            if user_input<=max_range: return user_input
            print("Invalid input.")
        except:
            if esc_stroke != "" and esc_stroke == user_input: return user_input
            print("Invalid input.")

def float_array_unlimited(question, esc_stroke, finished_stroke):
    return_array = []
    while True:
        try:
            user_input = input(question)
            return_array.append(float(user_input))
        except:
            if finished_stroke == user_input: return return_array
            elif esc_stroke !="" and esc_stroke == user_input: return user_input
            else: print("Invalid input.")

def debugger():#used to debug all functions here not for user use
    def function_parameter_helper(question, input_range, esc_stroke, finished_stroke):
        return_parameter = []
        if question:
             return_parameter.append(input("please input question: "))
        if input_range:
            
            range_type_debug = int(input("Please select what type of range you will be using 1 = manual array/tuple, 2 = 2 num range, 3 = 3 num range: "))
            if range_type_debug ==1:
                amount = int(input("please select how many numbers/words will be in manual: "))
                range_type_debug = []#recycling a variable
                int_or_not = int(input("are you putting in ints? 1 = yes 2 = no"))
                if int_or_not == 1:
                    for i in range(amount):range_type_debug.append(int(input(f"{i+1} : ")))
                if int_or_not == 2:
                    for i in range(amount):range_type_debug.append(input(f"{i+1} : "))
            
            if range_type_debug ==2: 
                min_num = int(input("enter min number(inclusive): "))
                max_num = int(input("enter max number(exclusive): "))
                range_type_debug = range(min_num, max_num)
            
            if range_type_debug ==3:
                min_num = int(input("enter min number(inclusive): "))
                max_num = int(input("enter max number(exclusive): "))
                mod_num = int(input("enter skiping number: "))
                range_type_debug = range(min_num, max_num, mod_num)
            return_parameter.append(range_type_debug)
        
        if esc_stroke:
            return_parameter.append(input("enter esc_stroke: "))
        if finished_stroke:
            return_parameter.append(input("enter finished_stroke: "))
        return return_parameter
       
    functions = [int_limited,int_unlimted,int_array_unlimited,str_limited,str_unlimited,float_unlimited,float_array_unlimited]
    string_selection = ""
    for i in range(len(functions)):
        string_selection += f"{i} = {functions[i].__name__}, "
    dev_input = int(input(string_selection))
    if dev_input == 0:
        parameters = (function_parameter_helper(True,True,True,False))#int_limited
        functions[dev_input](parameters[0],parameters[1],parameters[2])
    if dev_input == 1:
        parameters = (function_parameter_helper(True,False,True,False))#int_unlimited
        functions[dev_input](parameters[0],parameters[1])
    if dev_input == 2:
        parameters = (function_parameter_helper(True,False,True,True))#int_array_unlimited
        functions[dev_input](parameters[0],parameters[1],parameters[2])
    if dev_input == 3:
        parameters = (function_parameter_helper(True,True,True,False))#str_limited
        functions[dev_input](parameters[0],parameters[1],parameters[2])
    if dev_input == 4:
        parameters = (function_parameter_helper(True,False,True,False))#str_unlimited
        functions[dev_input](parameters[0],parameters[1],parameters[2])
    if dev_input == 5:
        parameters = (function_parameter_helper(True,False,True,False))#float_unlimited
        functions[dev_input](parameters[0],parameters[1],parameters[2])
    if dev_input == 6:
        parameters = (function_parameter_helper(True,False,True,True))#float_array_unlimited
        functions[dev_input](parameters[0],parameters[1],parameters[2])

            
