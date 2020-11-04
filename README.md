# Monkey-Challenge
Given a Jungle in the middle of an island of n*m dimensions. Each field in this jungle contains a positive integer which is the amount of bananas that exist in that field. Initially the monkey is at first column but can be at any row. The monkey can move only (right->,right up /,right down\) from a given cell. Find out the maximum amount of bananas they can collect.

# Solution
I created a method to make the monkey challenge, my idea was verify all lines of the field to check the first column and after that check only the 3 possible options.
If I think in an entire solution, I will create a verification to the matrix, to check if the structure of this matrix is ok, and I will create a solution to the user create a matrix, but that is not the challenge asked, so I skip this steps.

# Solution (Portuguese)
Eu criei um método para fazer o "Monkey Challenge", minha ideia era verificar todas as linhas da "floresta" para ver a primeira coluna e depois disso verificar apenas as 3 opções possíveis.
Se eu fosse pensar em uma solução completa, eu iria criar uma verificação para a matriz, para verificar se a matriz está estruturamente correta, e iria criar uma solução para o usuário preencher a matriz, mas isso não é o que o desafio pedia então eu pulei esses passos.

# Result

sample 1: 


12

['1, 0', '2, 1', '0, 2']



sample 2: 


16

['2, 0', '3, 1', '2, 2', '0, 3']



sample 3: 


83

['1, 0', '0, 1', '0, 2', '0, 3']
