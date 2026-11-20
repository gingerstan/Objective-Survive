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
				"planet_health" : 300
			},
			"threats" : {
				"asteroid_spawn_rate_slope" : -0.004,
				"asteroid_spawn_rate_mod" : 200 
			},
			"missiles" : {
				"speed" : 10,
				"radius" : 4,
				"cooldown" : 20
			}
		},

	2 : {
			"planet" : {
				"planet_health" : 200
			},
			"threats" : {
				"asteroid_spawn_rate_slope" : -0.005,
				"asteroid_spawn_rate_mod" : 190 
			},
			"missiles" : {
				"speed" : 5,
				"radius" : 1.5,
				"cooldown" : 60
			}
		},

	3 : {
			"planet" : {
				"planet_health" : 150
			},
			"threats" : {
				"asteroid_spawn_rate_slope" : -0.006,
				"asteroid_spawn_rate_mod" : 180
			},
			"missiles" : {
				"speed" : 3,
				"radius" : 1,
				"cooldown" : 90
			}
		},

	4 : {
			"planet" : {
				"planet_health" : 50
			},
			"threats" : {
				"asteroid_spawn_rate_slope" : -0.008,
				"asteroid_spawn_rate_mod" : 180
			},
			"missiles" : {
				"speed" : 2.2,
				"radius" : 0.7,
				"cooldown" : 110
			}
		},

	5 : {
			"planet" : {
				"planet_health" : 30
			},
			"threats" : {
				"asteroid_spawn_rate_slope" : -0.01,
				"asteroid_spawn_rate_mod" : 170 
			},
			"missiles" : {
				"speed" : 1.8,
				"radius" : 0.4,
				"cooldown" : 120
			}
		}

}

	