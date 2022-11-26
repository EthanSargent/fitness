`fitness` is a small class hierarchy I'm using to track my weightlifting performance. There are three classes in the hierarchy: `Set`, `Exercise`, and `Workout`.

A `Set` is a weight and a number of reps.
````
s = Set(385, 4)
````

An `Exercise` is a list of `N` sets, `N-1` rest periods, and a name.
````
deadlift = Exercise([Set(385, 4), Set(385, 4), Set(385, 3)], [5, 5], "deadlift")
````

A `Workout` is a date and a list of exercises.
````
w = Workout(20221124, [squat, deadlift])
````

You can save a workout to a JSON file for that date in `workouts/` with `add_workout`.
````
add_workout(w) # writes to workouts/20221124.json
````

Once you have saved a few workouts, you can visualize your progress for a specific exercise and an arbitrary metric. Two metrics are coded up for you already, `VOLUME` and `MAX_WEIGHT`.

![](https://github.com/EthanSargent/fitness/blob/main/examples/deadlift_max_weight.png "")

You can also define your own metrics. A metric operates on an exercise and returns a number.

![](https://github.com/EthanSargent/fitness/blob/main/examples/deadlift_max_per_set_volume.png "")

