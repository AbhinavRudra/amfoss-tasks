'''
Eren's assignment is straightforward: he is given an enigmatic elemental construct suspended in a mystical chamber, and he must ascertain whether the construct is in a state of mystical equilibrium or if it is undergoing ethereal motion.
The elemental construct is depicted as a mystical point with coordinates (0, 0, 0). Eren believes that by summing all the vectors acting upon it, he can determine if the construct remains perfectly still or if it's experiencing instability by checking if the coordinates add up to 0.
Now, seeking the counsel of a skilled wizard like yourself, Eren implores your assistance in crafting a program that can skillfully decipher the state of the elemental construct based on the given vectors of mysterious forces. Your expertise in the arcane arts shall be pivotal in helping Eren overcome this intricate challenge.
'''
n = int(input())
x, y, z = 0, 0, 0

for i in range(n):
    a, b, c = map(int, input().split())
    x += a
    y += b
    z += c

if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
