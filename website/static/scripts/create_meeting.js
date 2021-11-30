
function getCssValuePrefix()
{
    var rtrnVal = '';//default to standard syntax
    var prefixes = ['-o-', '-ms-', '-moz-', '-webkit-'];
    // Create a temporary DOM object for testing
    var dom = document.createElement('div');
    for (var i = 0; i < prefixes.length; i++)
    {
        // Attempt to set the style
        dom.style.background = prefixes[i] + 'linear-gradient(#000000, #ffffff)';
        // Detect if the style was successfully set
        if (dom.style.background)
        {
            rtrnVal = prefixes[i];
        }
    }
    dom = null;
    delete dom;
    return rtrnVal;
}

function hexToRgb(hex)
{
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})?$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}


const hoursPerCell = 2;
const calendarStartHour = 8;
const calendarStartMinutes = calendarStartHour * 60;
const daysInCalendarWeek = 5;

// var

function getCellIndexForTime(startDayNumber, startHour, startMinute)
{
    console.assert(0 <= startDayNumber && startDayNumber < 5); // 0 = Monday, 4 = Friday
    console.assert(startHour >= calendarStartHour);
    console.assert(0 <= startMinute && startMinute < 60);
    var startTime = startHour + startMinute/60;
    return Math.floor((startTime - calendarStartHour) / hoursPerCell) * daysInCalendarWeek + startDayNumber;
}

function eventStartPercent(startHour, startMinute)
{
    var startTime = startHour + startMinute/60;
    var startPercent = (startTime - calendarStartHour) % hoursPerCell / hoursPerCell * 100;
    return startPercent.toString() + "%";
}

function eventHeightPercent(eventDurationHours)
{
    var heightPercent = eventDurationHours / hoursPerCell * 100;
    return heightPercent.toString() + "%";
}

function addTimeToCalendar(startDayNumber, startHour, startMinute, endHour, endMinute, color1, color2=null)
{
    if(color2 == null)
        color2 = color1;
    // example run:    addTimeToCalendar(1, 13, 30, 0, 0, 'red');
    var tableCells = document.getElementsByClassName("content")[0];

    var index = getCellIndexForTime(startDayNumber, startHour, startMinute);
    var targetDiv = tableCells.children[Math.floor(index)];

    var startPercent = eventStartPercent(startHour, startMinute);
    var eventDuration = endHour - startHour + (endMinute - startMinute) / 60;
    var heightPercent = eventHeightPercent(eventDuration);

    var eventDiv = document.createElement("div");
    eventDiv.setAttribute("class", "eventDiv");

    eventDiv.style.position = 'absolute';

    eventDiv.style.display = 'block';
    eventDiv.style.top = startPercent;
    eventDiv.style.left = '0px';
    eventDiv.style.boxSizing = "border-box";
    eventDiv.style.background = getCssValuePrefix() + "linear-gradient(135deg, " + color1 + ", " + color2 + ")";
    eventDiv.style.height = heightPercent;
    eventDiv.style.width = '100%';


    var rgb = hexToRgb(color1);
    var boxShadowString = "0 20px 30px 0 rgba(" + rgb.r + ", " + rgb.g + ", " + rgb.b + ", 0.3)";
    eventDiv.addEventListener('mouseenter', function() {
         eventDiv.style.transform = "scale(1.05)";
         eventDiv.style.boxShadow = boxShadowString;
      });
    eventDiv.addEventListener('mouseleave', function(){
        eventDiv.style.transform = "scale(1.00)";
        eventDiv.style.boxShadow = "none";
    });
    targetDiv.appendChild(eventDiv);
}


/*
const selectElement = document.querySelector('.ice-cream');

selectElement.addEventListener('change', (event) => {
  const result = document.querySelector('.result');
  result.textContent = `You like ${event.target.value}`;
});
*/

// study_groups_meeting_times:
//      study_groups_meeting_times = dict()  # studyGroupID -> {"vnumbers": v_numbers, 'names': names, 'sections': sections, 'section_meeting_times': section_meeting_times, 'colors': v_number_to_color} for that given study group
function populateCalendarOnSelect(e)
{
    clearCalendar();
    var studyGroupID = e.value;
    console.log(studyGroupID);
    console.log(study_groups);
    console.log(study_groups_meeting_times);
    var studyGroupData = study_groups_meeting_times[studyGroupID];
    for(var i = 0; i < studyGroupData["section_meeting_times"].length; i++)
    {
        var vnumber = studyGroupData["vnumbers"][i];
        var color = studyGroupData["colors"][vnumber];
        var meeting_time = studyGroupData['section_meeting_times'][i];
        var startTime = meeting_time["start_time"];
        var endTime = meeting_time["end_time"];
        var startHour = startTime["hour"];
        var startMinute = startTime["minute"];
        var endHour = endTime["hour"];
        var endMinute = endTime["minute"];
        var dayNumber = meeting_time['weekday_num'];
        addTimeToCalendar(dayNumber, startHour, startMinute, endHour, endMinute, color); //, color2=null)
    }

}


function clearCalendar()
{
    var calendarSquares = document.getElementsByClassName("calendarSquare");
    for (const calendarSquare of calendarSquares) {
        removeAllChildrenOfElement(calendarSquare);
    }
}

function removeAllChildrenOfElement(element)
{
    while (element.firstChild)
    {
        element.removeChild(element.lastChild);
    }
}


function setAddressInputText(s)
{
    document.getElementById("AddressInputTextBox").value = s;
}

function filterAddressListByAvailableStudyTools()
{
    var checkboxes = document.getElementsByClassName('studyToolCheckbox');
    var checkedBoxes = [];
    for(checkbox of checkboxes)
    {
        if(checkbox.checked)
            checkedBoxes.push(checkbox.value);
    }
    console.log(study_tools);

    const validAddresses = new Set();
    for(study_tool of study_tools)
    {
        var studyToolsOfAddress = study_tool['study_tools'];
        if(checkedBoxes.every(val => studyToolsOfAddress.includes(val)))
            validAddresses.add(study_tool['address']);
    }

    var addressListDiv = document.getElementById('AddressListDiv');
    addressListDiv.style.minHeight = addressListDiv.clientHeight + "px"; // lock in height before deleting things

    var addressAnchors = document.getElementsByClassName('Address');
    for(addressAnchor of addressAnchors)
    {
        if(validAddresses.has(addressAnchor.dataset.value))
            addressAnchor.style.display = "block";
        else
            addressAnchor.style.display = "none";
    }

}

function showMeetingTypeOptions(e)
{
    var inpersonDiv = document.getElementById("InPersonInputDiv");
    var onlineDiv = document.getElementById("OnlineInputDiv");
    if(e.value == "Online")
    {
        inpersonDiv.style.display = "none";
        onlineDiv.style.display = "initial";
    }
    else if(e.value == "In-Person")
    {
        inpersonDiv.style.display = "initial";
        onlineDiv.style.display = "none";
    }
}
