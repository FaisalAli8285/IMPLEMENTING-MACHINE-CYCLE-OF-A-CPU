hexa_input = input("Enter a number in hexa decimal form : ")
decimal_value = int(hexa_input, 16)  # convert the hexadecimal to decimal
binary_value = bin(decimal_value)[2:].zfill(32)  # convert to binary and pad to 32 bits

operand1 = int(binary_value[0:8], 2)
operand2 = int(binary_value[8:16], 2)
alu_enable = int(binary_value[16:17], 2)  # Extract the 17th bit correctly
opCode = int(binary_value[17:21], 2)
Reserved = binary_value[21:32]
result = 0
status = 0

# Checking the ALU enable flag
if alu_enable == 1:
    if opCode == 0:
        result = operand1 + operand2
    elif opCode == 1:
        result = operand1 - operand2
    elif opCode == 2:
        result = operand1 * operand2
    elif opCode == 3:
        result = operand1 / operand2 if operand2 != 0 else "Error: Division by Zero"
    else:
        result = "Invalid Operator"
    status = 1
else:
    result = "ALU Disabled"

register = result

print(f"Instruction: {hexa_input}")
print(f"Binary Instruction: {binary_value}")
print(f"Operand 1: {operand1}")
print(f"Operand 2: {operand2}")
print(f"ALU Enable: {alu_enable}")
print(f"Opcode: {opCode}")
print(f"Reserved Bits: {Reserved}")
print(f"Result: {result}")
print(f"Status: {status}")
print(f"Register: {register}")
