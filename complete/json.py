import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"},
        ]
}

print(j)
print("################")
# json形式にして読み込み(dumps)
# print(json.dumps(j))
a = json.dumps(j)
# pythonの中でjsonを読み込み(loads)
json.loads(a)

# json形式としてファイルに書き込み(dump)
with open('test.json', 'w') as f:
    json.dump(j, f)

print("################")

# jsonファイルを読み込み(load)
with open('test.json', 'r') as f:
    print(json.load(f))
