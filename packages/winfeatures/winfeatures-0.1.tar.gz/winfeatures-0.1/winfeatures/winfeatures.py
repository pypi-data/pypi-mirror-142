import os

def install(feature):
    packageName = feature
    import os
    os.system("dism /online /Enable-Feature /FeatureName:" + packageName + "/All")

if __name__ == "__main__":
    install()