#given a string how many can be produced from that target  string

def find_count_string(Str , target):
    target_map = {}
    Str_map = {}
    for i in target:
        if i in target_map:
            target_map[i]+=1
        else:
            target_map = 1
    for i in Str:
        if i in Str_map:
            Str_map[i]+=1
        else:
            Str_map[i] = 1

           
        
        