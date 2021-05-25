# moduł.py

###Blok do wykonania zawsze###

def kwadrat(x):
    return x**2

zmienna = ["wartość zmiennej","kolejna wartość"]

##############################

if __name__ == "__main__":
    ## Blok do wykonania jedynie przy uruchamianiu modułu jako program ##
    print(f"kwadrat(25) = {kwadrat(25)}")
    print(f"zmienna: {zmienna}")
    zmienna.append("inna wartość")
    print(f"zmienna: {zmienna}")
