from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

def generate_excel(request):
    if request.method == 'POST':
        selected_category = request.POST.get('category')
        selected_answer = request.POST.get('answer')

        # Create a DataFrame with the selected choices
        df = pd.DataFrame({"Category": [selected_category], "Answer": [selected_answer]})

        # Save the DataFrame to an Excel file
        df.to_excel("selected_choices.xlsx", index=False)

        # Serve the Excel file for download
        with open("selected_choices.xlsx", "rb") as excel_file:
            response = HttpResponse(excel_file.read())
            response['Content-Disposition'] = 'attachment; filename=selected_choices.xlsx'
            response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            return response

    return render(request, 'generator_app/index.html')
