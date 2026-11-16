from enum import Enum

class Difficulty(Enum):
	Heaven = 1
	Easy = 2
	Normal = 3
	Hard = 4
	Nightmare = 5

diff_configs = {
	1 : {
			"planet" : {
				"planet_health" : 150
			},
			"asteroids" : {

			},
			"missiles" : {
				"speed" : 3,
				"radius" : 1.5,
				"cooldown" : 60
			}
		},

	2 : {
			"planet" : {
				"planet_health" : 125
			},
			"asteroids" : {

			},
			"missiles" : {
				"speed" : 2.4,
				"radius" : 0.9,
				"cooldown" : 100
			}
		},

	3 : {
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
		},

	2 : {
			"planet" : {
				"planet_health" : 50
			},
			"asteroids" : {

			},
			"missiles" : {
				"speed" : 1.6,
				"radius" : 0.4,
				"cooldown" : 130
			}
		},

	5 : {
			"planet" : {
				"planet_health" : 30
			},
			"asteroids" : {

			},
			"missiles" : {
				"speed" : 1.2,
				"radius" : 0.3,
				"cooldown" : 150
			}
		}

}

	