

def outer():

    y = 12
    def answer():
        return x
    return answer()
if __name__ == '__main__':
    x =42
    print(f'y in main is exists: {"y" in locals()}')