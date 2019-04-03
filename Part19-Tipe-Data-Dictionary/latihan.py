kelas_gold = {
    "id" : "101",
    "name" : "kevin",
    "job" : "engineer",
    "member type" : "gold"
}, {
    "id" : "103",
    "name" : "edwin",
    "job" : "soldier",
    "member type" : "gold"
}

kelas_silver = {
    "id" : "102",
    "name" : "joseph",
    "job" : "techer",
    "member type" : "silver"
}

all = {101:kelas_gold[0],102:kelas_silver,103:kelas_gold[1]}

for i in range(101,104):
    print(all[i])