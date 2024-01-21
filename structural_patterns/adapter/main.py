from structural_patterns.adapter.balloon import Balloon
from structural_patterns.adapter.balloon_adapter import BalloonAdapter

balloon = Balloon(1, 1, 1)
adapter = BalloonAdapter(balloon)

print(adapter.calculate_dp(0, 1))
adapter.modify_mass(1)
print(adapter.get_data())
