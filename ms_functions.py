def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def my_center_sweep_range(center, sweep, step):
	if sweep == 0:
		yield center
	else:
		num = round(sweep/2.0/step, 0)
		start = center - num*step
		end = center + num*step
		if (center - sweep/2.0) < start :
			yield (center - sweep/2.0)
		while start <= end:
			yield start
			start += step
		if (center + sweep/2.0) > end :
			yield (center + sweep/2.0)

def userConfirmation(msg):
    userReady = 'n'
    while userReady != 'y':
        userReady = raw_input(msg + '. Type y to continue. ')
