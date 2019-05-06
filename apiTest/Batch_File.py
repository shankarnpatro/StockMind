import os
def batchScript():
    os.system('requestApi.py')
    """
    calling register module
    """
    print("Sucessfully exucted 1st file")
    os.system('userUpdateApi.py')
    print("Sucessfully exucted 2nd file")
    os.system("EquityBuyApiPost.py")
    print("Sucessfully exucted 3rd file")
    os.system("EquitySellApiPost.py")
    print("Sucessfully exucted 4th file")

batchScript()
