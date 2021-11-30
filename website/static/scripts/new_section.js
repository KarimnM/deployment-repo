function AddMeetingTimeEntry()
{
    const meetingTimesEntryDivName = "meetingTimesEntryDiv";
    const meetingTimesEntrySpanName = "meetingTimesEntrySpan";
    const maxNumMeetingTimes = 5;
    var meetingTimesContainerDiv = document.getElementById("AddMeetingTimeDiv");
    var numMeetingTimeEntries = document.getElementsByName(meetingTimesEntryDivName).length;
    if(numMeetingTimeEntries >= maxNumMeetingTimes)
        return;

    const newEntryDiv = document.createElement("div");
    const newEntrySpan = document.createElement("span");
    newEntryDiv.setAttribute("name", meetingTimesEntryDivName);
    newEntrySpan.setAttribute("name", meetingTimesEntrySpanName);

    const startTimeInput = document.createElement("input");
    startTimeInput.setAttribute("name", "startTimeInput");
    startTimeInput.setAttribute("type", "time");
    startTimeInput.required = true;

    const endTimeInput = document.createElement("input");
    endTimeInput.setAttribute("type", "time");
    endTimeInput.setAttribute("name", "endTimeInput");
    endTimeInput.required = true;

    var weekdaySelector = document.createElement("select");
    weekdaySelector.name = "meetingDaySelector";

    var days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];

    for (const day of days)
    {
        var option = document.createElement("option");
        option.value = day
        option.text = day
        weekdaySelector.appendChild(option);
    }

    const removeMeetingTimeButton = document.createElement("button");
    removeMeetingTimeButton.name = "deleteMeetingTimeButton";
    removeMeetingTimeButton.type = "button";
    removeMeetingTimeButton.onclick = function() { removeMeetingTimeButton.parentElement.parentElement.remove(); };
    removeMeetingTimeButton.textContent = '❌';


    newEntrySpan.appendChild(weekdaySelector);
    newEntrySpan.appendChild(startTimeInput);
    newEntrySpan.appendChild(endTimeInput);
    newEntrySpan.appendChild(removeMeetingTimeButton);
    newEntryDiv.appendChild(newEntrySpan);

    meetingTimesContainerDiv.appendChild(newEntryDiv);
}

