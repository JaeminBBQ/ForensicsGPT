let caseName = document.getElementById("caseName");
let investigatorName = document.getElementById("investigatorName");
let caseDate = document.getElementById("caseDate");
let caseLocation = document.getElementById("caseLocation");
let deviceType = document.getElementById("deviceType");
let operatingSystem = document.getElementById("operatingSystem");
let serialNumber = document.getElementById("serialNumber");
let deviceStatus = document.getElementById("deviceStatus");
let accessConditions = document.getElementById("accessConditions");
let evidenceDetails = document.getElementById("evidenceSource");
let evidenceType = document.getElementById("evidenceType");
let timeFrame = document.getElementById("timeframe");
let violations = document.getElementById("violations");
let summary = document.getElementById("summary");
let evidence = document.getElementById("evidence");

let submitbutton = document.getElementById("submitbutton");


let ic = (icecream) => {
    console.log(icecream);
}

submitbutton.onclick = async () => {
    const body_data = new FormData();

    body_data.append("caseName", caseName.value);
    body_data.append("investigatorName", investigatorName.value);
    body_data.append("caseDate", caseDate.value);
    body_data.append("caseLocation", caseLocation.value);
    body_data.append("deviceType", deviceType.value);
    body_data.append("operatingSystem", operatingSystem.value);
    body_data.append("serialNumber", serialNumber.value);
    body_data.append("deviceStatus", deviceStatus.value);
    body_data.append("accessConditions", accessConditions.value);
    body_data.append("evidenceDetails", evidenceDetails.value);
    body_data.append("evidenceType", evidenceType.value);
    body_data.append("timeFrame", timeFrame.value);
    body_data.append("violations", violations.value);
    body_data.append("summary", summary.value);
    body_data.append("evidence", evidence.value);


    let tableParam = {
        method: "POST",
        body: body_data
    };
    const url = "http://localhost:8000/" + "api/llama/";

    const res = await fetch(url, tableParam);

    let json_data = await res.json();
}