from bundle_error import Error

def init_counters():
   col_ctr = 1
   return col_ctr

def inc_counters(col_ctr):
   col_ctr+=2
   return col_ctr



try:
   order_handle = open("order.txt", 'r')

except OSError as error:
   print("Can't open order file: ", error)

else:
  list_img_format = ['IMG', 'img', 'Img']
  list_flac_format = ['FLAC', 'flac', 'Flac']
  list_vid_format = ['VID', 'vid', 'Vid']

  hndle = order_handle.__iter__()
  line = [line for line in hndle]
  num_line = len(line) 
  line_ctr = 0 

  while line_ctr < num_line - 2:    
    data = line[line_ctr].split(" ") 
    print("data: ", data)
    col_ctr = init_counters()

    try:
     if list_img_format.count(data[col_ctr]) > 0:
        if int(data[col_ctr -1]) == 10:
            bundle_A = (int(data[col_ctr -1]) // 10) * 800
            bundle_B = (int(data[col_ctr -1]) // 5) * 450
            cost = "IMG: \n Cost_A=${0:d} \n Cost_B=${1:d}".format(bundle_A, bundle_B)
            print(cost) 
        elif int(data[col_ctr -1]) == 15:
            bundle_A = (int(data[col_ctr -1]) // 10) * 800
            bundle_B = ((int(data[col_ctr -1]) % 10) // 5) * 450
            bundle_cost = bundle_A + bundle_B
            cost = "IMG: \n Total Cost=${0:d} \n Breakdown: \n \t bundle_A=${1:d} \n \t bundle_B=${2:d}".format(bundle_cost, bundle_A, bundle_B)
            print(cost)
        elif int(data[col_ctr -1]) == 5:
            bundle_cost = (int(data[col_ctr -1]) // 5) * 450
            cost = "IMG: \n Cost=${0:d}".format(bundle_cost)
            print(cost)
        else:
            img_coverage = [10, 15, 5]
            if int(data[col_ctr -1]) not in img_coverage:
               raise Error("Bundle is out of my computation range")
        col_ctr = inc_counters(col_ctr)
    except:
        pass
        
             
    try:
     if list_flac_format.count(data[col_ctr]) > 0:
        if int(data[col_ctr -1]) in [3, 9, 15]:
            bundle_cost =  (int(data[col_ctr -1]) // 3) * 427.50
            cost = "FLAC: \n Cost=${0:.2f}".format(bundle_cost)
            print(cost)
        elif int(data[col_ctr -1]) in [6, 12, 24]:
            bundle_cost =  (int(data[col_ctr -1]) // 6) * 810
            cost = "FLAC: \n Cost=${0:d}".format(bundle_cost)
            print(cost)
        elif int(data[col_ctr -1]) == 18:
            bundle_cost = 427.50 + 810 + 1147.50   
            cost = "FLAC: \n Total Cost=${0:.2f} \n Breakdown: \n \t bundle_A=1x427.50=$427.50 \n \t bundle_B=1x810=$810 \n \t bundle_C=1x1147.50=$1147.50".format(bundle_cost)	
            print(cost)
        else:
            flac_coverage = [3, 9, 15, 6, 12, 24, 18]
            if int(data[col_ctr -1]) not in flac_coverage:
               raise Error("Bundle is out of my computation range")
        col_ctr = inc_counters(col_ctr)
    except:
        pass 

 
    try:
     if list_vid_format.count('VID') > 0:
        if int(data[col_ctr -1]) in [3, 6, 12]:
            bundle_cost =  (int(data[col_ctr -1]) // 3) * 570
            cost = "VID: \n Cost=${0:d}".format(bundle_cost)
            print(cost)		 
        elif int(data[col_ctr -1]) in [5, 10, 15, 20]:
            bundle_cost =  (int(data[col_ctr -1]) // 5) * 900
            cost = "VID: \n Cost=${0:d}".format(bundle_cost)
            print(cost)
        elif int(data[col_ctr -1]) in [9, 18, 27]:
            bundle_cost =  (int(data[col_ctr -1]) // 9) * 1530
            cost = "VID: \n Cost=${0:d}".format(bundle_cost)
            print(cost)
        elif int(data[col_ctr -1]) == 17:
            bundle_cost = (570 + 900 + 1530)   
            cost = "VID: \n Total Cost=${0:d} \n Breakdown: \n \t bundle_A=1x570=$570 \n \t bundle_B=1x900=$900 \n \t bundle_C=1x1530".format(bundle_cost)	
            print(cost)
        elif int(data[col_ctr -1]) == 13:
            bundle_cost = (2 * 900) + (1 * 570)
            cost = "VID: \n Total Cost=${0:d} \n Breakdown: \n \t bundle_A=2x900=$1800 \n \t bundle_B=1x570=$570".format(bundle_cost)
            print(cost)  
        else:
            vid_coverage = [3, 6, 12, 5, 10, 15, 20, 9, 18, 27, 17, 13]
            if int(data[col_ctr -1]) not in vid_coverage:
               raise Error("Bundle is out of my computation range")
        col_ctr = inc_counters(col_ctr)   
    except:
        pass

    line_ctr+=1  

  order_handle.close()  


