import pandas as pd
import matplotlib.pyplot as plt
import fitness

class Metric:
	def __init__(self, name, extract_from_exercise):
		self.name = name
		self.extract_from_exercise = extract_from_exercise

MAX_WEIGHT = Metric("max_weight", lambda ex: max([s.weight for s in ex.sets]))
VOLUME = Metric("volume_lbs", lambda ex: sum([s.weight * s.reps for s in ex.sets]))

def viz(dates, metrics, yname):
	assert len(metrics) == len(dates)

	dates, metrics = zip(*sorted(zip(dates, metrics)))

	as_date_time = []
	for date in dates:
		assert len(str(date)) == 8 # s/b YYYYMMDD
		y = str(date)[:4]
		m = str(date)[4:6]
		d = str(date)[6:]
		as_date_time.append(y + "-" + m + "-" + d)

	as_pd_date_times = pd.to_datetime(as_date_time)

	DF = pd.DataFrame()
	DF['value'] = metrics
	DF = DF.set_index(as_pd_date_times)
	plt.plot(DF)
	plt.ylabel(yname)
	plt.gcf().autofmt_xdate()
	plt.show()

def viz_exercise(name, metric):
	all_workouts = fitness.load_workouts()
	es = fitness.get_exercises(all_workouts, name)
	dates = [w.date for w in all_workouts if w.has_exercise(name)]
	values = [metric.extract_from_exercise(e) for e in es]
	viz(dates, values, metric.name)
