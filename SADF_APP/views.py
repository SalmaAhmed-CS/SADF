import joblib
from django.shortcuts import render , redirect

def index(request):
    if request.method == 'POST':
        c1 = request.POST['c1']
        c2 = request.POST['c2']
        c3 = request.POST['c3']
        c4 = request.POST['c4']
        c5 = request.POST['c5']
        c6 = request.POST['c6']
        c7 = request.POST['c7']
        c8 = request.POST['c8']
        c9 = request.POST['c9']
        c10 = request.POST['c10']
        c11 = request.POST['c11']
        c12 = request.POST['c12']
        c13 = request.POST['c13']
        c14 = request.POST['c14']
        c15 = request.POST['c15']
        c16 = request.POST['c16']
        c17 = request.POST['c17']
        c18 = request.POST['c18']
        c19 = request.POST['c19']
        c20 = request.POST['c20']
        c21 = request.POST['c21']
        c22 = request.POST['c22']
        c23 = request.POST['c23']
        c24 = request.POST['c24']
        c25 = request.POST['c25']
        c26 = request.POST['c26']
        c27 = request.POST['c27']
        c28 = request.POST['c28']
        c29 = request.POST['c29']
        c30 = request.POST['c30']

        c1 = int(c1)
        c2 = int(c2)
        c3 = int(c3)
        c4 = int(c4)
        c5 = int(c5)
        c6 = int(c6)
        c7 = int(c7)
        c8 = int(c8)
        c9 = int(c9)
        c10 = int(c10)
        c11 = int(c11)
        c12 = int(c12)
        c13 = int(c13)
        c14 = int(c14)
        c15 = int(c15)
        c16 = int(c16)
        c17 = int(c17)
        c18 = int(c18)
        c19 = int(c19)
        c20 = int(c20)
        c21 = int(c21)
        c22 = int(c22)
        c23 = int(c23)
        c24 = int(c24)
        c25 = int(c25)
        c26 = int(c26)
        c27 = int(c27)
        c28 = int(c28)
        c29 = int(c29)
        c30 = int(c30)

    # Load the model from the file
        knn_from_joblib = joblib.load('Saved_model.pkl')
        row1 = [(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30)]
        print("working !!")
        prodict = knn_from_joblib.predict(row1)
        return render(request, 'prodict.html', {'prodict': knn_from_joblib.predict(row1)})
    else:
        knn_from_joblib = joblib.load('Saved_model.pkl')
        row1 = [(1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2)]

        prodict = knn_from_joblib.predict(row1)
        return render(request, 'base.html', {'prodict': prodict})

