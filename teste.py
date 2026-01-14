celsius = float(input("Digite a temperatura em celsius: "))

kelvin = (celsius + 273.15)

print(f"A temperatura de celsius {celsius}°C equivale a {kelvin: .1f}°K" )




#float(): Essencial aqui. Se você digitar 25, o Python entende como o texto "25". Para fazer contas, o float transforma isso no número 25.0.

#Ordem de Precedência: Em Python, as operações seguem a regra matemática (multiplicação e divisão antes de soma). Por isso, celsius * 9/5 é calculado primeiro, e o resultado é somado a 32.

#f-strings: É a maneira mais moderna e limpa de exibir variáveis no meio de frases em Python.