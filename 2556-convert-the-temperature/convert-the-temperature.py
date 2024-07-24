class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = 273.15 + celsius
        far = celsius * 1.80 + 32
        return [kelvin, far]
        