import pandas as pd
df = pd.read_csv('Info.csv', sep = ";")
delete = []
to_del = df[(df["ap_hi"]<df["ap_lo"])]['id']
to_del1 = df[(df['height'].quantile(0.025)>df['height'])]['id']
to_del2 = df[(df['height'].quantile(0.975)<df['height'])]['id']
to_del3 = df[(df['weight'].quantile(0.025)>df['weight'])]['id']
to_del4 = df[(df['weight'].quantile(0.975)<df['weight'])]['id']
DELETE = (to_del, to_del2, to_del1, to_del3, to_del4)
for ever in DELETE:
    for i in ever:
        delete.append(i)
df = df.drop(delete)
d = len(delete)
f = len(df)
print("Процент удаленных строк "+str(((d/f)*100)))
df["BMI"] = df['weight']/((df['height']/100)**2)
print("+ BMI: ")
print(df)
string = df["gender"].value_counts()
answ = []
for ever in string:
    answ.append(ever)
female = answ[0]
male = answ[1]
print("Мужчин "+str(male))
print("Женщин "+str(female))
smoking = pd.crosstab(df["smoke"], df["gender"])
psf=(smoking[1][1])/female
psm=(smoking[2][1])/male
freq = int(round(psm/psf))#Процент курящих мужчин: процент курящих женщин
print("Процент курящих мужчин к проценту курящих женщин "+str(freq))
slife = df[df['smoke'] == 1]["age"].mean()
life = df[df["smoke"] == 0]['age'].mean()
razn = int(round((life - slife)/30))
print("Разница в возрасте[мес] курящих и не курящих "+str(razn))
new = df[(df["age"])&(df['smoke']==1)&(df['gender'] == 2)]
new1 = pd.DataFrame(data = new, columns=['age', 'ap_hi','cholesterol',"cardio"])
new2 = new1[(new1["age"]/365)<65]
new3 = new2[new2["age"]/365>=60]
new3 = pd.DataFrame(data = new3)
new3['age']= round(new3['age']/365)
sample1 = new3[(new3["ap_hi"] == 120)&(new3["cholesterol"] == 1)]
sample2 = new3[(new3["ap_hi"] >= 160)&(new3["cholesterol"] == 3)&(new3["ap_hi"] < 180)]
pcs2 = (sample2['cardio'].value_counts()[1])/(sample2['cardio'].value_counts()[1]+sample2['cardio'].value_counts()[0])
pcs1 = (sample1['cardio'].value_counts()[1])/(sample1['cardio'].value_counts()[1]+sample1['cardio'].value_counts()[0])
print("Отношение количества больных курящих мужчин к здоровым курящим мужчинам "+str(round(pcs2/pcs1)))




