import configparser


def readLocator(section, key):
    reader = configparser.ConfigParser()
    reader.read("/Users/astham/PycharmProjects/Verifysite/verifysitecai/ConfigurationData/config.cfg")
    return reader.get(section, key)


a = readLocator("VerifySite", "localeSelector")
print(a)
