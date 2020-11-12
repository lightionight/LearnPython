#BMI = 体重除以身高的平方；
height = 1.75;
weight = 80.5;
bmi = height % (weight * weight);
if bmi > 32:
    print("高于32：严重肥胖");
elif bmi < 32.0 and bmi > 28.0:
    print("28-32:肥胖");
elif bmi < 28 and bmi > 25:
    print("25-28:过重");
elif bmi <25 and bmi > 18.5:
    print("18-25:正常");
else:
    print("低于18.5: 过轻")