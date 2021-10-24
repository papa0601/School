while True:
    print("\n\n\n")
    while True:
        try:
            formula = (input("계산할 식을 입력하세요>>>")).replace(" ", "")
            if formula.count("+") + formula.count("*") + formula.count("/") > 1:
                raise(ZeroDivisionError)
            else:
                checkf = formula.count("*") + formula.count("/")
                if checkf == 0:
                    if formula.find("+") == -1:
                        list = (formula.replace("-", "+-")).split("+")
                        result = int(list[0]) + int(list[1])
                    else:
                        list = formula.split("+")
                        result = int(list[0]) + int(list[1])

                else:
                    if formula.find("*") == -1:
                        list = formula.split("/")
                        result = int(list[0]) / int(list[1])
                    else:
                        list = formula.split("*")
                        result = int(list[0]) * int(list[1])
                
                break

        except:
            print("오류가 발생했습니다! 식을 확인하고 다시 입력해주세요.")


    print("계산 결과 : " + str(result))