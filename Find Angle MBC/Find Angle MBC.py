import math
LengthOfAB = int(input().strip())
LengthOfBC = int(input().strip())
LengthOfAC_Squared = (LengthOfAB*LengthOfAB) + (LengthOfBC*LengthOfBC)
LengthOfAC = math.sqrt(LengthOfAC_Squared)
LengthOfMc = LengthOfAC/2
CosienMBC = LengthOfBC / LengthOfAC
AngleMBCInRad = math.acos(CosienMBC)
AngleMBCInDegree = (AngleMBCInRad*180)/math.pi
AngleMBCInDegree = round(AngleMBCInDegree)
AngleMBCInDegree = str(AngleMBCInDegree)
print(AngleMBCInDegree + chr(176))
