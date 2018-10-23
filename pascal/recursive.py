from sys import argv
from contextlib import redirect_stdout
def bin_coeff(n , k): 
	return 1 if k == 0 or k == n else bin_coeff(n-1 , k-1) + bin_coeff(n-1 , k) 
if __name__ == "__main__":
    n = int(argv[1])
    k = int(argv[2])
    with open("triangle.out", "w", encoding="utf-8") as out:
        with redirect_stdout(out):
            for i in range(1,n): 
                p = 1;
                for j in range(1,k):
                    if p > 0:
                        print(int(p),end=" ")
                        p = p * (i - j) / j
                print('\n')
