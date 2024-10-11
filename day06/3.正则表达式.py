# re模块
import re

# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')


# print(m.group(1))
# print(m.group(2))

# 编译
# re_telephone = re.compile(r"^((13|15|18|19)([0-9]{9}+))$")


# res = re_telephone.match("13001723623").groups()

# print(res)

# 正则表达式邮箱

res_email = re.compile(r"^\<([\d\w\s+]+)\>([\s\d\w]+)(\.?)([\d\w]+)@(([\d\w]+)).(([\d\w]{2,4}))$")


def is_valid_email(addr):
    res = res_email.match(addr)
    if res != None:
        return True
    else:
        return False
def name_of_email(addr):
    res = res_email.match(addr)
    if res != None:
        return res.group(1)
    else:
        return False
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
print(name_of_email('<Tom Paris> tom@voyager.org'))
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'

print('ok')