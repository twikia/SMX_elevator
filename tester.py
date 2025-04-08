import elevator as script

# tuple of list, list, int
tests = [([5, 5, 5, 4, 1, 1], [5, 4, 1], 40),
        ([1], [1], 0),
        ([], [], 0),
        ([1, 2, 3, 6, 4], [1, 2, 3, 4, 6], 50), # test all above
        ([6, 4, 3, 2, 1], [6, 4, 3, 2, 1], 50), # test all below
        ([6, 4, 2, 7, 8], [6, 4, 2, 7, 8], 100), # test going down first
        ([-6, -4, -2, -7, -8], [-6, -4, -2, -7, -8], 100), # test negative nums
        # ai test cases
        ([1, 2, 3], [1, 2, 3], 20),
        ([3, 2, 1], [3, 2, 1], 20),
        ([1, 5, 2, 4, 3], [1, 2, 3, 4, 5], 40),
        ([4, 8, 1, 3, 2], [4, 8, 3, 2, 1], 110),
        ([10, 2, 8, 4, 6], [10, 8, 6, 4, 2], 80),
 
        ]

def test():
    for test in tests:
        
        res = script.main(test[0])
        if res[0] != test[2] or res[1] != test[1]:
            print("test failed")
            print("test:", test[0])
            print(test[2])
            print(test[1])
            print("results:")
            print(res)
            
        else:
            print(f"test passed {test[2]}")


if __name__ == "__main__":
    test()
