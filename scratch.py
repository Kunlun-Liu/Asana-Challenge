

while count < days_logged:
    if (i + 2) < visited:  # needs to be at least 3 entries left
        if (user['time_stamp2'].iloc[i + 1] - user['time_stamp2'].iloc[i]) <= pd.Timedelta(days=period) and (
                user['time_stamp2'].iloc[i + 1] - user['time_stamp2'].iloc[i]) > pd.Timedelta(days=1):
            count += 1  # logged in twice within a 7 day period
            new_timeframe = (user['time_stamp2'].iloc[i + 1] - user['time_stamp2'].iloc[i])
            if (user['time_stamp2'].iloc[i + 2] - user['time_stamp2'].iloc[i + 1]) <= new_timeframe and (
                    user['time_stamp2'].iloc[i + 2] - user['time_stamp2'].iloc[i + 1]) > pd.Timedelta(days=1):
                active_user = True  # they logged in three times within a 7 period window
                count += 1
            else:
                i += 1
                count = 1
        else:
            i += 1
            count = 1
    else:
        count = days_logged
return active_user

import pandas as pd

data = pd.read_csv("takehome_user_engagement-intern.csv")
data["time_stamp"] = pd.to_datetime(data['time_stamp'])


def createAdopted(data,days_logged=3,period=6):
    adopted = {}
    data["time_stamp"] = pd.to_datetime(data['time_stamp'])
    for id in pd.unique(data["user_id"]):
        subset = data[data["user_id"] == id]
        if subset.shape[0] >= days_logged:
            for i in range(len(subset)-2):
                if abs(subset.iloc[i,0]-subset.iloc[i+2,0]) <= pd.Timedelta(days=period):
                    adopted[id] = 1
                    break
        else:
            adopted[id] = 0
    df = pd.DataFrame(list(adopted.items()), columns=["user_id", "adopted"])
    return df

df = createAdopted(data,3,7)

pd.value_counts(df["adopted"])

def checkDays(data,separate=1):
    data["time_stamp"] = pd.to_datetime(data['time_stamp'])
    for id in pd.unique(data["user_id"]):
        subset = data[data["user_id"] == id]
        subset["time_stamp"] = list(set(subset["time_stamp"]))
        for i in range(len(subset)-1):
            if abs(subset.iloc[i, 0] - subset.iloc[i + 1, 0]) != pd.Timedelta(days=separate):
                return False

print(checkDays(data,1))

pd.DataFrame(list(set(data["time_stamp"])))
