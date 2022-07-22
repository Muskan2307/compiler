from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'CompilerPython/index.html')

def runcode(request):
    if request.method == "POST":
        import sys
        codeareadata = request.POST['codearea']
        original_stdout=sys.stdout
        try:
            sys.stdout = open('file.txt', 'w')
            exec(codeareadata)
            sys.stdout.close()
            sys.stdout = original_stdout
            output = open('file.txt', 'r').read()

        except Exception as e:
            output = e
    return render(request, 'CompilerPython/index.html', {"code":codeareadata , "output":output})
