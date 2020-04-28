"""
MondoDBについて
・ドキュメント指向データーベース
・json形式で記述してDBに保存するのでSQL文を必要としない(No SQL)
・mongodbでは大体時間も保存する
・mongodbは大体ログなどを大量に保存するのに使う
"""

import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'date': datetime.datetime.utcnow()
}

stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'date': datetime.datetime.utcnow()
}
# stacksという名前のテーブルを作成（しているようなイメージ）
db_stacks = db.stacks
# stack1の内容をDBに投入して、その後返ってきたidをstack_idという名前の変数に格納
# stack_id = db_stacks.insert_one(stack1).inserted_id
# print(stack_id, type(stack_id))


from bson.objectid import ObjectId

# スタックIDを文字列で格納(このままだと検索できないので下記のようにObjectIdで囲って変換する必要がある)
# str_stack_id = '5ea80d9345ecee4d0e3ee233'
# 上記で投入したデータをDBから取得
# print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))

# id以外でも検索できる
# print(db_stacks.find_one({'name': 'customer1'}))
# print(db_stacks.find_one({'pip': ['python', 'java', 'go']}))


# stack_id = db_stacks.insert_one(stack2).inserted_id
# print(stack_id, type(stack_id))

# データベースを全部取得する場合
# for stack in db_stacks.find():
#     print(stack)

# 時間での検索方法
# now = datetime.datetime.utcnow()
# lt...less than 今より過去のもの、gt...greater than 今より未来のもの
# for stack in db_stacks.find({'date': {'$lt': now}}):
#     print(stack)

# name: customer1のデータをname: yyyにアップデート
db_stacks.find_one_and_update(
    {'name': 'customer1'}, {'$set': {'name': 'yyy'}}
)
print(db_stacks.find_one({'name': 'yyy'}))

# name: customer1のデータ削除
db_stacks.delete_one({'name': 'yyy'})
print(db_stacks.find_one({'name': 'yyy'}))
