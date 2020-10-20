P1_time = [["09:00","10:30"],["10:30","12:00"],["14:00","15:00"],["16:00","17:30"]]
Bounded1 = ["08:00","20:00"]

P2_time = [["10:00","11:30"],["12:00","13:00"],["14:00","15:30"],["16:30","18:00"]]
Bounded2 = ["08:00","19:00"]


def avail_interval(time_list):
	interval = []
	for i in range (0,len(time_list)-1):
		interval_list = []
		if time_list[i][1] != time_list[i+1][0]:
			interval_list.append(time_list[i][1])
			interval_list.append(time_list[i+1][0])
			interval.append(interval_list)
	return interval



def add_bounder(ptime,intervals,bound):
	mini_interval = []
	if ptime[0][0] != bound[0]:
		mini_interval.append(bound[0])
		mini_interval.append(ptime[0][0])
		intervals.insert(0,mini_interval)
	mini_interval = []
	if ptime[-1][1] != bound[1]:
		mini_interval.append(ptime[-1][1])
		mini_interval.append(bound[1])
		intervals.append(mini_interval)
	return intervals



def compare_interval(intervals1,intervals2):
	inter = []
	for i in range(0,len(intervals1)):
		t1h1 = int(intervals1[i][0][0:2])
		t1m1 = int(intervals1[i][0][3:5])

		t1h2 = int(intervals1[i][1][0:2])
		t1m2 = int(intervals1[i][1][3:5])
		for j in range(0,len(intervals2)):
			temp_inter = []
			t2h1 = int(intervals2[j][0][0:2])
			t2m1 = int(intervals2[j][0][3:5])

			t2h2 = int(intervals2[j][1][0:2])
			t2m2 = int(intervals2[j][1][3:5])

			if (t1h1*60+t1m1) <= (t2h1*60+t2m1) and (t1h2*60+t1m2) >= (t2h2*60+t2m2):
				inter.append(intervals2[j])

			elif (t1h1*60+t1m1) >= (t2h1*60+t2m1) and (t1h2*60+t1m2) <= (t2h2*60+t2m2):
				inter.append(intervals1[i]) 

			elif (t1h1*60+t1m1) <= (t2h1*60+t2m1) and (t1h2*60+t1m2) > (t2h1*60+t2m2) and (t1h2*60+t1m2) <= (t2h2*60+t1m2):
				temp_inter.append(intervals2[j][0])
				temp_inter.append(intervals1[i][1])
				inter.append(temp_inter)
			elif (t1h1*60+t1m1) >= (t2h1*60+t2m1) and (t1h1*60+t1m1) < (t2h2*60+t2m2) and (t1h2*60+t1m2) >= (t2h2*60+t2m2):
				temp_inter.append(intervals1[i][0])
				temp_inter.append(intervals2[j][1])
				inter.append(temp_inter)
	return inter





A1 = avail_interval(P1_time)
A2 = avail_interval(P2_time)

arr = compare_interval(add_bounder(P1_time,A1,Bounded1),add_bounder(P2_time,A2,Bounded2))
print(arr)