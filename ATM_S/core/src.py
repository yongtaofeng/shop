# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28
from  lib import  common
from interface import user,bank,shopping
from lib import common
user_log=common.get_logger('user')
user_info={
    'name':None
}



def login():
  print("登录")
  if user_info["name"]:
      print("您已经登录了")
      return
  count=0
  while True:
      name=input("请输入用户名:").strip()
      password=input("请输入密码：").strip()
      flag,msg=user.login_interface(name,password)
      if flag:
          print(msg)
          user_info['name']=name
          break
      else:
          count+=1
          if count >= 3:
              user.lock_user(name)
              user_log.info("%s的账户已被锁定"%name)
              break
          print(msg)
          break

def register():
    print("注册功能")
    if user_info["name"]:
      user_log.info("%s已经有账号了，不能在注册了"%user_info['name'])
      print("您已经登录了，不能注册")
    while True:
        name=input("请输入用户名：").strip()
        password=input("请输入密码：").strip()
        conf_password=input("请确认密码:").strip()
        if password == conf_password:
          flag,msg=user.register_interface(name,password)
          if flag:
              user_log.info("%s账户已经注册成功"%name)
              print(msg)

              break
          else:
              print(msg)
              break
        else:
            print("密码不正确")
            continue
@common.auth
def check_balance():
    print("查看余额")
    balance=bank.check_balance_interface(user_info['name'])
    print("您的余额为%s"%balance)
@common.auth
def transfer():
    print("转账")
    while True:
        to_user=input("输入要转给的用户:").strip()
        balance=input("输入转账金额:").strip()
        if balance.isdigit():
            balance=int(balance)
            flg,msg=bank.transfer_interface(user_info['name'],to_user,balance)
            if flg:
                print(msg)
                break
            else:
                print(msg)


@common.auth
def repay():
    print("还款")
    balance=input("请输入还款金额：").strip()
    if balance.isdigit():
       balance=int(balance)
       flg,msg=bank.repat_interface(user_info['name'],balance)
       print(msg)

@common.auth
def withraw():
    print("取款")
    while True:
        balance=input("请输入取款金额：").strip()
        if balance.isdigit():
           balance=int(balance)
           flag,msg=bank.withdraw_interface(user_info['name'],balance)
           if flag:
               print(msg)
               break
           else:
               print(msg)
               continue

@common.auth
def check_records():
    pass

@common.auth
def shop():
    user_balance = bank.check_balance_interface(user_info['name'])
    cost = 0
    shopping_cart = {}
    good_list = [
        ['coffee', 10],
        ['chicken', 20],
        ['iphone', 8000],
        ['macPro', 15000],
        ['car', 100000]
    ]
    while True:
        for i, good in enumerate(good_list):
            print("%s:%s" % (i, good))
        choice = input("请输入人你需要购买的商品：").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice > len(good_list):continue
            good_name = good_list[choice][0]
            good_price = good_list[choice][1]
            if user_balance >= good_price:
                if good_name in shopping_cart:
                    shopping_cart[good_name]['count'] += 1
                else:
                    shopping_cart[good_name] = {'price': good_price, 'count': 1}
                print("您成功将[%s]加入了购物车"%good_name)
                user_balance -= good_price
                cost += good_price
        if choice == 'q':
            if cost == 0:
                break
            print(shopping_cart)
            config=input("你确定购买完成了，开始结账吗？（y/n):").strip()
            if config == 'y':
                flag,msg=shopping.shooping_interface(user_info['name'],cost,shopping_cart)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
                    break
            else:
                print("您什么都没买")
                break
@common.auth
def check_shopping_cart():
    shopping.check_shoppingcart_interface(user_info['name'])

def logout():
    pass
func_dic = {
    '1': login,
    '2': register,
    '3': check_balance,
    '4': transfer,
    '5': repay,
    '6': withraw,
    '7': check_records,
    '8': shop,
    '9': check_shopping_cart,
    '10': logout
}


def run():
    while True:
        print('''
        1、登录
        2、注册
        3、查看余额
        4、转账
        5、还款
        6、取款
        7、查看流水
        8、购物
        9、查看购买商品        
        10、注销 
        ''')
        choice = input("请输入你需要的选择：").strip()
        if choice == 'q':break
        if choice not in func_dic: continue
        func_dic[choice]()
