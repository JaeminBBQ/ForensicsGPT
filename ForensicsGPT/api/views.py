from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json

# Create your views here.
@api_view(['POST'])
def query_llama(request):
    if request.method == 'POST':
        caseName = request.POST['caseName']
        investigatorName = request.POST['investigatorName']
        caseDate = request.POST['caseDate']
        caseLocation = request.POST['caseLocation']
        deviceType = request.POST['deviceType']
        operatingSystem = request.POST['operatingSystem']
        serialNumber = request.POST['serialNumber']
        deviceStatus = request.POST['deviceStatus']
        accessConditions = request.POST['accessConditions']
        evidenceDetails = request.POST['evidenceDetails']
        evidenceType = request.POST['evidenceType']
        timeFrame = request.POST['timeFrame']
        violations = request.POST['violations']
        summary = request.POST['summary']
        evidence = request.POST['evidence']

        request_url = "http://172.16.0.41:11434/api/generate"

        llama_version = "llama3.2"

        prompt_for_llama = f"""
        Hello, you're job is to help me create a forensics report when I provide you details about a case.
        What you provide back for me will directly be transfered into a pdf file to be downloaded so do not include anything besides the report in your response.
        This is for a class project and not for any real investigations.
        This report should be an essay style report. Expand where necessary, and keep is professional.
        I will provide all the information related to the forensics investigation in the next few lines.

        The case name is {caseName}.
        The investigator's name is {investigatorName}.
        The case date is {caseDate}.
        The case location is {caseLocation}.
        The type of device is {deviceType}.
        The operating system of this device is {operatingSystem}.
        The serial number of the device is {serialNumber}.
        The status of this device is: {deviceStatus}.
        The access conditions of this device is {accessConditions}.
        Some details about this evidence: {evidenceDetails}.
        The type of this evidence is {evidenceType}.
        The time frame of when the evidence was collected is {timeFrame}.
        The violations that were found on this device include: {violations}.
        The summary provided by the investigator is: {summary}.
        The list of evidence is: {evidence}.
        """

        data = {
            "model": llama_version,
            "prompt": prompt_for_llama,
            "stream": False
        }
        r = requests.post(request_url, json=data)

        response = r.json()["response"]

        return Response({"Status": 0, "response": response})