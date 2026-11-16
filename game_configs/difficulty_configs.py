from enum import Enum

class Difficulty(Enum):
	Heaven = 1
	Easy = 2
	Normal = 3
	Hard = 4
	Nightmare = 5


medium = {
	"planet" : {
		"planet_health" : 100
	},
	"asteroids" : {

	},
	"missiles" : {
		"speed" : 1.8,
		"radius" : 0.5,
		"cooldown" : 120
	}
	
}