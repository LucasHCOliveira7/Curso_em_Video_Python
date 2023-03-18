# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite uma medida em metros: '))
km = medida / 1000
hc = medida / 100
dam = medida / 10
m = medida
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida {}m corresponde a: \n{} quilômetros \n{} hectômetros \n{} decâmetros'
      '\n{} decímetros \n{} centímetros \n{} milímetros'.format(medida, km, hc, dam, dm, cm, mm))
