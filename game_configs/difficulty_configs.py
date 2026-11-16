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
			"threats" : {
				"asteroid_spawn_rate_slope" : -0.002,
				"asteroid_spawn_rate_mod" : 200 
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
			"threats" : {
				"asteroid_spawn_rate_slope" : -0.002,
				"asteroid_spawn_rate_mod" : 190 
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
			"threats" : {
				"asteroid_spawn_rate_slope" : -0.003,
				"asteroid_spawn_rate_mod" : 180
			},
			"missiles" : {
				"speed" : 1.8,
				"radius" : 0.5,
				"cooldown" : 120
			}
		},

	4 : {
			"planet" : {
				"planet_health" : 50
			},
			"threats" : {
				"asteroid_spawn_rate_slope" : -0.004,
				"asteroid_spawn_rate_mod" : 180
			},
			"missiles" : {
				"speed" : 1.6,
				"radius" : 0.4,
				"cooldown" : 130
			}
		},

	5 : {
			"planet" : {
				"planet_health" : 10
			},
			"threats" : {
				"asteroid_spawn_rate_slope" : -0.0045,
				"asteroid_spawn_rate_mod" : 170 
			},
			"missiles" : {
				"speed" : 1.2,
				"radius" : 0.3,
				"cooldown" : 150
			}
		}

}

	