class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        parts = ip.split(".")
        binarySections = []
        for part in parts:
            binarySections.append(f"{int(part):08b}")
        base = int("".join(binarySections), 2)
        cidrs = []
        while n > 0:
            binary = f"{base:032b}"
            numCovered = 1
            numDigits = 0
            for i in range(len(binary) - 1, -1, -1):
                if binary[i] != "0" or numCovered * 2 > n:
                    break
                numCovered *= 2
                numDigits += 1
            n -= numCovered
            cidrs.append(self.toCIDR(binary, numDigits))
            base += numCovered
        return cidrs

    def binaryToIP(self, binary):
        return f"{int(binary[:8], 2)}.{int(binary[8:16], 2)}.{int(binary[16:24], 2)}.{int(binary[24:], 2)}"

    def toCIDR(self, binary, numDigits):
        return f"{self.binaryToIP(binary)}/{32 - numDigits}"

    def printIPs(self, ip: str, n: int):
        for i in range(n):
            num = int(ip.replace(".", "")) + i
            print(str(bin(num))[2:])
