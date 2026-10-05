from index import square

def main():
    test_squere()
    
def test_squere():
    assert square(3)==9
    assert square(2)==4
    
    
if __name__=="__main__":
    main()