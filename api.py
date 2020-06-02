from flask import Flask, json, request


api = Flask(__name__)

def converter(num):
    roman_nums = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    rom = []
    for i in roman_nums:
        k = num // i
        num -= k * i
        n = k*roman_nums[i]
        rom.append(n)
    return ''.join(rom)

@api.route('/', methods=['POST'])
def get_students():
    alpha = request.form["number"]
    return converter(alpha)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=80)