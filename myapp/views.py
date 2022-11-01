from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
from scipy.stats import norm
from collections import Counter
import numpy as np
from .forms import resultados
import pandas as pd
import openpyxl 
# Create your views here.


def hello(request, username):
    return HttpResponse(username)


def distriNormal(lista):

    mu = np.mean(lista)
    sigma = np.std(lista)
    x1 = min(lista)
    x2 = max(lista)

    z1 = (x1-mu)/sigma
    z2 = (x2-mu)/sigma

    x = np.arange(z1, z2, 0.0001)
    x2 = np.arange(-10, 10, 0.0001)
    y = norm.pdf(x, 0, 1)
    y2 = norm.pdf(x2, 0, 1)
    fig, ax = plt.subplots(figsize=(9, 6))
    plt.style.use("fivethirtyeight")
    ax.plot(x2, y2)
    ax.fill_between(x, y, 0, color="g")
    ax.fill_between(x2, y2, 0, alpha=0.1)
    ax.set_xlabel("numero de elementos fuera del promedio")
    ax.set_title("Distribucion normal")
    plt.savefig("gaussiana.png")


def entero(x):
    return parseInt(x)


def index(request):
    # = [1,2,2,25,3,2,4,5,2,5,6,7,3,5,2,4,5,6,7,4,20,30,43,22,19,3]
    lista = []
    if (request.GET['array'] == '' and request.GET['file'] != ''):
        print("entre")
        read = pd.read_csv(request.GET['file'])
        read = read.values
        print(len(read))
        lista = read
    elif (request.GET['array'] != ''):
        lista = request.GET['array']
        lista = lista[1:]
        lista = lista[:-1]
        lista = lista.split(',')

        lista = [int(x) for x in lista]

        print(lista)

        media = np.mean(lista)
        mediana = np.median(lista)
        desviacion = np.std(lista)
        varianza = np.var(lista)
        minimo = min(lista)
        maximo = max(lista)
        counter = Counter(lista)
        moda = counter.most_common()
        moda2 = moda[0]
        distriNormal(lista)

        return render(request, 'index.html', {
            'mediana': mediana,
            'media': media,
            'desviacion': desviacion,
            'varianza': varianza,
            'min': minimo,
            'max': maximo,
            'moda': moda2,
        })
    else:
        return HttpResponse("404")


def about(request):
    return HttpResponse("About")


def input(request):

    return render(request, 'input.html', {
        'form': resultados
    })
