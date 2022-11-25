import json
import os
import re

class Set:
    def __init__(self, weight, reps):
        self.weight = weight
        self.reps = reps
        
    def to_json(self):
        return {"weight" : self.weight, "reps" : self.reps}
    
    @classmethod
    def from_json(cls, obj):
        return Set(obj['weight'], obj['reps'])

    def __repr__(self):
        return json.dumps(self.to_json(), indent=2)

class Exercise:
    def __init__(self, sets, rests, name):
        assert len(sets) == len(rests) + 1
        self.sets = sets
        self.rests = rests
        self.name = name
    
    def to_json(self):
        return {"sets" : [s.to_json() for s in self.sets], "rests" : self.rests, "name" : self.name}
    
    @classmethod
    def from_json(cls, obj):
        return Exercise([Set.from_json(d) for d in obj['sets']], [r for r in obj['rests']], obj['name'])

    def __repr__(self):
        return json.dumps(self.to_json(), indent=2)
        
class Workout:
    def __init__(self, date, exercises):
        self.date = date
        self.exercises = exercises
        
    def to_json(self):
        return {self.date : [e.to_json() for e in self.exercises]}
    
    @classmethod
    def from_json(cls, obj):
        dates = list(obj.keys())
        assert len(dates) == 1
        date = dates[0]
        return Workout(date, [Exercise.from_json(d) for d in obj[date]])

    def get_exercise(self, name):
        exercises_matching_name = [e for e in self.exercises if e.name == name]
        assert len(exercises_matching_name) == 1
        return exercises_matching_name[0]

    def has_exercise(self, name):
        exercises_matching_name = [e for e in self.exercises if e.name == name]
        return len(exercises_matching_name) > 0

    def __repr__(self):
        return json.dumps(self.to_json(), indent=2)

def add_workout(workout, overwrite=False):
    d = workout.to_json()
    dest = str(workout.date)
    fname = f"./workouts/{dest}.json"
    if (not overwrite):
        assert (not os.path.isfile(fname))
    
    with open(fname, 'w') as f:
        json.dump(d, f, indent=4)

def workout_from_path(path):
    with open(path, 'r') as f:
        return json.load(f)

def load_workouts():
    paths = [path for path in os.listdir("./workouts") if re.match("\d{8}\.json", path)]
    ds = [workout_from_path(f"./workouts/{path}") for path in paths]
    workouts = [Workout.from_json(d) for d in ds]
    return workouts

def get_exercises(workouts, name):
    return [w.get_exercise(name) for w in workouts if w.has_exercise(name)]


