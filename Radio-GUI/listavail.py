import subprocess
PATH_OF_AIRPORT: str = (
    "/System/Library/PrivateFrameworks/"
    "Apple80211.framework/Versions/Current/Resources/airport"
)
process = subprocess.Popen([PATH_OF_AIRPORT, "-s"], stdout=subprocess.PIPE)
out, err = process.communicate()
process.wait()
lines = out.decode("utf-8").splitlines()
ssidList = []
for a in lines:
    ssidList.append(a.strip().split(" ")[0])