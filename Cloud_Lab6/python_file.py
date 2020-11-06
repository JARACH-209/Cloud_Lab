from typing import Callable, List
import math
#DO NOT MAKE UNNECESSARY CHANGES
class DistanceFuncs:
	def calc_distance(self, point_a: List[float], point_b: List[float], dist_func: Callable)->float:
		return dist_func(point_a, point_b)
	@staticmethod
	def euclidean(point_a: List[float], point_b: List[float])->float:
		return math.dist(point_a, point_b)
	@staticmethod
	def manhattan_distance(point_a: List[float], point_b: List[float]):
		raise NotImplementedError()
	@staticmethod
	def jaccard_distance(point_a: List[float], point_b: List[float]):
		raise NotImplementedError()

def main():
	test = DistanceFuncs()
	
	print("The distance is : ",test.calc_distance([2,3],[10,10],test.euclidean))
if __name__ =="__main__":
	main()